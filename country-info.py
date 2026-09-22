from lib.app import run, ask

def main():
    run("Country Info", "/api/tools/countryInfo", lambda: {"name": ask("Negara:")})

if __name__ == "__main__":
    main()
