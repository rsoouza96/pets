from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)


class Characteristic(models.Model):
    characteristic = models.CharField(max_length=255)


class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField(max_length=255)
    weight = models.FloatField(max_length=255)
    sex = models.CharField(max_length=255)
    characteristic_set = models.ManyToManyField(Characteristic)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)