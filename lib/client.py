import json
import urllib.error
import urllib.parse
import urllib.request
from config import VEXO_API_KEY

BASE_URL = "https://vexoapi.site"
TIMEOUT = 25


def request(path, params=None):
    if not VEXO_API_KEY.strip():
        raise RuntimeError("VEXO_API_KEY belum diisi di config.py")
    query = dict(params or {})
    query["apikey"] = VEXO_API_KEY.strip()
    url = BASE_URL + path + "?" + urllib.parse.urlencode(query, doseq=True)
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "X-ValeZ_Tools/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as res:
            raw = res.read()
            status = res.status
    except urllib.error.HTTPError as e:
        raw = e.read()
        status = e.code
    except urllib.error.URLError as e:
        raise RuntimeError(f"Koneksi gagal: {e.reason}") from e
    except TimeoutError as e:
        raise RuntimeError("Request timeout") from e
    try:
        data = json.loads(raw.decode("utf-8", "replace"))
    except json.JSONDecodeError:
        raise RuntimeError(f"Response bukan JSON (HTTP {status})")
    if status >= 400:
        raise RuntimeError(str(data.get("message", f"HTTP {status}")) if isinstance(data, dict) else f"HTTP {status}")
    if isinstance(data, dict) and data.get("status") is False:
        raise RuntimeError(str(data.get("message", "Request ditolak")))
    return data


def pretty(data):
    return json.dumps(data, ensure_ascii=False, indent=2)


def find_first(value, keys):
    if isinstance(value, dict):
        for key in keys:
            if key in value and value[key]:
                return value[key]
        for item in value.values():
            hit = find_first(item, keys)
            if hit is not None:
                return hit
    elif isinstance(value, list):
        for item in value:
            hit = find_first(item, keys)
            if hit is not None:
                return hit
    return None
