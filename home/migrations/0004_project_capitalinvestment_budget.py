# Generated by Django 4.1.5 on 2023-01-17 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_expenseclassification_supplier_expense'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('due_date', models.DateField()),
                ('homestead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.homestead')),
                ('staff_responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.staff')),
            ],
        ),
        migrations.CreateModel(
            name='CapitalInvestment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.project')),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('property_cost_monthly', models.DecimalField(decimal_places=2, max_digits=10)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('period_start', models.DateTimeField()),
                ('period_end', models.DateTimeField()),
                ('capital_investment', models.ManyToManyField(related_name='investments', to='home.capitalinvestment')),
            ],
        ),
    ]
