import json
from pathlib import Path

JSON_PATH = Path(__file__).parent.parent.parent / "data" / "ng.json"

def load_ng_json():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

ng_json_data = load_ng_json()