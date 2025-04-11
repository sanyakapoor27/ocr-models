FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install https://paddleocr.bj.bcebos.com/whl/cpu/avx/paddlepaddle-2.5.0-cp39-cp39-linux_x86_64.whl

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
