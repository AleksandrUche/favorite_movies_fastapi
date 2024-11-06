### О проекте 
RESTFull API сервис, который позволяет пользователям регистрироваться,
аутентифицироваться и управлять списком своих избранных фильмов. Интеграция с Kinopoisk
API Unofficial для получения информации о фильмах.

### Технологический стек:
- FastAPI
- SQLAlchemy 2.0
- AsyncIO
- Httpx
- JWT для аутентификации

### Для запуска приложения выполнить следующие шаги:

1. Если у вас еще не установлен poetry, это можно сделать с помощью команды:
   ```pip install poetry```.
2. Находясь в директории проекта с файлом pyproject.toml, установить зависимости с
   помощью команды: ```poetry install```.
3. Необходимо поднять postgresql с помощью команды:

```
docker run -p 5432:5432 --name postgres_movie -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=12345 -e POSTGRES_DB=postgres -d postgres:13.1
```

4. Создайте файл ```.env``` по примеру файла ```.env-example```, не забудьте указать
   API_KEY_KINOPOISK.
5. Проведите миграции: ```alembic upgrade head```.
6. Запуск приложения: ```uvicorn app.main:app --reload```.