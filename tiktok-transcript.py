from lib.app import run, ask

def main():
    run("TikTok Transcript", "/api/tools/tttranscript", lambda: {"url": ask("URL TikTok:")})

if __name__ == "__main__":
    main()
