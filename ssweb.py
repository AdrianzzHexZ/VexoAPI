from lib.app import run, ask

def main():
    def build():
        url = ask("URL website:")
        device = ask("Device (desktop/mobile):") or "desktop"
        theme = ask("Theme (light/dark):") or "light"
        full_page = ask("Full page? [Y/n]:").lower() != "n"
        return {"url": url, "device": device, "theme": theme, "fullPage": str(full_page).lower()}
    run("Web Screenshot", "/api/tools/ssweb", build)

if __name__ == "__main__":
    main()
