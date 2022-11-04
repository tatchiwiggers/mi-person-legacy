
FROM python:3.8.6-buster

COPY scripts/app.py scripts/app.py
COPY scripts/model.py model.py
COPY requirements.txt requirements.txt
COPY scripts/model.py scripts/model.py
COPY scripts/__init__.py scripts/__init__.py



RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn scripts.app:app --host 0.0.0.0
