FROM python:3.10

COPY . /fast_api
WORKDIR /fast_api 
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
