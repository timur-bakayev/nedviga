from django.db import models
from .base_model import BaseModel


class House(models.Model):
    class Type(models.TextChoices):
        dom = 'дом', 'ДОМ'
        kvartira = 'квартира', 'КВАРТИРА'
        dacha = 'дача', 'ДАЧА'

    base_role = Type.dom
    role = models.CharField(max_length=255, choices=Type.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class Kvartira(House):
    base_role = House.Type.kvartira
    title = models.CharField(max_length=255)


class Dacha(House):
    base_role = House.Type.dacha
    title = models.CharField(max_length=255)
    price = models.IntegerField()
