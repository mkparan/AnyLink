import os
import re
import uuid
from pathlib import Path

from flask import Flask, jsonify, request, send_file, send_from_directory

try:
    import yt_dlp
except ImportError:  # pragma: no cover - handled at runtime
    yt_dlp = None

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
DOWNLOAD_DIR = BASE_DIR / "downloads"
DOWNLOAD_DIR.mkdir(exist_ok=True)


def sanitize_url(url: str) -> str:
    value = (url or "").strip()
    if not value:
        raise ValueError("Please enter a video URL.")
    if not re.match(r"^https?://", value):
        raise ValueError("Please provide a full http:// or https:// URL.")
    return value


def download_video(url: str) -> Path:
    if yt_dlp is None:
        raise RuntimeError("yt-dlp is not installed. Install dependencies with pip install -r requirements.txt")

    safe_prefix = uuid.uuid4().hex
    output_template = str(DOWNLOAD_DIR / f"{safe_prefix}.%(title)s.%(ext)s")
    options = {
        "format": "best[ext=mp4]/best",
        "outtmpl": output_template,
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
        "socket_timeout": 30,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.extract_info(url, download=True)

    matches = sorted(DOWNLOAD_DIR.glob(f"{safe_prefix}.*"))
    if matches:
        return matches[-1]

    raise RuntimeError("The video could not be downloaded. The URL may be unsupported or the site may block downloads.")


@app.route("/")
def index():
    return send_file(BASE_DIR / "index.html")


@app.route("/<path:filename>")
def static_files(filename: str):
    return send_from_directory(BASE_DIR, filename)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/download", methods=["POST"])
def download():
    try:
        url = sanitize_url(request.form.get("url", ""))
    except ValueError as exc:
        return jsonify({"success": False, "error": str(exc)}), 400

    try:
        file_path = download_video(url)
    except RuntimeError as exc:
        return jsonify({"success": False, "error": str(exc)}), 400

    filename = file_path.name
    return jsonify({
        "success": True,
        "message": "Video downloaded successfully.",
        "download_url": f"/downloads/{filename}",
    })


@app.route("/downloads/<path:filename>")
def serve_download(filename: str):
    return send_from_directory(DOWNLOAD_DIR, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
