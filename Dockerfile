FROM python:alpine3.19

RUN apk add --no-cache gcc musl-dev

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["python","./src/app.py"]
