FROM python:3.11.11-alpine3.21

WORKDIR /app

RUN apk add --no-cache nodejs npm

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY bot/ ./bot/

CMD ["python", "bot/bot.py"]
