from lib.app import run, ask

SOURCES = {
    "1": ("CNBC Indonesia", "/api/berita/cnbcindonesia"),
    "2": ("Suara", "/api/berita/suara"),
    "3": ("Liputan6", "/api/berita/liputan6"),
    "4": ("Tribunnews", "/api/berita/tribunnews"),
    "5": ("Sindonews", "/api/berita/sindonews"),
    "6": ("Kompas", "/api/berita/kompas"),
    "7": ("Merdeka", "/api/berita/merdeka"),
    "8": ("CNN Indonesia", "/api/berita/cnn"),
    "9": ("JKT48", "/api/berita/jkt48"),
    "10": ("Antara", "/api/berita/antara"),
}

def main():
    print("\n".join(f"{k}. {v[0]}" for k, v in SOURCES.items()))
    choice = ask("Pilih sumber:")
    source = SOURCES.get(choice)
    if not source:
        return
    run(source[0], source[1], lambda: {})

if __name__ == "__main__":
    main()
