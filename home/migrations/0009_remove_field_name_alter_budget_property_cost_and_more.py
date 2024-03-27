# Generated by Django 5.0.3 on 2024-03-26 00:50

import django.core.validators
import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_event"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="field",
            name="name",
        ),
        migrations.AlterField(
            model_name="budget",
            name="property_cost",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(Decimal("0.01"))],
            ),
        ),
        migrations.AlterField(
            model_name="budget",
            name="property_cost_monthly",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(Decimal("0.01"))],
            ),
        ),
        migrations.AlterField(
            model_name="budget",
            name="salary",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(Decimal("0.01"))],
            ),
        ),
        migrations.AlterField(
            model_name="crop",
            name="yield_unit",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="home.yieldunits"
            ),
        ),
        migrations.AlterField(
            model_name="field",
            name="crop",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="home.crop"
            ),
        ),
        migrations.AlterField(
            model_name="staff",
            name="email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="staff",
            name="primary_location",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="home.location",
            ),
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.TextField()),
                ("datetime", models.DateTimeField()),
                ("scheduled", models.BooleanField(default=False)),
                ("scheduled_datetime", models.DateTimeField()),
                ("read", models.BooleanField(default=False)),
                (
                    "staff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.staff"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
                ("completed", models.BooleanField(default=False)),
                ("comment", models.TextField()),
                (
                    "homestead",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.homestead"
                    ),
                ),
                (
                    "staff_responsible",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.staff"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TaskList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("due_date", models.DateTimeField()),
                ("start_date", models.DateTimeField()),
                (
                    "homestead",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.homestead"
                    ),
                ),
                (
                    "staff_responsible",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.staff"
                    ),
                ),
                ("tasks", models.ManyToManyField(to="home.task")),
            ],
        ),
        migrations.CreateModel(
            name="TaskListLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("datetime", models.DateTimeField()),
                ("comment", models.TextField()),
                (
                    "staff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.staff"
                    ),
                ),
                (
                    "task_list",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.tasklist"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TaskListNotification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("datetime", models.DateTimeField()),
                ("read", models.BooleanField(default=False)),
                (
                    "staff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.staff"
                    ),
                ),
                (
                    "task_list",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.tasklist"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WorkLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
                ("comment", models.TextField()),
                (
                    "staff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.staff"
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.task"
                    ),
                ),
            ],
        ),
    ]
