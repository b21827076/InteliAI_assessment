from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name.__add__(self.surname).__add__(self.email)