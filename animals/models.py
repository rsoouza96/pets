from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Characteristic(models.Model):
    characteristic = models.CharField(max_length=255)
    
    def __str__(self):
        return self.characteristic


class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField(max_length=255)
    weight = models.FloatField(max_length=255)
    sex = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    characteristic_set = models.ManyToManyField(Characteristic)
    
    def __str__(self):
        return self.name