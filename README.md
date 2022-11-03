# resmanage
Команды
установка Django/ создание проекта

    pip install django
    django-admin startproject res_manage

    cd res_manage

    python manage.py startapp apitest

Git

    инициализируем проект: git init
    создам файл .gitignore и заполняем его

    файл с зависимостями: pip freeze > requirements.txt
    делаем миграции: python manage.py migrate
    создаем admin: python manage.py createsuperuser

 Запускаем проект: python manage.py runserver
 
 Настройки
>>settings.py

INSTALLED_APPS [
    'rest_framework',
    'apitest',
    'phone_field'
]
Доп. Библиотеки
*поле с номером телефона
pip install django-phone-field
pip install djangorestframework
