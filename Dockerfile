FROM python:3.9-slim-buster

EXPOSE 8501

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /airbnb

COPY . /airbnb

RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "airbnb.py", "--server.port=8501", "--server.address=0.0.0.0"]
