import os
import sys
import time
import re
import shutil
import json

# ─── Enable ANSI on Windows ───────────────────
os.system("")

# ─── COLORS ───────────────────────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
CYAN    = "\033[96m"
BLUE    = "\033[94m"
WHITE   = "\033[97m"
DIM     = "\033[2m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
MAGENTA = "\033[95m"
RED     = "\033[91m"
ORANGE  = "\033[38;5;208m"

# ─── CONFIG FILE (stores TeraBox API key) ─────
CONFIG_PATH = os.path.join(os.path.expanduser("~"), ".xdownder_config.json")

def load_config():
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def save_config(cfg):
    try:
        with open(CONFIG_PATH, "w") as f:
            json.dump(cfg, f, indent=2)
    except Exception as e:
        print(f"  {YELLOW}⚠  Could not save config: {e}{RESET}")

# ─── HELPERS ──────────────────────────────────
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def typewrite(text, delay=0.022, color=""):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def divider(char="═", color=CYAN, width=60):
    print(color + "  " + char * width + RESET)

def format_duration(seconds):
    if not seconds:
        return "N/A"
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h}:{m:02}:{s:02}" if h else f"{m}:{s:02}"

def format_filesize(size_bytes):
    if not size_bytes:
        return "N/A"
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} GB"

# ─── FFMPEG AUTO-DETECT ───────────────────────
def get_ffmpeg_path():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        pass
    return shutil.which("ffmpeg")

FFMPEG_PATH = get_ffmpeg_path()

# ─── SPLASH SCREEN ────────────────────────────
BANNER = [
    r" ██╗  ██╗██████╗  ██████╗ ██╗    ██╗███╗   ██╗██████╗ ███████╗██████╗ ",
    r" ╚██╗██╔╝██╔══██╗██╔═══██╗██║    ██║████╗  ██║██╔══██╗██╔════╝██╔══██╗",
    r"  ╚███╔╝ ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝",
    r"  ██╔██╗ ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗",
    r" ██╔╝ ██╗██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║██████╔╝███████╗██║  ██║",
    r" ╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝",
]

def splash():
    clear()
    print()
    divider("═", CYAN, 74)
    print()
    for line in BANNER:
        print(f"  {BOLD}{CYAN}{line}{RESET}")
        time.sleep(0.08)
    print()
    typewrite("            ⚡ MULTI-PLATFORM DOWNLOADER  ⚡", delay=0.018, color=YELLOW + BOLD)
    print()
    print(f"       {DIM}by{RESET}  {BOLD}{MAGENTA}Sudhirxd.in{RESET}  {DIM}│  v2.0  │  YouTube · Instagram · TikTok · TeraBox · and more{RESET}")
    print()
    divider("═", CYAN, 74)
    print()

    # System check
    print(f"  {CYAN}◈  SYSTEM CHECK{RESET}")
    time.sleep(0.3)
    print(f"  {DIM}┌{'─'*40}┐{RESET}")

    # Python check
    time.sleep(0.2)
    pyver = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"  {DIM}│{RESET}  {GREEN}✔{RESET}  Python     {WHITE}{pyver}{RESET:<20}{DIM}│{RESET}")

    # yt-dlp check
    time.sleep(0.2)
    try:
        import yt_dlp
        print(f"  {DIM}│{RESET}  {GREEN}✔{RESET}  yt-dlp     {WHITE}installed{RESET:<21}{DIM}│{RESET}")
    except ImportError:
        print(f"  {DIM}│{RESET}  {RED}✘{RESET}  yt-dlp     {RED}NOT FOUND{RESET:<21}{DIM}│{RESET}")

    # ffmpeg check
    time.sleep(0.2)
    if FFMPEG_PATH:
        print(f"  {DIM}│{RESET}  {GREEN}✔{RESET}  FFmpeg     {WHITE}detected{RESET:<22}{DIM}│{RESET}")
    else:
        print(f"  {DIM}│{RESET}  {YELLOW}⚠{RESET}  FFmpeg     {YELLOW}not found{RESET:<21}{DIM}│{RESET}")

    # requests check (for TeraBox)
    time.sleep(0.2)
    try:
        import requests
        print(f"  {DIM}│{RESET}  {GREEN}✔{RESET}  requests   {WHITE}installed{RESET:<21}{DIM}│{RESET}")
    except ImportError:
        print(f"  {DIM}│{RESET}  {YELLOW}⚠{RESET}  requests   {YELLOW}not found (TeraBox needs it){RESET:<7}{DIM}│{RESET}")

    # cookies.txt check
    time.sleep(0.2)
    _ck_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cookies.txt")
    if os.path.exists(_ck_path):
        print(f"  {DIM}│{RESET}  {GREEN}✔{RESET}  cookies    {WHITE}found ✓{RESET:<23}{DIM}│{RESET}")
    else:
        print(f"  {DIM}│{RESET}  {DIM}○{RESET}  cookies    {DIM}not found (optional){RESET:<21}{DIM}│{RESET}")

    print(f"  {DIM}└{'─'*40}┘{RESET}")
    print()

    if not FFMPEG_PATH:
        print(f"  {YELLOW}⚠  FFmpeg missing — MP3/M4A may not work{RESET}")
        print(f"  {DIM}  pip install imageio-ffmpeg  OR  https://ffmpeg.org{RESET}")
        print()

    divider("─", DIM, 74)
    print()

