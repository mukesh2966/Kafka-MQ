FROM python:3.9-slim

WORKDIR /home
ENV PYTHONUNBUFFERED=1



COPY . ./

RUN chmod +x ./run.sh

CMD ./run.sh