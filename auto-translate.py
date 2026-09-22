from lib.app import run, ask

def main():
    run("Auto Translate", "/api/tools/autotranslate", lambda: {"text": ask("Teks:")})

if __name__ == "__main__":
    main()
