# py-ron — Claude Code Rules

> Per-project rules for Claude Code. The root `.claude/CLAUDE.md` rules also apply.

## Project Context

- **Type**: Submodule (added 2026-02-15) — Python image generation app
- **Purpose**: Generates Ron Swanson quotes on random Unsplash photos
- **Remote**: https://github.com/aaronjones003/py-ron
- **Tech Stack**: Python, PIL (Pillow), Requests, Unsplash API

## Project-Specific Rules

- This is a Python script that generates composite images
- Main script: `app.py`
- Fetches quotes from ron-swanson-quotes.herokuapp.com
- Fetches photos from Unsplash API (requires API key)
- Uses PIL for image processing and text overlay
- Dependencies listed in `requirements.txt`
- The app generates images and saves them locally
- When modifying, ensure proper error handling for API failures
- Font file `font.ttf` is used for quote text rendering

## File Organization

- `app.py` — Main application script
- `requirements.txt` — Python dependencies
- `font.ttf` — Font for text overlay
- `*.png` — Generated output images
- `index.html` — Simple web interface
