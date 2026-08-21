# first_python_projects

This repository contains my first Python programs — small, functional scripts I wrote while learning the basics.

---

## 1. Password Strength Checker

A command-line Python tool that scores password strength based on length, character variety, predictability, and membership in a common-password list.

### How it works

- **Common-password check (instant fail):** if the password matches an
  entry in a known-weak list, it scores 0 and stops there — no partial
  credit for a bad password just because it also has a digit in it.
- **Length (0–3 points):** 8+ chars = 1, 12+ = 2, 16+ = 3. Length
  contributes more to real-world entropy than any single character class,
  so it's weighted accordingly.
- **Character variety (0–4 points):** one point each for a digit,
  uppercase letter, lowercase letter, and special character.
- **Predictability penalty (−1):** deducted if the password contains a
  repeated run (`aaa`) or an ascending sequence (`abc`, `123`).
- **Rating:** score ÷ max score (7) → `STRONG` (≥85%), `MEDIUM` (≥50%),
  or `TOO WEAK` (below that).

### Usage

```bash
python3 password_strength_checker.py
```

You'll be prompted for a password via `getpass`, so it won't echo to the
terminal. The tool prints what's missing (if anything) and a final rating.

**Example:**

```
Enter your password: 
- Add at least one uppercase letter.
- Add at least one special character.

REMARKS -- Password is MEDIUM (4/7)
```

### Requirements

Python 3.6+, standard library only (`getpass`, `string`). No external
dependencies.

---

## 2. Snake, Water, Gun Game

A CLI variation of Rock-Paper-Scissors. Snake beats water, water beats gun, gun beats snake.

### How it works

The win logic is driven by a lookup dictionary instead of a chain of `if/elif` statements:

```python
beats = {1: -1, -1: 0, 0: 1}  # key beats value
```

Each entry encodes one rule (e.g. `1: -1` means snake beats water). A result is checked with a single lookup — `beats[computer] == you` — rather than six separate hand-written comparisons for every possible matchup.

### Features

- Input is validated in a loop — invalid entries re-prompt instead of crashing.
- Score (wins / losses / draws) is tracked across rounds and printed at the end.
- The game repeats until the player chooses not to play again.

### Usage

```bash
python3 snake_water_gun.py
```

**Example:**

```
Enter Your Choice (s/w/g): s

You chose snake
Computer chose gun
You lose!

Play again? (y/n): n

Final Score — Wins: 0, Losses: 1, Draws: 0
Thank you! Hope you enjoyed
```

### Requirements

Python 3, standard library only (`random`). No external dependencies.

---

## 3. Terminal Weather App 🌦️

A command-line tool that fetches real-time weather data for any city using the OpenWeatherMap API.

### How it works

The script communicates with an external REST API, parses the JSON response, and renders a stylized dashboard in the terminal.

- **API Integration:** Uses the `requests` library to pass parameters and handle network timeouts or bad status codes.
- **Environment Variables:** Keeps the private API key secure by loading it from a local `.env` file via `python-dotenv` instead of hardcoding it.
- **Rich UI:** Uses the `rich` library for colorful, formatted panels instead of plain prints.
- **CLI Arguments:** Uses `sys.argv` to allow passing the city directly on the command line, falling back to an `input()` prompt if omitted.

### Usage

```bash
python weather_app.py Tokyo
```

```bash
python weather_app.py
```

### Example

```text
$ python weather_app.py London

Fetching weather data for London...

╭────────────────── 🌍 Weather in London ──────────────────╮
│                                                            │
│ 🌡️  Temperature: 15.2°C (Feels like 14.5°C)               │
│ ☁️  Condition:   Overcast Clouds                          │
│ 💧 Humidity:    72%                                       │
│                                                            │
╰────────────────────────────────────────────────────────────╯
```

### Requirements

- Python 3.6+
- External dependencies: `requests`, `python-dotenv`, `rich`

Requires a free OpenWeatherMap API key saved in a local `.env` file:

```env
WEATHER_API_KEY=your_api_key_here
```

---

## 4. YouTube Video Downloader

A command-line tool that downloads a single YouTube video at the best available quality using `yt-dlp`.

### How it works

- **Best quality download:** uses `'bestvideo+bestaudio/best'` instead of a pre-merged `'best'` format, so it isn't capped at ~720p. Requires `ffmpeg` installed on your system to merge the separate video and audio streams.
- **Playlist rejection:** YouTube playlist links have a `list` parameter but no `v` (single video) parameter. This tool explicitly detects and rejects bare playlist URLs before attempting any download — yt-dlp's built-in `noplaylist` option only prevents downloading a playlist when a URL contains *both* a video and a playlist ID together, so it does not by itself stop a bare playlist link from downloading every item in the playlist.
- **URL validation:** rejects anything that isn't a recognizable `youtube.com` or `youtu.be` link before calling yt-dlp at all.
- **Error handling:** cleanly catches invalid URLs, unavailable videos, age-restricted videos requiring sign-in, and network failures, instead of crashing with a raw traceback.

### Usage

```bash
python YouTube_video_downloader.py
```

Downloaded files are saved into a `downloads/` folder (not tracked in this repo).

### Example

```
$ python YouTube_video_downloader.py

🎥 YouTube Video Downloader

Enter the YouTube Video URL: https://youtu.be/dQw4w9WgXcQ

⏳ Fetching video information and starting download...
[download] Destination: downloads/Rick Astley - Never Gonna Give You Up.mp4
[download] 100% of 62.43MiB in 00:01

✅ Download completed successfully!
```

### Requirements

- Python 3.6+
- External dependencies: `yt-dlp`, `rich`
- **`ffmpeg` must be installed separately** (not a pip package) — required to merge the best available video and audio streams. Install via your OS package manager (e.g. `choco install ffmpeg`, `brew install ffmpeg`, or `apt install ffmpeg`).

Install Python dependencies via:

```bash
pip install -r requirements.txt
```
