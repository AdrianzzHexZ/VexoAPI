from lib.app import run, ask

def main():
    run("All-in-One Downloader", "/api/download/aio", lambda: {"url": ask("URL:")})

if __name__ == "__main__":
    main()
