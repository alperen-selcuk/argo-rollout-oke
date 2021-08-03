## build and run
Without using docker-compose:
```
docker build -t py-app .

docker run -d --env COLOR=RED -p 5000:5000 py-app
```

## call
```
curl -s localhost:5000 | grep label

while true; do curl -s localhost:5000 | grep label; sleep 0.1; done
```
