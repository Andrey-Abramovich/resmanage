from django.db import models
from phone_field import PhoneField


class Person(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя пользователя')
    birth = models.DateField(verbose_name='Дата рождения')
    login = models.CharField(max_length=24, unique=True)
    password = models.CharField(max_length=24)
    phone = PhoneField(null=False, unique=True, help_text='Введите номер телефона')
    tg = models.CharField(max_length=50, blank=True, help_text='Ваш никнейм в Telegram')
    email = models.EmailField(blank=True)

    def __str__(self):
        return '{}'.format(self.name)
