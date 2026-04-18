FROM python:3.11.6

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y ffmpeg libgl1

RUN libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["gunicorn", "--timeout", "120", "-b", "0.0.0.0:10000", "main:app"]