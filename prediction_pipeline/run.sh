docker build -t gcr.io/molten-reserve-317003/predict:latest .

docker push gcr.io/molten-reserve-317003/predict:latest

docker rm -f app

docker run --net=host -d --name=app -v $(pwd)/test/:/mnt/c/mk1/uploads -e PORT=8080 gcr.io/molten-reserve-317003/predict:latest

docker logs -f app