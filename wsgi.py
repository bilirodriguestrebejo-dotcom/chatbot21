import sys
from pathlib import Path

# Agregar la carpeta backend al path de Python
BACKEND_DIR = Path(__file__).resolve().parent / "chatbot 5" / "backend"
sys.path.insert(0, str(BACKEND_DIR))

from appy import app

