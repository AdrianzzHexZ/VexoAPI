from lib.app import run, ask

def main():
    run("URL Shortener", "/api/tools/shorturl", lambda: {"url": ask("URL panjang:")})

if __name__ == "__main__":
    main()
