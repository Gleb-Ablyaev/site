from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=70, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', default=0)

    TYPE = [
        ('BRK', 'Завтрак'),
        ('LUN','Обед'),
        ('DIN','Ужин'),
    ]
    type = models.CharField(choices=TYPE, max_length=3, default='BRK', verbose_name='Тип')

    def __str__(self):
        return self.title