import os
import shutil
import textwrap

R = "\033[0m"
B = "\033[1m"
CY = "\033[96m"
BL = "\033[94m"
GR = "\033[92m"
YE = "\033[93m"
RE = "\033[91m"
WH = "\033[97m"
DM = "\033[90m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def width():
    return max(42, min(shutil.get_terminal_size((80, 24)).columns - 2, 78))


def title(text):
    w = width()
    print(f"{BL}╭{'─' * (w - 2)}╮{R}")
    print(f"{BL}│{R}{B}{CY}{text.center(w - 2)}{R}{BL}│{R}")
    print(f"{BL}╰{'─' * (w - 2)}╯{R}")


def section(text):
    print(f"\n{CY}{B}▸ {text}{R}")


def line(label, value):
    w = width()
    prefix = f"{DM}{label}{R} "
    avail = max(12, w - len(label) - 1)
    parts = textwrap.wrap(str(value), width=avail) or [""]
    print(prefix + parts[0])
    pad = " " * (len(label) + 1)
    for part in parts[1:]:
        print(pad + part)


def panel(text, color=WH):
    w = width()
    inner = w - 4
    print(f"{BL}╭{'─' * (w - 2)}╮{R}")
    for raw in str(text).splitlines() or [""]:
        rows = textwrap.wrap(raw, width=inner) or [""]
        for row in rows:
            print(f"{BL}│{R} {color}{row.ljust(inner)}{R} {BL}│{R}")
    print(f"{BL}╰{'─' * (w - 2)}╯{R}")


def ok(text):
    print(f"{GR}✓{R} {text}")


def fail(text):
    print(f"{RE}✗{R} {text}")


def info(text):
    print(f"{YE}•{R} {text}")


def ask(text):
    return input(f"{CY}{text}{R} ").strip()