# ─── SPINNING LOADER ──────────────────────────
def spinner(message, duration=0.0, stop_event=None):
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    i = 0
    if stop_event:
        while not stop_event.is_set():
            sys.stdout.write(f"\r  {CYAN}{frames[i % len(frames)]}{RESET}  {WHITE}{message}{RESET}   ")
            sys.stdout.flush()
            time.sleep(0.08)
            i += 1
        sys.stdout.write(f"\r  {GREEN}✔{RESET}  {WHITE}{message}{RESET}   \n")
        sys.stdout.flush()

# ─── ANIMATED DOWNLOAD BAR (TeraBox) ──────────
def fake_progress_bar(label="Downloading", total_steps=50, color=CYAN):
    """Animated progress bar for TeraBox (no real byte progress from API)."""
    bar_len = 40
    print()
    for i in range(total_steps + 1):
        percent = (i / total_steps) * 100
        filled  = int(bar_len * i / total_steps)
        bar     = color + "█" * filled + DIM + "░" * (bar_len - filled) + RESET
        sys.stdout.write(
            f"\r  {bar}  {BOLD}{WHITE}{percent:5.1f}%{RESET}"
            f"  {MAGENTA}{label}{RESET}   "
        )
        sys.stdout.flush()
        time.sleep(0.04)
    print()

# ─── MODE SELECTOR ────────────────────────────
def choose_mode():
    print(f"  {BOLD}{CYAN}╔══ SELECT DOWNLOADER MODE ══════════════════════════════╗{RESET}")
    print(f"  {BOLD}{CYAN}║                                                        ║{RESET}")
    print(f"  {BOLD}{CYAN}║  {GREEN}[1]{CYAN}  🌐  All Social Media Downloader                   ║{RESET}")
    print(f"  {BOLD}{CYAN}║      {DIM}YouTube · Instagram · TikTok · Twitter & more{CYAN}      ║{RESET}")
    print(f"  {BOLD}{CYAN}║                                                        ║{RESET}")
    print(f"  {BOLD}{CYAN}║  {ORANGE}[2]{CYAN}  📦  TeraBox Downloader                            ║{RESET}")
    print(f"  {BOLD}{CYAN}║      {DIM}Direct download from TeraBox / 1024tera links{CYAN}       ║{RESET}")
    print(f"  {BOLD}{CYAN}║                                                        ║{RESET}")
    print(f"  {BOLD}{CYAN}╚════════════════════════════════════════════════════════╝{RESET}")
    print()

    while True:
        try:
            choice = input(f"  {CYAN}➜  {BOLD}Choose mode [{WHITE}1{CYAN}/{WHITE}2{CYAN}]{RESET}{CYAN}: {RESET}{WHITE}").strip()
            print(RESET, end="")
            if choice == "1":
                return "social"
            elif choice == "2":
                return "terabox"
            else:
                print(f"  {YELLOW}⚠  Please enter 1 or 2.{RESET}")
        except KeyboardInterrupt:
            return None

# ═══════════════════════════════════════════════
# ─── SOCIAL MEDIA DOWNLOADER (unchanged v1) ───
# ═══════════════════════════════════════════════

COOKIES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cookies.txt")

def get_cookies_opt():
    """Return yt-dlp cookiefile option if cookies.txt exists next to the script."""
    if os.path.exists(COOKIES_PATH):
        return COOKIES_PATH
    return None

# ─── PROGRESS HOOK ────────────────────────────
def make_progress_hook(fmt, quality):
    def hook(d):
        if d['status'] == 'downloading':
            total      = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
            downloaded = d.get('downloaded_bytes', 0)
            percent    = round(downloaded / total * 100, 1) if total else 0
            speed      = (d.get('_speed_str') or 'N/A').strip()
            eta        = (d.get('_eta_str')   or 'N/A').strip()
            dl         = (d.get('_downloaded_bytes_str') or '').strip()
            tot        = (d.get('_total_bytes_str')      or '').strip()

            bar_len = 40
            filled  = int(bar_len * percent / 100)
            bar     = (CYAN + "█" * filled + DIM + "░" * (bar_len - filled) + RESET)

            label = f"{fmt.upper()}"
            if quality and fmt not in ('mp3','m4a'):
                label += f" {quality}p"

            sys.stdout.write(
                f"\r  {bar}  {BOLD}{WHITE}{percent:5.1f}%{RESET}"
                f"  {GREEN}{speed:>10}{RESET}"
                f"  ETA {YELLOW}{eta:<6}{RESET}"
                f"  {DIM}{dl:>8}/{tot:<8}{RESET}"
                f"  {MAGENTA}{label}{RESET}   "
            )
            sys.stdout.flush()

        elif d['status'] == 'finished':
            bar = GREEN + "█" * 40 + RESET
            sys.stdout.write(
                f"\r  {bar}  {BOLD}{GREEN}100.0%{RESET}"
                f"  {GREEN}Merging / Finalizing...{RESET}                    \n"
            )
            sys.stdout.flush()
    return hook

