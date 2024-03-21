FROM python:3.8-slim

WORKDIR /python-docker

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY index.py .

EXPOSE 9001

CMD ["python", "index.py"]