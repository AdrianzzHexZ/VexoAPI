from lib.app import run, ask

def main():
    run("Dictionary", "/api/tools/dictionary", lambda: {"word": ask("Kata:")})

if __name__ == "__main__":
    main()