# ─── VIDEO INFO ───────────────────────────────
def get_info(url):
    import yt_dlp
    import threading

    result = [None]
    error  = [None]
    stop   = threading.Event()

    def fetch():
        try:
            opts = {'quiet': True, 'no_warnings': True}
            ck = get_cookies_opt()
            if ck:
                opts['cookiefile'] = ck
            with yt_dlp.YoutubeDL(opts) as ydl:
                result[0] = ydl.extract_info(url, download=False)
        except Exception as e:
            error[0] = str(e)
        finally:
            stop.set()

    t = threading.Thread(target=fetch, daemon=True)
    t.start()
    spinner("Fetching video info...", stop_event=stop)
    t.join()

    if error[0]:
        err = error[0]
        if "Private" in err or "private" in err:
            print(f"  {RED}✘  This video is private.{RESET}\n")
        elif "unavailable" in err.lower():
            print(f"  {RED}✘  Video unavailable or removed.{RESET}\n")
        elif "region" in err.lower():
            print(f"  {RED}✘  This video is region-blocked.{RESET}\n")
        else:
            print(f"  {RED}✘  {err}{RESET}\n")
        return None

    return result[0]

def show_info(info):
    print()
    divider("─", CYAN, 74)
    print(f"  {BOLD}{WHITE}  {info.get('title','Unknown')}{RESET}")
    divider("─", DIM, 74)
    print(f"  {CYAN}  Uploader  {RESET}{WHITE}{info.get('uploader','N/A')}{RESET}")
    print(f"  {CYAN}  Duration  {RESET}{WHITE}{format_duration(info.get('duration'))}{RESET}")
    print(f"  {CYAN}  Views     {RESET}{WHITE}{info.get('view_count',0):,}{RESET}")
    print(f"  {CYAN}  Platform  {RESET}{WHITE}{info.get('extractor_key','N/A')}{RESET}")
    divider("─", CYAN, 74)

# ─── FORMAT MENU ──────────────────────────────
def choose_format(info):
    height_sizes = {}
    for f in info.get('formats', []):
        h = f.get('height')
        if h and f.get('vcodec', 'none') != 'none':
            fs = f.get('filesize') or f.get('filesize_approx') or 0
            if h not in height_sizes or fs > height_sizes[h]:
                height_sizes[h] = fs

    heights = sorted(height_sizes.keys(), reverse=True)

    options = []
    idx = 1

    print(f"\n  {BOLD}{CYAN}  ╔══ AVAILABLE FORMATS ══════════════════════════════╗{RESET}")
    print(f"  {BOLD}{CYAN}  ║                                                    ║{RESET}")
    print(f"  {BOLD}{CYAN}  ║  {YELLOW}▶  VIDEO + AUDIO{CYAN}                                  ║{RESET}")
    print(f"  {BOLD}{CYAN}  ║{'─'*52}║{RESET}")

    for h in heights:
        size_str = format_filesize(height_sizes[h]) if height_sizes[h] else "~size varies"
        for ext in ['mp4', 'mkv', 'webm']:
            color = WHITE if ext == 'mp4' else DIM
            tag   = f"{GREEN}★ {RESET}" if ext == 'mp4' else "  "
            print(
                f"  {CYAN}  ║{RESET}  {CYAN}[{idx:2}]{RESET}  {tag}{color}{h}p  {ext.upper():<5}{RESET}"
                f"  {DIM}Video+Audio  ~{size_str:<10}{RESET}  {CYAN}║{RESET}"
            )
            options.append({'type': 'video', 'format': ext, 'quality': str(h), 'size': height_sizes[h]})
            idx += 1

    print(f"  {BOLD}{CYAN}  ║{'─'*52}║{RESET}")
    print(f"  {BOLD}{CYAN}  ║  {MAGENTA}♪  AUDIO ONLY{CYAN}                                     ║{RESET}")
    print(f"  {BOLD}{CYAN}  ║{'─'*52}║{RESET}")

    print(f"  {CYAN}  ║{RESET}  {CYAN}[{idx:2}]{RESET}  {MAGENTA}MP3   192kbps  Audio Only{RESET}                  {CYAN}║{RESET}")
    options.append({'type': 'audio', 'format': 'mp3', 'quality': '192', 'size': 0})
    idx += 1

    print(f"  {CYAN}  ║{RESET}  {CYAN}[{idx:2}]{RESET}  {MAGENTA}M4A   Best     Audio Only{RESET}                  {CYAN}║{RESET}")
    options.append({'type': 'audio', 'format': 'm4a', 'quality': 'best', 'size': 0})
    idx += 1

    print(f"  {BOLD}{CYAN}  ║                                                    ║{RESET}")
    print(f"  {BOLD}{CYAN}  ╚════════════════════════════════════════════════════╝{RESET}")
    print(f"  {DIM}  {GREEN}★{RESET}{DIM} = Recommended format{RESET}")
    print()

    while True:
        try:
            choice = input(f"  {CYAN}➜  {BOLD}Choose format [{WHITE}1{CYAN}-{WHITE}{idx-1}{CYAN}]{RESET}{CYAN}: {RESET}{WHITE}").strip()
            print(RESET, end="")
            n = int(choice)
            if 1 <= n <= len(options):
                return options[n - 1]
            print(f"  {YELLOW}⚠  Enter a number between 1 and {len(options)}{RESET}")
        except ValueError:
            print(f"  {YELLOW}⚠  Please enter a valid number.{RESET}")
        except KeyboardInterrupt:
            return None

