from lib.app import run, ask

def main():
    run("TikTok Downloader", "/api/download/tiktok-hd", lambda: {"url": ask("URL TikTok:")})

if __name__ == "__main__":
    main()
