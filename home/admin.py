from django.contrib import admin
from .models.budget import Budget
from .models.capital_investment import CapitalInvestment
from .models.crop import Crop
from .models.event import Event
from .models.field import Field
from .models.homestead import Homestead
from .models.location import Location
from .models.role import Role
from .models.role_classes import RoleClasses
from .models.staff import Staff
from .models.yield_units import YieldUnits

# Register your models here.
admin.site.register(Homestead)
admin.site.register(Location)
admin.site.register(Staff)
admin.site.register(Role)
admin.site.register(RoleClasses)
admin.site.register(YieldUnits)
admin.site.register(Crop)
admin.site.register(Field)