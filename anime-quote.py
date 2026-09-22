from lib.app import run

def main():
    run("Anime Quote", "/api/anime/quote", lambda: {})

if __name__ == "__main__":
    main()
