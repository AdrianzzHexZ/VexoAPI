from lib.app import run, ask

def main():
    run("Google Search", "/api/search/google", lambda: {"query": ask("Query:")})

if __name__ == "__main__":
    main()
