from django.db import models

"""
Пользователь
"""
class User(models.Model):
    STATUS_CHOICES = (
        ('Активирован', 'Активирован'),
        ('Не активирован', 'Не активирован')
    )
    id = models.AutoField(primary_key=True),
    first_name = models.CharField(max_length=50, verbose_name="Имя"),
    last_name = models.CharField(max_length=50, verbose_name="Фамилия"),
    email = models.CharField(max_length=150, verbose_name="Адрес электронной почты"),
    password = models.CharField(max_length=150, verbose_name="Пароль"),
    status = models.CharField(choices=STATUS_CHOICES, default="Не активирован", verbose_name="Статус активации аккаунта"),
    activate_code = models.CharField(max_length=6, null=True, blank=True, verbose_name="Код активации"),

