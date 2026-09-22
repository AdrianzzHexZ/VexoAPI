from lib.app import run, ask

def main():
    def build():
        return {"text": ask("Tulis pesan:")}
    run("AI Chat", "/api/ai/gemini", build)

if __name__ == "__main__":
    main()
