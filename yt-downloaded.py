from lib.app import run, ask

def main():
    run("YouTube MP3", "/api/download/ytmp3", lambda: {"url": ask("URL YouTube:")})

if __name__ == "__main__":
    main()
