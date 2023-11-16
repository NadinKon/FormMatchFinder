## FormMatchFinder
Web-приложение для определения заполненных форм.

### Технологии
<li> FastAPI
<li> MongoDB
<li> Docker

### Установка
Клонируйте репозиторий https://github.com/NadinKon/FormMatchFinder.git <br>

### Работа
Собрать образ: docker-compose build
Запустить: docker-compose up

После запуска, чтобы выполнить скрипт init_db.py и добавить шаблоны в базу данных MongoDB: <br>
- получить доступ к контейнеру приложения: docker exec <br>
- найти имя или ID контейнера приложения: docker ps <br>
- запустить сессию docker exec -it <имя_или_id_контейнера_приложения> /bin/bash <br>
- запустите скрипт init_db.py: python init_db.py <br>

Тесты можно запустить внутри контейнера приложения, используя следующую команду: pytest test_api.py
