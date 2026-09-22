from lib.app import run, ask

def main():
    run("Brat Maker", "/api/maker/brat", lambda: {"text": ask("Teks:")})

if __name__ == "__main__":
    main()
