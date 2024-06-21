# Mockoon 로컬 도커환경 구성 레포


### docker-compose가 다음 환경을 구성합니다:
* npm을 위한 Node.js
* Mockoon-cli 설치 (`npm install -g @mockoon/cli`)
* NginX
* Nginx 프록시 `http://localhost:80/api` to Mockoon-cli port 3000

## 설치 
docker-compose로 시작할 수 있습니다.
~~~
$ cd /경로/mockoon-env-local
$ docker-compose up -d
~~~

## Mockoon API 데이터 교체
