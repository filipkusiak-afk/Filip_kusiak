import os
import sys

print("--- RAPORT STANU PROJEKTU ---")

# 1. Sprawdzanie bibliotek
try:
    import cv2
    print("[OK] OpenCV jest zainstalowane (wersja: " + cv2.__version__ + ")")
except ImportError:
    print("[BŁĄD] Brakuje OpenCV! Wpisz w terminalu: pip install opencv-python")

try:
    import fastapi
    print("[OK] FastAPI jest zainstalowane")
except ImportError:
    print("[BŁĄD] Brakuje FastAPI! Wpisz w terminalu: pip install fastapi uvicorn")

# 2. Sprawdzanie plików
if os.path.exists("haarcascade_fullbody.xml"):
    print("[OK] Plik modelu (XML) jest na miejscu.")
else:
    print("[BŁĄD] Brakuje pliku haarcascade_fullbody_default.xml!")

if os.path.exists("test.jpg"):
    print("[OK] Plik testowy (test.jpg) jest na miejscu.")
else:
    print("[OSTRZEŻENIE] Brakuje pliku test.jpg (ale program ruszy bez niego, po prostu nie przetestujesz uploadu lokalnego).")

print("-----------------------------")
