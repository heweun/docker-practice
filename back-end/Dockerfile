FROM python:3.11.9
WORKDIR /app

# dockerize 설치
ADD https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz /tmp/
RUN tar -C /usr/local/bin -xzvf /tmp/dockerize-linux-amd64-v0.6.1.tar.gz

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install cryptography
RUN pip install python-dotenv
COPY ./app /app
CMD ["dockerize", "-wait", "tcp://db:3306", "-timeout", "60s", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
