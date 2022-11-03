
FROM python:3.8.6-buster

COPY mi-person/app.py /app.py
COPY requirements.txt /requirements.txt
COPY mi-person/ml_logic/model.py /ml_logic/model.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0",  "--port",  "8080"]

