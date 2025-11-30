from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "recipes_sample.json"
CHROMA_DIR = ROOT / ".chroma_db"

TOP_K = 3
