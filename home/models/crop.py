from decimal import Decimal
from django.contrib.gis.db import models
from django.forms import ValidationError
from django.utils import timezone
from django.core.validators import MinValueValidator

from home.models.yield_units import YieldUnits


class Crop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    plant_date = models.DateTimeField()
    plant_target_date = models.DateTimeField(null=True, blank=True)
    harvest_date = models.DateTimeField()
    harvest_target_date = models.DateTimeField()
    yield_goal = models.DecimalField(validators=[MinValueValidator(Decimal('0.00'))], max_digits=10, decimal_places=2, default=Decimal('0.00'))
    yield_unit = models.ForeignKey(YieldUnits, on_delete=models.PROTECT)
    yield_actual = models.DecimalField(validators=[MinValueValidator(Decimal('0.00'))], max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return self.name

    def clean(self, *args, **kwargs):
        if (self.yield_actual < Decimal('0.00') 
            or self.yield_goal < Decimal('0.00') 
            or self.harvest_date < self.plant_date
            or self.harvest_target_date < self.plant_date
            or self.plant_date < timezone.now()):
            raise ValidationError(f"Crop data. Please check your input. {self}")
        super(Crop, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Crop, self).save(*args, **kwargs)