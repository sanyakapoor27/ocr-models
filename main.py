from fastapi import FastAPI, File, UploadFile
from paddleocr import PaddleOCR
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import shutil
import os

app = FastAPI()

# CORS for Express JS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models
ocr_models = {
    'en': PaddleOCR(use_angle_cls=True, lang='en'),
    'devanagari': PaddleOCR(use_angle_cls=True, lang='devanagari'),
}

@app.post("/ocr/")
async def ocr_scan(lang: str, file: UploadFile = File(...)):
    if lang not in ocr_models:
        return {"error": "Unsupported language"}

    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = ocr_models[lang].ocr(temp_file, cls=True)

    os.remove(temp_file)

    extracted_text = ""
    for line in result:
        for word in line:
            extracted_text += word[1][0] + " "

    return {"text": extracted_text.strip()}
