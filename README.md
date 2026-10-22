# Skystore

Учебный проект интернет-магазина цифровых товаров: плагинов, примеров кода, скриптов и других решений для разработчиков.
Проект развивается в рамках курса по Django и будет дополняться на каждом уроке.

## Стек

- Python 3.14
- Django 6.1.2
- Bootstrap 5 (CDN)
- SQLite (база данных для разработки)

## Установка и запуск

```bash
# 1. Виртуальное окружение
python -m venv venv

# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

# 2. Зависимости
pip install -r requirements.txt

# 3. Миграции
python manage.py migrate

# 4. Сервер разработки
python manage.py runserver
```

Приложение доступно по адресу <http://127.0.0.1:8000/>.

## Страницы

| Адрес       | Описание                                  |
|-------------|-------------------------------------------|
| `/`         | Главная страница (каталог товаров)        |
| `/home/`    | Главная страница (альтернативный адрес)   |
| `/contacts/`| Страница контактов с формой обратной связи|
| `/admin/`   | Админ-панель Django                       |

## Структура проекта

```
.
├── catalog/                  # Приложение каталога
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   └── contacts.html
│   ├── urls.py
│   ├── views.py
│   ├── models.py
│   └── ...
├── skystore/                 # Настройки Django-проекта
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

## Правила работы с Git (GitFlow)

- `main` — стабильная ветка, только проверенный код;
- `develop` — основная ветка разработки;
- `feature/<название>` — ветки под отдельные задачи, вливаются в `develop` через pull request.

## Автор

Учебный проект в рамках курса по Django.
