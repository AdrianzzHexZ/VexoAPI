from lib.app import run, ask

def main():
    value = ask("Nomor surah (Enter = semua):")
    run("Al-Quran", "/api/islamic/quran", (lambda: {"surah": value}) if value else lambda: {})

if __name__ == "__main__":
    main()
