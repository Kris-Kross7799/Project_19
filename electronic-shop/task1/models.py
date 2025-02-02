from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=300, unique=True)  # Имя покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2) #Баланс
    age = models.PositiveIntegerField() #возраст

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)  # Название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена игры
    size = models.DecimalField(max_digits=10, decimal_places=2)  # размер файлов игры
    description = models.TextField(blank=True)  # Описание игры
    age_limited=models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title
