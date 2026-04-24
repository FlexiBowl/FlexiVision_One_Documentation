from pathlib import Path

exec((Path(__file__).resolve().parents[2] / "_shared" / "conf_common.py").read_text(encoding="utf-8"), globals())
