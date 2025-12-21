import cv2
import numpy as np
import requests
import uvicorn
import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from ultralytics import YOLO

# Inicjalizacja aplikacji
app = FastAPI(title="Licznik Osób API (YOLOv8)", description="Wykrywanie osób przy użyciu sieci neuronowej YOLO")

# Folder na wyniki
OUTPUT_FOLDER = "processed_images"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("--- ŁADOWANIE MODELU YOLO ---")
print("Przy pierwszym uruchomieniu program pobierze plik 'yolov8n.pt' (ok. 6MB). Czekaj...")
# Ładujemy model "nano" (najlżejszy i najszybszy)
model = YOLO("yolov8n.pt")
print("--- MODEL ZAŁADOWANY ---")


def detect_people_yolo(image_array: np.ndarray, filename: str) -> int:
    """
    Funkcja wykrywająca ludzi za pomocą YOLOv8.
    """
    # 1. Wykonaj detekcję (YOLO robi całą magię tutaj)
    # conf=0.4 oznacza, że AI musi być pewna na min. 40%, że to człowiek
    results = model(image_array, conf=0.4)

    people_count = 0

    # 2. Przeanalizuj wyniki
    # YOLO zwraca listę wykrytych obiektów. Musimy sprawdzić, które to ludzie.
    for result in results:
        boxes = result.boxes
        for box in boxes:
            # Sprawdź klasę obiektu (class_id)
            # W bazie COCO (na której uczone jest YOLO), ID 0 to "person" (człowiek)
            class_id = int(box.cls[0])

            if class_id == 0:  # Jeśli to człowiek
                people_count += 1

                # Pobierz współrzędne ramki
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Narysuj czerwoną ramkę
                cv2.rectangle(image_array, (x1, y1), (x2, y2), (0, 0, 255), 2)

                # (Opcjonalnie) Dodaj napis "Person"
                cv2.putText(image_array, f"Person {int(box.conf[0] * 100)}%", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # 3. Zapisz wynik
    output_path = os.path.join(OUTPUT_FOLDER, f"processed_{filename}")
    cv2.imwrite(output_path, image_array)

    return people_count


# --- ENDPOINTY (Takie same jak wcześniej) ---

@app.get("/")
def home():
    return {"message": "API YOLO działa! Wejdź na /docs"}


@app.get("/count-local")
def count_local(file_path: str):
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Plik nie istnieje")
    img = cv2.imread(file_path)
    if img is None:
        raise HTTPException(status_code=400, detail="Błąd odczytu obrazu")

    filename = os.path.basename(file_path)
    count = detect_people_yolo(img, filename)
    return {"filename": filename, "people_count": count, "file_path": f"{OUTPUT_FOLDER}/processed_{filename}"}


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        raise HTTPException(status_code=400, detail="Nieprawidłowy plik")

    count = detect_people_yolo(img, file.filename)
    return {"filename": file.filename, "people_count": count}


@app.get("/count-url")
def count_url(url: str):
    try:
        resp = requests.get(url, stream=True).raw
        image_data = np.asarray(bytearray(resp.read()), dtype="uint8")
        img = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
        if img is None:
            raise HTTPException(status_code=400, detail="To nie jest obraz")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    count = detect_people_yolo(img, "url_image.jpg")
    return {"source": url, "people_count": count}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)