[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
# Тестовое задание UpTrader

### Задание

Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1. Меню реализовано через template tag
2. Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3. Хранится в БД.
4. Редактируется в стандартной админке Django
5. Активный пункт меню определяется исходя из URL текущей страницы
6. Меню на одной странице может быть несколько. Они определяются по названию.
7. При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8. На отрисовку каждого меню требуется ровно 1 запрос к БД
 Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
 {% draw_menu 'main_menu' %}

При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.

### Настройки

.env:
```dotenv
SECRET_KEY= 
```
## Запуск проекта
### Склонировать репозиторий на локальную машину:
```
git clone https://github.com/Bogdan.Odilov/admin_menu
```
### Для работы
1. Установить виртуальное окружение python -m venv venv
2. Активировать виртуальное окружение source venv/scripts/activate
3. Установить зависимости pip install -r requirements.txt
4. Выполнить миграции python manage.py migrate
5. Выполните команду python manage.py syncdb для обновления структуры БД
6. Запустить сервет python manage.py runserver
7. Создайте суперюзер python manage.py createsuperuser
8. Перейдите в админ панель по ссылке http://127.0.0.1:8000/admin/

### Админ панель

![alt text](https://code-live.ru/media/upload/images/2013/07/27/django_mymenu_admin_1.png)