# ─── DOWNLOAD (Social) ────────────────────────
def do_download(url, chosen):
    import yt_dlp

    fmt     = chosen['format']
    quality = chosen['quality']

    DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Downloads", "XDOWNDER")
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    print()
    divider("─", CYAN, 74)
    print(f"  {BOLD}{GREEN}  ⬇  DOWNLOADING{RESET}")
    print(f"  {DIM}  Format   : {fmt.upper()}{RESET}")
    if fmt not in ('mp3', 'm4a'):
        print(f"  {DIM}  Quality  : {quality}p{RESET}")
    print(f"  {DIM}  Save to  : {DOWNLOAD_DIR}{RESET}")

    ck = get_cookies_opt()
    if ck:
        print(f"  {GREEN}  🍪  cookies.txt detected — using for auth{RESET}")
    else:
        print(f"  {DIM}  💡  Tip: place cookies.txt next to script for age-restricted/private videos{RESET}")
    divider("─", DIM, 74)
    print()

    saved_file = [None]

    def post_hook(d):
        if d['status'] == 'finished':
            saved_file[0] = d.get('filename')

    cookie_opt = {'cookiefile': ck} if ck else {}

    if fmt in ('mp3', 'm4a'):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title).100s.%(ext)s'),
            'restrictfilenames': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': fmt,
                'preferredquality': '192',
            }],
            'progress_hooks': [make_progress_hook(fmt, None), post_hook],
            'quiet': True,
            'ffmpeg_location': FFMPEG_PATH,
            **cookie_opt,
        }
    else:
        # Format string with proper fallbacks:
        # 1. Best video <= quality + best audio (merged)
        # 2. Best video <= quality (no separate audio)
        # 3. Best single format <= quality
        # 4. Absolute best available (last resort)
        fmt_str = (
            f'bestvideo[height<={quality}][ext={fmt}]+bestaudio/best'
            f'/bestvideo[height<={quality}]+bestaudio/best'
            f'/best[height<={quality}]'
            f'/best'
        )
        ydl_opts = {
            'format': fmt_str,
            'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title).100s.%(ext)s'),
            'restrictfilenames': True,
            'merge_output_format': fmt,
            'progress_hooks': [make_progress_hook(fmt, quality), post_hook],
            'quiet': True,
            'noplaylist': True,
            'ffmpeg_location': FFMPEG_PATH,
            **cookie_opt,
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        actual_file = None
        if saved_file[0]:
            base = os.path.splitext(saved_file[0])[0]
            for ext in [fmt, 'mp4', 'mkv', 'webm', 'mp3', 'm4a']:
                candidate = f"{base}.{ext}"
                if os.path.exists(candidate):
                    actual_file = candidate
                    break
        if not actual_file:
            files = [os.path.join(DOWNLOAD_DIR, f) for f in os.listdir(DOWNLOAD_DIR)]
            if files:
                actual_file = max(files, key=os.path.getmtime)

        print()
        divider("═", GREEN, 74)
        print(f"  {BOLD}{GREEN}  ✔  DOWNLOAD COMPLETE!{RESET}")
        divider("─", DIM, 74)

        if actual_file and os.path.exists(actual_file):
            size_bytes = os.path.getsize(actual_file)
            filename   = os.path.basename(actual_file)
            ext        = os.path.splitext(actual_file)[1].lstrip('.').upper()
            print(f"  {CYAN}  File Name  {RESET}{WHITE}{filename}{RESET}")
            print(f"  {CYAN}  Format     {RESET}{WHITE}{ext}{RESET}")
            if fmt not in ('mp3', 'm4a'):
                print(f"  {CYAN}  Quality    {RESET}{WHITE}{quality}p{RESET}")
            print(f"  {CYAN}  File Size  {RESET}{WHITE}{format_filesize(size_bytes)}{RESET}")
            print(f"  {CYAN}  Full Path  {RESET}{WHITE}{os.path.abspath(actual_file)}{RESET}")
        else:
            print(f"  {CYAN}  Saved to   {RESET}{WHITE}{DOWNLOAD_DIR}{RESET}")

        divider("═", GREEN, 74)
        print()

    except Exception as e:
        print(f"\n  {RED}✘  Download failed: {e}{RESET}\n")

