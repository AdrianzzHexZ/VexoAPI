from lib.ui import clear, title, section, info
from config import AUTHOR, VEXO_API_KEY
import subprocess
import sys
from pathlib import Path

TOOLS = [
    ("1", "AI Chat", "ai-chat.py"),
    ("2", "TikTok Downloader", "tt-downloaded.py"),
    ("3", "YouTube MP3", "yt-downloaded.py"),
    ("4", "All-in-One Downloader", "all-downloaded.py"),
    ("5", "Al-Quran", "al-quran.py"),
    ("6", "Jadwal Sholat", "jadwal-sholat.py"),
    ("7", "Asmaul Husna", "asmaul-husna.py"),
    ("8", "Doa Harian", "doa-harian.py"),
    ("9", "Hadits Arbain", "hadits-arbain.py"),
    ("10", "Translate", "translate.py"),
    ("11", "Auto Translate", "auto-translate.py"),
    ("12", "Cek Cuaca", "weather.py"),
    ("13", "Google Search", "google-search.py"),
    ("14", "YouTube Search", "youtube-search.py"),
    ("15", "Berita", "news.py"),
    ("16", "Dictionary", "dictionary.py"),
    ("17", "Country Info", "country-info.py"),
    ("18", "GitHub Info", "github-info.py"),
    ("19", "TikTok Transcript", "tiktok-transcript.py"),
    ("20", "Anime Quote", "anime-quote.py"),
    ("21", "Brat Maker", "brat-maker.py"),
    ("22", "Web Screenshot", "ssweb.py"),
    ("23", "URL Shortener", "url-shortener.py"),
]


def main():
    while True:
        clear()
        title("X-ValeZ Tools")
        section(f"Developer • {AUTHOR}")
        if not VEXO_API_KEY.strip():
            info("VEXO_API_KEY belum diisi di config.py")
        else:
            info("API key terpasang")
        print()
        for key, name, _ in TOOLS:
            print(f"{key:>2}. {name}")
        print(" Q. Keluar")
        print()
        choice = input("Pilih: ").strip().lower()
        if choice == "q":
            break
        selected = next((x for x in TOOLS if x[0] == choice), None)
        if not selected:
            continue
        subprocess.run([sys.executable, str(Path(__file__).with_name(selected[2]))])


if __name__ == "__main__":
    main()
