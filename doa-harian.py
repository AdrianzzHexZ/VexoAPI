from lib.app import run, ask

def main():
    value = ask("Kata pencarian doa (Enter = semua):")
    run("Doa Harian", "/api/islamic/doa-harian", (lambda: {"query": value}) if value else lambda: {})

if __name__ == "__main__":
    main()
