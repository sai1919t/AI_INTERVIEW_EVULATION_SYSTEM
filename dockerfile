FROM python:3.11.6

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y ffmpeg libgl1

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python", "main.py"]