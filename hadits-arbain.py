from lib.app import run, ask

def main():
    value = ask("Nomor hadits (Enter = semua):")
    run("Hadits Arbain", "/api/islamic/hadits-arbain", (lambda: {"no": value}) if value else lambda: {})

if __name__ == "__main__":
    main()
