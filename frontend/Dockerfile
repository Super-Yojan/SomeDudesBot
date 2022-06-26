FROM python
WORKDIR /code

COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip install -U py-cord --pre

COPY . .

ENTRYPOINT ["python", "main.py"]
