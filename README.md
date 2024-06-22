## 도커 이미지 만들어보기
- back-end : Fastapi, MySQL
- front-end : React

## Compose 파일 실행
```
docker compose up -d --build
```

## 특이사항
- .env 파일 업로드 안함
- 백엔드 컨테이너가 안될때 Doker Desktop에서 Run누르면 실행됨..

## .env 작성 예시
```
MYSQL_ROOT_PASSWORD=1234
MYSQL_DATABASE=test
URL_DATABASE=mysql+pymysql://root:1234@db:3306/test
```
