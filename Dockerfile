FROM frolvlad/alpine-python-machinelearning:latest

RUN pip install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
ENTRYPOINT  ["python"]
CMD ["app.py"]