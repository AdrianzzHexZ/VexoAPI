from lib.app import run, ask

def main():
    run("Cek Cuaca", "/api/tools/cekcuaca", lambda: {"kota": ask("Kota:")})

if __name__ == "__main__":
    main()
