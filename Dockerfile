FROM python:3

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["flask", "run", "--debug", "--host=0.0.0.0", "--port=8000"]