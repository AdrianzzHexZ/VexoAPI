from lib.app import run, ask

def main():
    def build():
        text = ask("Teks:")
        source = ask("Bahasa asal (contoh en):") or "auto"
        target = ask("Bahasa tujuan (contoh id):") or "id"
        return {"text": text, "source": source, "target": target}
    run("Translate", "/api/tools/translate", build)

if __name__ == "__main__":
    main()
