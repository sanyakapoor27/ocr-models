from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import io

app = FastAPI()

# Health check
@app.get("/")
async def root():
    return {"message": "OCR API running"}

# OCR Endpoint
@app.post("/ocr/")
async def ocr_image(file: UploadFile = File(...), lang: str = Form(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    # OCR Processing
    try:
        text = pytesseract.image_to_string(image, lang=lang)
    except pytesseract.TesseractError as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

    return {"text": text}
