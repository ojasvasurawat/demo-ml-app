
docker build -t python-app:0.0 .

docker tag python-app:0.0 ojasvasurawat/height-pred-app

docker push ojasvasurawat/height-pred-app