from django.contrib.gis.db import models


# Create your models here.
class Homestead(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Location(models.Model):
    homestead = models.ForeignKey(Homestead, on_delete=models.CASCADE, related_name="locations")
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    primary_location = models.BooleanField()

    def __str__(self):
        return self.name


class Staff(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    primary_location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class RoleClasses(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    enabled = models.BooleanField()

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    email = models.EmailField()
    role_class = models.ForeignKey(RoleClasses, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class YieldUnits(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abbreviation = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Crop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    plant_date = models.DateTimeField()
    harvest_date = models.DateTimeField()
    harvest_target_date = models.DateTimeField()
    yield_goal = models.IntegerField()
    yield_unit = models.ForeignKey(YieldUnits, on_delete=models.CASCADE)
    yield_actual = models.IntegerField()

    def __str__(self):
        return self.name


class Field(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ExpenseClassification(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
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

    def __str__(self):
        return self.spender.last_name + ', ' + self.spender.first_name + ' spent on ' + self.datetime.__str__() + ' ' \
            + self.debtor.last_name + ', ' + self.debtor.first_name + ' owes ' + self.debt


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    homestead = models.ForeignKey(Homestead, on_delete=models.CASCADE)
    start_date = models.DateField()
    due_date = models.DateField()
    staff_responsible = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CapitalInvestment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.project.name


class Budget(models.Model):
    property_cost = models.DecimalField(max_digits=10, decimal_places=2)
    property_cost_monthly = models.DecimalField(max_digits=10, decimal_places=2)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    capital_investment = models.ManyToManyField(CapitalInvestment, related_name='investments')
    period_start = models.DateTimeField()
    period_end = models.DateTimeField()

    def __str__(self):
        return self.period_start.__str__() + '-' + self.period_end.__str__()


class Event(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    homestead = models.ForeignKey(Homestead, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.start_date.__str__() + ' ' + self.start_time.__str__() + ' ' + self.location.name + ' @ ' + self.homestead.name



