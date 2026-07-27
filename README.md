# AnyLink

AnyLink is a modern web-based project designed to download videos from various online platforms using a simple and user-friendly interface. It supports popular sites such as YouTube, Instagram, TikTok, and Facebook, making it an all-in-one video link downloader.

## Overview

AnyLink allows users to paste a video URL, process it through the backend, and download media quickly and easily. The project combines:

- HTML for the page structure
- CSS for styling
- Bootstrap for responsive design
- Python for the downloader logic

## Features

- Simple and clean interface
- Supports video links from multiple platforms
- Responsive design for desktop and mobile
- Easy-to-use download experience

## Supported Platforms

- YouTube
- Instagram
- TikTok
- Facebook

## Project Structure

| File / Folder  | Description                             |
| -------------- | --------------------------------------- |
| app.py         | Python backend for the downloader logic |
| index.html     | Main web page for user interaction      |
| assets/        | Static files for the web app            |
| assets/css/    | Custom CSS styles                       |
| assets/js/     | JavaScript files                        |
| assets/vendor/ | Third-party libraries such as Bootstrap |
| README.md      | Project documentation                   |

## Getting Started

### 1. Install Python dependencies

Open a terminal in the project folder and run:

```bash
python -m pip install -r requirements.txt
```

If you are using the project virtual environment that was created locally, use:

```bash
d:/Projects/AnyLink/.venv/Scripts/python.exe -m pip install -r requirements.txt
```

### 2. Start the app

Run the Flask backend with:

```bash
d:/Projects/AnyLink/.venv/Scripts/python.exe app.py
```

Then open your browser at:

```text
http://127.0.0.1:5000
```

### 3. Use the downloader

1. Paste a supported video URL into the input field.
2. Click Download.
3. Wait for the backend to process the link and provide a download link.

## Notes

- The app uses Flask and yt-dlp to download videos from supported links.
- Some websites may block or restrict downloads, so results may vary depending on the source.

## Tech Stack

- HTML
- CSS
- Bootstrap
- Python

## Notes

AnyLink is designed as a lightweight web project for downloading videos from supported links. It can be expanded with more features such as format selection, batch downloads, and improved backend support.
