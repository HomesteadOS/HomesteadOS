from django.db import models


# Create your models here.
class HomeStead(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()


class Location(models.Model):
    homestead = models.ForeignKey(HomeStead, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    address = models.
    description = models.TextField()
    primary_location = models.BooleanField()


class Staff(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    primary_location = models.ForeignKey(Location, on_delete=models.CASCADE)


class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    email = models.EmailField()


class RoleClasses(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    enabled = models.BooleanField()


class YieldUnits(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abbreviation = models.CharField(max_length=3)


class Crop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    plant_date = models.DateTimeField()
    harvest_date = models.DateTimeField()
    harvest_target_date = models.DateTimeField()
    yield_goal = models.IntegerField()
    yield_unit = models.ForeignKey(YieldUnits, on_delete=models.CASCADE)
    yield_actual = models.IntegerField()


class Field(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
