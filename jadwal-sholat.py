from lib.app import run, ask

def main():
    run("Jadwal Sholat", "/api/islamic/jadwal-sholat", lambda: {"kota": ask("Kota:")})

if __name__ == "__main__":
    main()
