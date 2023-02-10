from django.db import models


class BaseModel(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now_add=True)
