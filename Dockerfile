FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y gcc libglib2.0-0 libsm6 libxrender1 libxext6 wget

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install https://paddleocr.bj.bcebos.com/whl/linux/mkl/avx/stable/paddlepaddle-2.4.0-cp39-cp39-linux_x86_64.whl

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

