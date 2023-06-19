from django.db import models


class Svaz(models.Model):
    last_name = models.CharField('Фамилия', max_length=100)
    first_name = models.CharField('Имя', max_length=100)
    biografy = models.TextField('Биография')
    data_roj = models.DateField('Дата рождения')
    email = models.EmailField('Email')
    image = models.ImageField('Фотография')
    otvet = models.BooleanField('Ответили', default=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Контактные данные'
