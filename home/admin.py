from django.contrib import admin
from .models.budget import Budget
from .models.capital_investment import CapitalInvestment
from .models.crop import Crop
from .models.event import Event
from .models.expense import Expense
from .models.expense_classification import ExpenseClassification
from .models.field import Field
from .models.homestead import Homestead
from .models.location import Location
from .models.notification import Notification
from .models.project import Project
from .models.role import Role
from .models.role_classes import RoleClasses
from .models.staff import Staff
from .models.yield_units import YieldUnits
from .models.supplier import Supplier
from .models.task import Task
from .models.task_list import TaskList
from .models.task_list_log import TaskListLog
from .models.task_list_notification import TaskListNotification
from .models.work_log import WorkLog

# Register your models here.
admin.site.register(Homestead)
admin.site.register(Location)
admin.site.register(Staff)
admin.site.register(Role)
admin.site.register(RoleClasses)
admin.site.register(YieldUnits)
admin.site.register(Crop)
admin.site.register(Field)
admin.site.register(Project)
admin.site.register(Event)
admin.site.register(Expense)
admin.site.register(ExpenseClassification)
admin.site.register(Supplier)
admin.site.register(Task)
admin.site.register(TaskList)
admin.site.register(TaskListLog)
admin.site.register(TaskListNotification)
admin.site.register(WorkLog)
admin.site.register(Notification)
admin.site.register(Budget)
admin.site.register(CapitalInvestment)
