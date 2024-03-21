FROM python:3.8-slim

WORKDIR /python-docker

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY profile.py .

EXPOSE 9002

CMD ["python", "profile.py"]