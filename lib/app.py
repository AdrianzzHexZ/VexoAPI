from lib.client import request, pretty
from lib.ui import clear, title, panel, fail, ask, info


def run(tool_name, path, params_builder):
    clear()
    title(f"X-ValeZ Tools • {tool_name}")
    try:
        params = params_builder() if params_builder else {}
        result = request(path, params)
        panel(pretty(result))
    except KeyboardInterrupt:
        print()
    except Exception as e:
        fail(str(e))
    input("\nEnter untuk kembali...")


def one(prompt, key, required=True):
    value = ask(prompt)
    if required and not value:
        raise ValueError(f"{key} wajib diisi")
    return {key: value}
