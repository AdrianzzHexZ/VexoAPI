from lib.app import run, ask

def main():
    run("YouTube Search", "/api/search/youtube", lambda: {"query": ask("Query:")})

if __name__ == "__main__":
    main()
