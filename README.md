# Структура проекта
```
django-internet-shop/
|—— api/ # Приложение для API
    |—— blog/ # API для блога 
    |—— products/ # API для продуктов
    |—— users/ # API для пользователей 
    |—— __init__.py
    |—— apps.py
    |—— permissions.py
    |—— urls.py
|—— blog/ # Приложение блога
    |—— migrations/
    |—— templates/
    |—— tenplatetags/
    |—— __init__.py
    |—— admin.py
    |—— apps.py
    |—— forms.py
    |—— models.py
    |—— urls.py
    |—— views.py
|—— config/ # Настройки проекта
    |—— __init__.py
    |—— asgi.py
    |—— settings.py
    |—— urls.py
    |—— wsgi.py
|—— media/ # Изображения
    |—— shopapp/
|—— nginx/ # Нстройка для образа nginx
    |—— Dockerfile
    |—— nginx.conf
|—— products/ # Приложения продуктов
    |—— management/
    |—— migrations/  
    |—— templates/
    |—— templatetags/
    |—— __init__.py
    |—— admin.py
    |—— apps.py
    |—— forms.py
    |—— models.py
    |—— urls.py
    |—— views.py
|—— static/ # Статика (css, js)
    |—— css/
    |—— js/
|—— users/ # Приложение пользователей
    |—— management/
    |—— migrations/
    |—— templates/
    |—— templatetags/
    |—— __init__.py
    |—— admin.py
    |—— apps.py
    |—— forms.py
    |—— models.py
    |—— urls.py
    |—— views.py
|—— .dockerignore
|—— .env.sample
|—— .flake8
|—— .gitignore
|—— docker-compose.dev.yml
|—— docker-compose.yml
|—— Dockerfile
|—— gunicorn_config.py
|—— LICENSE
|—— Makefile
|—— manage.py
|—— README.md
|—— requirements.txt
```

# Результаты работы:
- ### Реализован CRUD для блога, продуктов и пользователей
- ### Создано API для приложения и задокументирована в OpenAPI
- ### Разработан механизм аутентификации, авторизации и подтверждения аккаунта по email
- ### Для API механизм аутентификации и авторизации происходит с помощью JWT Token и Bearer
- ### Реализовано кеширование с помощью Redis
- ### Созданы команды для создания админа, модератора и категорий
- ### Реализованы шаблоны для отображения HTML страницы
- ### Написаны тесты для API
- ### Реализован запуск приложения с помощью Docker, gunicorn и nginx
- ### Разработан механизм непрерывной интеграции (CI)

# Основной стек проекта:
- ### Python 3.10
- ### Django 4.2
- ### Django REST Framework 3.15
- ### PostgreSQL 11
- ### Django ORM
- ### gunicorn
- ### Redis
- ### Docker
- ### GitHub Actions (CI)

# Как пользоваться проектом

## 1) Скопируйте проект на Ваш компьютер
```
git clone git@github.com:Nk3YQQ/django-internet-shop.git
```

## 2) Добавьте файл .env для переменных окружения
Чтобы запустить проект, понадобятся переменные окружения, которые необходимо добавить в созданный Вами .env файл.

Пример переменных окружения необходимо взять из файла .env.sample

## 3) Запустите проект

Запуск проекта
```
make run
```

Остановка проекта
```
make stop
```
