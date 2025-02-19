FROM python:3.11.11-alpine3.21

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY bot/ ./bot/

CMD ["python", "bot/bot.py"]