# ─── SOCIAL MEDIA LOOP ────────────────────────
def social_media_loop():
    while True:
        try:
            print(f"  {BOLD}{CYAN}╔══ PASTE YOUR LINK BELOW ═══════════════════════════════╗{RESET}")
            print(f"  {BOLD}{CYAN}║{RESET}  {DIM}Supports: YouTube, Instagram, TikTok, Twitter & more{RESET}  {CYAN}║{RESET}")
            print(f"  {BOLD}{CYAN}╚════════════════════════════════════════════════════════╝{RESET}")
            print(f"  {DIM}  Commands: 'help'  |  'clear'  |  'back'  |  'exit'{RESET}")
            print()
            url = input(f"  {BOLD}{CYAN}➜  URL : {RESET}{BOLD}{WHITE}").strip()
            print(RESET, end="")

            if not url:
                print()
                continue

            if url.lower() in ('exit', 'quit', 'q'):
                return 'exit'

            if url.lower() == 'back':
                return 'back'

            if url.lower() == 'help':
                print(f"\n  {CYAN}{BOLD}  HELP{RESET}")
                divider("─", DIM, 74)
                print(f"  {WHITE}  Paste any URL{RESET}   {DIM}→ fetch info & pick format{RESET}")
                print(f"  {WHITE}  back         {RESET}   {DIM}→ go back to mode selector{RESET}")
                print(f"  {WHITE}  clear        {RESET}   {DIM}→ clear the screen{RESET}")
                print(f"  {WHITE}  exit/quit/q  {RESET}   {DIM}→ close XDOWNDER{RESET}")
                divider("─", DIM, 74)
                print()
                continue

            if url.lower() == 'clear':
                clear()
                splash()
                continue

            info = get_info(url)
            if not info:
                continue

            show_info(info)

            chosen = choose_format(info)
            if not chosen:
                print(f"  {YELLOW}Cancelled.{RESET}\n")
                continue

            do_download(url, chosen)
            print()

        except KeyboardInterrupt:
            print(f"\n\n  {YELLOW}Returning to main menu...{RESET}\n")
            return 'back'


# ═══════════════════════════════════════════════
# ─── TERABOX DOWNLOADER ───────────────────────
# ═══════════════════════════════════════════════

TERABOX_API_URL  = "https://xapiverse.com/api/terabox"

def terabox_splash():
    print()
    divider("═", ORANGE, 74)
    print(f"  {BOLD}{ORANGE}  📦  TERABOX DOWNLOADER{RESET}")
    print(f"  {DIM}  Powered by xAPIverse — xapiverse.com{RESET}")
    divider("═", ORANGE, 74)
    print()

def get_or_ask_api_key(cfg):
    """Return saved API key or prompt user once, then save it."""
    if cfg.get("terabox_api_key"):
        print(f"  {GREEN}✔{RESET}  {DIM}API key loaded from saved config.{RESET}")
        print(f"  {DIM}  (type 'resetkey' to use a different key){RESET}")
        print()
        return cfg["terabox_api_key"]

    print(f"  {CYAN}◈  xAPIverse Key Required{RESET}")
    print(f"  {DIM}  Get yours at: https://xapiverse.com{RESET}")
    print(f"  {DIM}  API: POST https://xapiverse.com/api/terabox-pro{RESET}")
    print()
    while True:
        try:
            key = input(f"  {BOLD}{ORANGE}➜  Paste API Key : {RESET}{WHITE}").strip()
            print(RESET, end="")
            if key:
                cfg["terabox_api_key"] = key
                save_config(cfg)
                print(f"  {GREEN}✔{RESET}  API key saved locally.\n")
                return key
            print(f"  {YELLOW}⚠  API key cannot be empty.{RESET}")
        except KeyboardInterrupt:
            return None

def terabox_resolve(url, api_key):
    """Call the xAPIverse TeraBox API and return parsed result."""
    try:
        import requests
    except ImportError:
        print(f"  {RED}✘  'requests' library not found.{RESET}")
        print(f"  {DIM}  Run: pip install requests{RESET}\n")
        return None

    import threading

    result = [None]
    error  = [None]
    stop   = threading.Event()

    def fetch():
        try:
            resp = requests.post(
                TERABOX_API_URL,
                headers={
                    "Content-Type": "application/json",
                    "xAPIverse-Key": api_key,
                },
                json={"url": url},
                timeout=30,
            )
            if resp.status_code == 200:
                result[0] = resp.json()
            elif resp.status_code == 401:
                error[0] = "Invalid API key — please check your xAPIverse key."
            elif resp.status_code == 403:
                error[0] = "Access forbidden — check your xAPIverse plan or credits."
            elif resp.status_code == 429:
                error[0] = "Rate limit exceeded — please wait before trying again."
            else:
                error[0] = f"API error {resp.status_code}: {resp.text[:200]}"
        except Exception as e:
            error[0] = str(e)
        finally:
            stop.set()

    t = threading.Thread(target=fetch, daemon=True)
    t.start()
    spinner("Resolving TeraBox link...", stop_event=stop)
    t.join()

    if error[0]:
        print(f"  {RED}✘  {error[0]}{RESET}\n")
        return None

    return result[0]

