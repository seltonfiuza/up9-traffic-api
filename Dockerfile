FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app/app

ENV WORKER_CLASS="uvicorn.workers.UvicornH11Worker"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]