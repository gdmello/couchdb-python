# couchdb-python
Build image

`  $ docker build -t couchdb-python:1.6.1 .`
  
Run image

`  $ docker run couchdb-python:1.6.1`
  
Access Futon
```
  $ docker ps | grep couchdb-python
    CONTAINER ID  IMAGE                  COMMAND                  CREATED       STATUS        PORTS     NAMES
    622d9a1f892b  couchdb-python:1.6.1   "tini -- /docker-entr"   9 seconds ago Up 8 seconds  5984/tcp  reverent_darwin
  $ docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' 622d9
    172.17.0.3
  $ curl 172.17.0.3:5984
    {"couchdb":"Welcome","uuid":"5955494dc8cb7a8c2c1f5648eab0db53","version":"1.6.1","vendor":{"version":"1.6.1","name":"The Apache Software Foundation"}}
```
