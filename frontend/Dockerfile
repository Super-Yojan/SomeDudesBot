FROM python
WORKDIR /code

RUN apt install libffi-dev libnacl-dev python3-dev
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main.py"]
