# ⚡ XDOWNDER — Multi-Platform Downloader

> Download videos, audio, and TeraBox files from the terminal — fast, clean, one click.
> 
> **by [Sudhirxd.in](https://sudhirxd.in)**

---

## 📦 Supported Platforms

| Mode | Platforms |
|------|-----------|
| 🌐 Social Media | YouTube, Instagram, TikTok, Twitter, Facebook & 1000+ more |
| 📦 TeraBox | terabox.com · 1024tera.com · freeterabox.com |

---

## 🚀 Quick Start

### 1. Install Python
Download from [python.org](https://python.org) — **Python 3.8+** required.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Tool

**Double-click** → `xdownder.bat`

Or via terminal:
```bash
python xdownder.py
```

---

## 📁 Folder Structure

```
📁 Your Folder
├── xdownder.py        ← Main script
├── xdownder.bat       ← One-click launcher (Windows)
├── requirements.txt   ← Dependencies
└── cookies.txt        ← (Optional) for age-restricted videos
```

---

## 🍪 cookies.txt (Optional)

Place a `cookies.txt` file in the **same folder** as the script.
This allows downloading **age-restricted** or **private** videos from YouTube.

To export cookies:
- Use the browser extension **"Get cookies.txt LOCALLY"** (Chrome/Firefox)
- Export from YouTube while logged in
- Save as `cookies.txt` next to `xdownder.py`

---

## 📥 Download Formats

### 🌐 Social Media Mode
- **Video:** MP4, MKV, WEBM (up to 4K)
- **Audio:** MP3 (192kbps), M4A (best quality)

### 📦 TeraBox Mode
- **Direct Download** — original file quality
- **Stream:** 1080p, 720p, 480p, 360p (MP4 via FFmpeg)
- **ZIP** — for folders/multiple files

---

## 🔑 TeraBox API Key

For TeraBox API Key
Dm here:- www.instagram.com/sudhirxd.in

---

## 📂 Downloaded Files Location

All files are saved to:
```
C:\Users\<YourName>\Downloads\XDOWNDER\
```
| Type | Subfolder |
|------|-----------|
| Social Media | `XDOWNDER\` |
| TeraBox | `XDOWNDER\TeraBox\` |

---

## ⌨️ Commands

| Command | Action |
|---------|--------|
| `back` | Return to mode selector |
| `clear` | Clear the screen |
| `help` | Show help (Social mode) |
| `resetkey` | Change TeraBox API key |
| `exit` / `q` | Quit the app |

---

## ⚙️ FFmpeg

FFmpeg is needed for:
- MP3 / M4A audio extraction
- TeraBox HLS stream downloads

**Auto-install via pip (recommended):**
```bash
pip install imageio-ffmpeg
```

Or download manually from [ffmpeg.org](https://ffmpeg.org).

---

## 🛠️ Requirements

| Package | Purpose |
|---------|---------|
| `yt-dlp` | Social media downloading |
| `requests` | TeraBox API calls + direct downloads |
| `imageio-ffmpeg` | Auto-bundled FFmpeg (MP3/stream support) |

---

## ❓ Troubleshooting

| Problem | Fix |
|---------|-----|
| `python` not recognized | Install Python & add to PATH |
| `yt-dlp not found` | Run `pip install yt-dlp` |
| FFmpeg missing warning | Run `pip install imageio-ffmpeg` |
| TeraBox API error 401 | Check your xAPIverse API key |
| Age-restricted video fails | Add `cookies.txt` next to script |

---

*Made with ❤️ by Sudhirxd.in*