def show_terabox_info(data):
    """Display info about resolved TeraBox file(s) and API credits."""
    print()
    divider("─", ORANGE, 74)

    # Parse response — API returns {"status":"success","total_files":N,"list":[...],"free_credits_remaining":"98/100"}
    files = []
    if isinstance(data, dict):
        if data.get("status") == "success" or "list" in data:
            files = data.get("list", [])
        elif "data" in data:
            raw = data["data"]
            files = raw if isinstance(raw, list) else [raw]
        else:
            files = [data]
    elif isinstance(data, list):
        files = data

    if not files:
        print(f"  {RED}✘  No files found in response.{RESET}\n")
        return None

    total = data.get("total_files", len(files)) if isinstance(data, dict) else len(files)
    print(f"  {BOLD}{ORANGE}  📦  FILES FOUND: {total}{RESET}")

    # ── Credits display ──────────────────────────
    if isinstance(data, dict):
        credits_left = data.get("free_credits_remaining", "")
        used_free    = data.get("used_free_credit", False)
        if credits_left:
            credit_color = GREEN if not used_free else YELLOW
            credit_tag   = f"  {DIM}[free]{RESET}" if used_free else ""
            print(f"  {credit_color}  💳  Credits remaining: {BOLD}{credits_left}{RESET}{credit_tag}")
    divider("─", DIM, 74)

    for i, f in enumerate(files, 1):
        name      = f.get("name", "Unknown")
        size_fmt  = f.get("size_formatted", "")
        duration  = f.get("duration", "")
        quality   = f.get("quality", "")
        ftype     = f.get("type", "")
        is_dir    = f.get("is_dir", "0")

        icon = "📁" if is_dir == "1" else ("🎬" if ftype == "video" else "📄")

        print(f"  {ORANGE}  [{i}]{RESET}  {icon}  {BOLD}{WHITE}{name}{RESET}")

        meta = []
        if size_fmt:   meta.append(f"Size: {size_fmt}")
        if duration:   meta.append(f"Duration: {duration}")
        if quality:    meta.append(f"Quality: {quality}")
        if ftype:      meta.append(f"Type: {ftype}")

        if meta:
            print(f"        {DIM}" + "  │  ".join(meta) + f"{RESET}")

        # Show stream options if video
        streams = f.get("fast_stream_url", {})
        if streams:
            available = list(streams.keys())
            print(f"        {DIM}Streams: {', '.join(available)}{RESET}")

        print()

    divider("─", ORANGE, 74)
    print()
    return files

def terabox_pick_download_option(file_info):
    """
    Let user pick how to download: direct file or a stream quality.
    Returns (url, label) tuple.
    """
    name     = file_info.get("name", "file")
    ftype    = file_info.get("type", "")
    streams  = file_info.get("fast_stream_url", {})
    dlink    = file_info.get("normal_dlink", "")
    zip_link = file_info.get("zip_dlink", "")

    options = []
    idx = 1

    print(f"  {BOLD}{ORANGE}╔══ DOWNLOAD OPTIONS ════════════════════════════════════╗{RESET}")
    print(f"  {BOLD}{ORANGE}║                                                        ║{RESET}")

    # Direct download
    if dlink:
        quality = file_info.get("quality", "")
        size_fmt = file_info.get("size_formatted", "")
        label = f"Direct Download"
        if quality: label += f"  ({quality})"
        if size_fmt: label += f"  {size_fmt}"
        print(f"  {ORANGE}║{RESET}  {CYAN}[{idx}]{RESET}  {GREEN}★{RESET}  {WHITE}{label}{RESET}  {DIM}(recommended){RESET}  {ORANGE}║{RESET}")
        options.append(("direct", dlink, f"Direct {quality or 'original'}"))
        idx += 1

    # Stream quality options
    if streams:
        print(f"  {ORANGE}║{'─'*56}║{RESET}")
        print(f"  {ORANGE}║{RESET}  {MAGENTA}🎬  STREAM (save as .mp4){RESET}                            {ORANGE}║{RESET}")
        for res in ["1080p", "720p", "480p", "360p"]:
            if res in streams:
                print(f"  {ORANGE}║{RESET}  {CYAN}[{idx}]{RESET}     {WHITE}Stream {res}{RESET}                                    {ORANGE}║{RESET}")
                options.append(("stream", streams[res], f"Stream {res}"))
                idx += 1

    # ZIP download
    if zip_link:
        print(f"  {ORANGE}║{'─'*56}║{RESET}")
        print(f"  {ORANGE}║{RESET}  {CYAN}[{idx}]{RESET}  📦  {DIM}Download as ZIP{RESET}                                {ORANGE}║{RESET}")
        options.append(("zip", zip_link, "ZIP archive"))
        idx += 1

    print(f"  {BOLD}{ORANGE}║                                                        ║{RESET}")
    print(f"  {BOLD}{ORANGE}╚════════════════════════════════════════════════════════╝{RESET}")
    print()

    while True:
        try:
            choice = input(f"  {BOLD}{ORANGE}➜  Choose [{WHITE}1{ORANGE}-{WHITE}{idx-1}{ORANGE}]{RESET}{ORANGE}: {RESET}{WHITE}").strip()
            print(RESET, end="")
            n = int(choice)
            if 1 <= n <= len(options):
                return options[n - 1]
            print(f"  {YELLOW}⚠  Enter a number between 1 and {len(options)}{RESET}")
        except ValueError:
            print(f"  {YELLOW}⚠  Please enter a valid number.{RESET}")
        except KeyboardInterrupt:
            return None


