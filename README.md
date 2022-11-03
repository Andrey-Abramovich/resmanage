# resmanage
РАБОЧАЯ ВЕТКА MAIN

Команды

установка Django/ создание проекта

    1.pip install django
    2.django-admin startproject res_manage

    3.cd res_manage

    4.python manage.py startapp apitest

 Git

    5.инициализируем проект: git init
    6.создам файл .gitignore и заполняем его

    7.файл с зависимостями: pip freeze > requirements.txt
    8.делаем миграции: python manage.py migrate
    9.создаем admin: python manage.py createsuperuser

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
