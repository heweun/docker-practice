FROM python:3.11.9
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install cryptography
RUN pip install python-dotenv
COPY ./app /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]