def terabox_download_file(file_info, idx, total):
    """Download a single TeraBox file — shows option picker first."""
    try:
        import requests
    except ImportError:
        print(f"  {RED}✘  'requests' library not installed.{RESET}\n")
        return

    # Pick download option
    option = terabox_pick_download_option(file_info)
    if not option:
        print(f"  {YELLOW}  Cancelled.{RESET}\n")
        return

    opt_type, url, label = option

    # Build output filename
    base_name = file_info.get("name", f"terabox_file_{idx}")
    safe_name = re.sub(r'[\\/*?:"<>|]', "_", base_name)

    # For streams (.m3u8), save as .mp4 with resolution in name
    if opt_type == "stream":
        res = label.split()[-1]  # e.g. "1080p"
        name_no_ext, _ = os.path.splitext(safe_name)
        safe_name = f"{name_no_ext}_{res}.mp4"
    elif opt_type == "zip":
        safe_name = safe_name + ".zip"

    DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Downloads", "XDOWNDER", "TeraBox")
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    out_path = os.path.join(DOWNLOAD_DIR, safe_name)

    print()
    divider("─", ORANGE, 74)
    print(f"  {BOLD}{GREEN}  ⬇  DOWNLOADING  [{idx}/{total}]{RESET}")
    print(f"  {DIM}  Option   : {label}{RESET}")
    print(f"  {DIM}  File     : {safe_name}{RESET}")
    print(f"  {DIM}  Save to  : {DOWNLOAD_DIR}{RESET}")
    divider("─", DIM, 74)

    # ── HLS stream via ffmpeg ──────────────────
    if opt_type == "stream":
        if not FFMPEG_PATH:
            print(f"  {RED}✘  FFmpeg not found — needed for stream download.{RESET}")
            print(f"  {DIM}  pip install imageio-ffmpeg  OR  https://ffmpeg.org{RESET}\n")
            return
        import subprocess
        print()
        print(f"  {CYAN}  Using FFmpeg to download HLS stream...{RESET}")
        print(f"  {DIM}  (Progress shown by FFmpeg){RESET}\n")
        try:
            subprocess.run([
                FFMPEG_PATH, "-y",
                "-i", url,
                "-c", "copy",
                out_path
            ], check=True)

            print()
            divider("═", GREEN, 74)
            print(f"  {BOLD}{GREEN}  ✔  STREAM DOWNLOAD COMPLETE!{RESET}")
            divider("─", DIM, 74)
            if os.path.exists(out_path):
                print(f"  {ORANGE}  File Name  {RESET}{WHITE}{safe_name}{RESET}")
                print(f"  {ORANGE}  Quality    {RESET}{WHITE}{label}{RESET}")
                print(f"  {ORANGE}  File Size  {RESET}{WHITE}{format_filesize(os.path.getsize(out_path))}{RESET}")
                print(f"  {ORANGE}  Full Path  {RESET}{WHITE}{os.path.abspath(out_path)}{RESET}")
            divider("═", GREEN, 74)
            print()
        except subprocess.CalledProcessError as e:
            print(f"\n  {RED}✘  FFmpeg failed: {e}{RESET}\n")
        return

    # ── Direct / ZIP HTTP download ─────────────
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        }
        resp = requests.get(url, headers=headers, stream=True, timeout=60)
        resp.raise_for_status()

        total_size = int(resp.headers.get("content-length", 0))
        bar_len    = 40
        downloaded = 0
        start_time = time.time()

        print()
        with open(out_path, "wb") as fh:
            for chunk in resp.iter_content(chunk_size=65536):
                if chunk:
                    fh.write(chunk)
                    downloaded += len(chunk)

                    elapsed   = time.time() - start_time
                    speed     = downloaded / elapsed if elapsed > 0 else 0
                    percent   = (downloaded / total_size * 100) if total_size else 0
                    eta_s     = int((total_size - downloaded) / speed) if speed > 0 and total_size else 0
                    eta_str   = f"{eta_s}s" if eta_s < 60 else f"{eta_s//60}m{eta_s%60:02}s"
                    filled    = int(bar_len * percent / 100) if total_size else 0
                    bar       = ORANGE + "█" * filled + DIM + "░" * (bar_len - filled) + RESET
                    speed_str = format_filesize(speed) + "/s"
                    dl_str    = format_filesize(downloaded)
                    tot_str   = format_filesize(total_size) if total_size else "?"

                    sys.stdout.write(
                        f"\r  {bar}  {BOLD}{WHITE}{percent:5.1f}%{RESET}"
                        f"  {GREEN}{speed_str:>12}{RESET}"
                        f"  ETA {YELLOW}{eta_str:<6}{RESET}"
                        f"  {DIM}{dl_str:>8}/{tot_str:<8}{RESET}   "
                    )
                    sys.stdout.flush()

        bar = GREEN + "█" * bar_len + RESET
        sys.stdout.write(
            f"\r  {bar}  {BOLD}{GREEN}100.0%{RESET}"
            f"  {GREEN}Complete!{RESET}                                    \n"
        )
        sys.stdout.flush()

        final_size = os.path.getsize(out_path)
        print()
        divider("═", GREEN, 74)
        print(f"  {BOLD}{GREEN}  ✔  DOWNLOAD COMPLETE!{RESET}")
        divider("─", DIM, 74)
        print(f"  {ORANGE}  File Name  {RESET}{WHITE}{safe_name}{RESET}")
        print(f"  {ORANGE}  Option     {RESET}{WHITE}{label}{RESET}")
        print(f"  {ORANGE}  File Size  {RESET}{WHITE}{format_filesize(final_size)}{RESET}")
        print(f"  {ORANGE}  Duration   {RESET}{WHITE}{file_info.get('duration', 'N/A')}{RESET}")
        print(f"  {ORANGE}  Full Path  {RESET}{WHITE}{os.path.abspath(out_path)}{RESET}")
        divider("═", GREEN, 74)
        print()

    except Exception as e:
        print(f"\n  {RED}✘  Download failed: {e}{RESET}\n")

