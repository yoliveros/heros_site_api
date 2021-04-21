from django.db import models
import uuid

# Create your models here.


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=64,
                          default=uuid.uuid1())
    email = models.EmailField()
    user_name = models.CharField(max_length=64)
    password = models.CharField(max_length=256)
    type_user = models.BooleanField()

    def __str__(self):
        return self.id


class Score(models.Model):
    id = models.CharField(primary_key=True, max_length=64,
                          default=uuid.uuid1())
    id_character = models.ForeignKey("Characters", on_delete=models.CASCADE)
    id_user = models.ForeignKey("Users", on_delete=models.CASCADE)
    points = models.IntegerField(max_length=1)

    def __str__(self):
        return self.id


class Character(models.Model):
    id = models.CharField(primary_key=True, max_length=64,
                          default=uuid.uuid1())
    name = models.CharField(max_length=64)
    alias = models.CharField(max_length=64)
    image = models.ImageField()
    id_score = models.ForeignKey("Score", on_delete=models.CASCADE)
    id_company = models.ForeignKey("Company", on_delete=models.CASCADE)

    def __str__(self):
        self.id


class Company(models.Model):
    id = models.CharField(primary_key=True, max_length=64,
                          default=uuid.uuid1())
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.id
