# Mockoon CLI 서버 로컬도커 환경 구성 Repository


## Mockoon 데이터 파일 준비 
Mockoon 컨테이너가 정상적으로 시작되려면 먼저 `/mockoon/data` 폴더를 만들고 하위에 `evergreen.json` 이라는 이름으로 Mockoon API environment 파일을 추가해야합니다. 이 파일을 빼먹고 docker-compose를 시작했다면 파일을 추가후  mockoon 컨테이너를 재시작 하세요.

## Docker compose로 시작하기 
~~~
$ cd /경로/mockoon-env-local
$ docker-compose up -d
~~~
#### docker-compose는 다음 환경을 구성합니다:
* npm을 위한 Node.js
* Mockoon-cli 설치 (`npm install -g @mockoon/cli`)
* 파이썬: Mockoon API 데이터파일 기반으로 Swagger spec 파일을 생성하기위함 
* Swagger UI
* NginX : 포트 라우팅

#### 접속
http://localhost:8080

## Mockoon API 데이터 교체
 `/mockoon/data` 하위에 `evergreen.json` 파일을 교체한뒤에는 `mockoon` 컨테이너를 재시작해야 새로운 API가 반영됩니다.
 * $ `docker-compose restart mockoon`
