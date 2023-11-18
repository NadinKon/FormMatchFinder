## FormMatchFinder
Web-приложение для определения заполненных форм. <br>
В базе данных хранится список шаблонов форм. На вход /get_form POST передаются данные, в ответ нужно вернуть имя шаблона формы, если она была найдена. <br>
Если подходящей формы не нашлось, вернуть ответ в формате
{
    f_name1: FIELD_TYPE,
    f_name2: FIELD_TYPE
}
где FIELD_TYPE это тип поля, выбранный на основе правил валидации.

### Технологии
<li> FastAPI
<li> MongoDB
<li> Docker

### Установка
Клонируйте репозиторий https://github.com/NadinKon/FormMatchFinder.git <br>

### Работа
Собрать образ: docker-compose build <br>
Запустить: docker-compose up или docker-compose up -d --build <br>

После запуска, чтобы выполнить скрипт init_db.py и добавить шаблоны в базу данных MongoDB: <br>
- получить доступ к контейнеру приложения: docker exec <br>
- найти имя или ID контейнера приложения: docker ps <br>
- запустить сессию: docker exec -it <имя_или_id_контейнера_приложения> /bin/bash <br>
- запустите скрипт init_db.py: python init_db.py <br>

#### Тесты можно запустить внутри контейнера приложения, используя следующую команду: pytest test_api.py