def terabox_loop(cfg):
    terabox_splash()
    api_key = get_or_ask_api_key(cfg)
    if not api_key:
        return 'back'

    while True:
        try:
            print(f"  {BOLD}{ORANGE}╔══ TERABOX — PASTE YOUR LINK ══════════════════════════╗{RESET}")
            print(f"  {BOLD}{ORANGE}║{RESET}  {DIM}Supports: terabox.com · 1024tera.com · freeterabox.com{RESET}  {ORANGE}║{RESET}")
            print(f"  {BOLD}{ORANGE}╚════════════════════════════════════════════════════════╝{RESET}")
            print(f"  {DIM}  Commands: 'resetkey'  |  'back'  |  'exit'{RESET}")
            print()

            url = input(f"  {BOLD}{ORANGE}➜  URL : {RESET}{BOLD}{WHITE}").strip()
            print(RESET, end="")

            if not url:
                print()
                continue

            if url.lower() in ('exit', 'quit', 'q'):
                return 'exit'

            if url.lower() == 'back':
                return 'back'

            if url.lower() == 'resetkey':
                cfg["terabox_api_key"] = ""
                save_config(cfg)
                print(f"  {YELLOW}✔  API key cleared.{RESET}\n")
                api_key = get_or_ask_api_key(cfg)
                if not api_key:
                    return 'back'
                continue

            # Resolve the TeraBox link
            data = terabox_resolve(url, api_key)
            if not data:
                continue

            files = show_terabox_info(data)
            if not files:
                continue

            # If multiple files, let user pick or download all
            if len(files) == 1:
                terabox_download_file(files[0], 1, 1)
            else:
                print(f"  {ORANGE}  [A]{RESET}  Download ALL files")
                print(f"  {DIM}  Or enter file number to download one{RESET}")
                print()
                choice = input(f"  {BOLD}{ORANGE}➜  Choice [A or number]: {RESET}{WHITE}").strip().lower()
                print(RESET, end="")

                if choice == 'a':
                    for i, f in enumerate(files, 1):
                        terabox_download_file(f, i, len(files))
                else:
                    try:
                        n = int(choice)
                        if 1 <= n <= len(files):
                            terabox_download_file(files[n-1], n, len(files))
                        else:
                            print(f"  {YELLOW}⚠  Invalid choice.{RESET}\n")
                    except ValueError:
                        print(f"  {YELLOW}⚠  Please enter a number or 'A'.{RESET}\n")

            print()

        except KeyboardInterrupt:
            print(f"\n\n  {YELLOW}Returning to main menu...{RESET}\n")
            return 'back'


# ═══════════════════════════════════════════════
# ─── MAIN LOOP ────────────────────────────────
# ═══════════════════════════════════════════════

def main():
    cfg = load_config()
    splash()

    while True:
        try:
            mode = choose_mode()

            if mode is None:
                # Ctrl+C at mode selector
                break

            if mode == 'social':
                result = social_media_loop()
            elif mode == 'terabox':
                result = terabox_loop(cfg)

            if result == 'exit':
                break
            # 'back' → loop back to mode selector

            print()

        except KeyboardInterrupt:
            break

    print()
    divider("═", CYAN, 74)
    typewrite("       Thanks for using XDOWNDER  —  by Sudhirxd.in  ⚡", delay=0.018, color=YELLOW + BOLD)
    divider("═", CYAN, 74)
    print()

if __name__ == "__main__":
    main()
