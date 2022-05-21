FROM python
WORKDIR /code

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main.py"]
