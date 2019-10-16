from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField()
    country = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    balance = models.IntegerField()

    def __str__(self):
        return f'<id({self.id}): 이름:{self.last_name}{self.first_name}, 나이: {self.age} 지역: {self.country}, 전번: {self.phone} 잔액: {self.balance}>'