from django.db import models
import uuid

# Create your models here.


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=64, default=uuid.uuid1())
    email = models.EmailField()
    user_name = models.CharField(max_length=64)
    password = models.CharField(max_length=256)
    type_user = models.BooleanField()

    def __str__(self):
        return self.id


class Company(models.Model):
    id = models.CharField(primary_key=True, max_length=64, default=uuid.uuid1())
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.id


class Character(models.Model):
    id = models.CharField(primary_key=True, max_length=64, default=uuid.uuid1())
    name = models.CharField(max_length=64)
    alias = models.CharField(max_length=64)
    image = models.CharField(max_length=512)
    id_company = models.ForeignKey(
        "heros_apis.Company", on_delete=models.CASCADE
    )

    def __str__(self):
        self.id


class Score(models.Model):
    id = models.CharField(primary_key=True, max_length=64, default=uuid.uuid1())
    id_character = models.ForeignKey(
        "heros_apis.Character", on_delete=models.CASCADE
    )
    id_user = models.ForeignKey("heros_apis.User", on_delete=models.CASCADE)
    points = models.SmallIntegerField()

    def __str__(self):
        return self.id
