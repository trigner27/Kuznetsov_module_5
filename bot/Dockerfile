FROM python:3.11.8
WORKDIR /bot

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "bot.py"]

