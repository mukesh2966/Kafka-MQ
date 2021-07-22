docker build -t predict:latest .

docker rm -f predict

docker run --net=host -d --name=predict -v $(pwd)/:/mnt/c/mk1/uploads -e PORT=8080 predict:latest

docker logs -f predict