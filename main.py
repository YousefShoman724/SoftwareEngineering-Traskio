# root main.py so tests can import main
try:
    from backend.main import app
except Exception:
    from backend.app import app
