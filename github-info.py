from lib.app import run, ask

def main():
    run("GitHub Info", "/api/tools/github", lambda: {"user": ask("Username GitHub:")})

if __name__ == "__main__":
    main()
