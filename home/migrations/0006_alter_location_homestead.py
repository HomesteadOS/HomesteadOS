# Generated by Django 4.1.5 on 2023-02-03 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_expense_debt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='homestead',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='home.homestead'),
        ),
    ]
