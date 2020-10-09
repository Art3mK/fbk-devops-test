# Тестовое задание
- bring up: `docker-compose up`
- post record: `curl --header "Content-Type: application/json" -d '{"message":"Hello from CLI"}' http://127.0.0.1:8080/`
- list records in db: `docker-compose exec db psql -U postgres -d messages -c 'select * from messages;'`
