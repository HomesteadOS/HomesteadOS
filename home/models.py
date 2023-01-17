from django.contrib.gis.db import models


# Create your models here.
class HomeStead(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()


class Location(models.Model):
    homestead = models.ForeignKey(HomeStead, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
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


class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


class ExpenseClassification(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    spender = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, related_name='spender')
    debtor = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, related_name='debtor')
    datetime = models.DateTimeField()
    description = models.TextField()
    percent = models.IntegerField()
    classification = models.ForeignKey(ExpenseClassification, on_delete=models.DO_NOTHING)
    classification_detail = models.TextField()
    paid_external = models.BooleanField()
    paid_internal = models.BooleanField()
    approved = models.BooleanField(default=True)
    store = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    homestead = models.ForeignKey(HomeStead, on_delete=models.CASCADE)
    start_date = models.DateField()
    due_date = models.DateField()
    staff_responsible = models.ForeignKey(Staff, on_delete=models.CASCADE)


class CapitalInvestment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()


class Budget(models.Model):
    property_cost = models.DecimalField(max_digits=10, decimal_places=2)
    property_cost_monthly = models.DecimalField(max_digits=10, decimal_places=2)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    capital_investment = models.ManyToManyField(CapitalInvestment, related_name='investments')
    period_start = models.DateTimeField()
    period_end = models.DateTimeField()

