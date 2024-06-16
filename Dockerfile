FROM python:3.11
RUN mkdir /currency
WORKDIR /currency
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod a+x /currency/docker/app.sh