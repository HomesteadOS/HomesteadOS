import pytest
from django.contrib.gis.db import models
from home.models.capital_investment import CapitalInvestment
from home.models.project import Project


def capital_investment_creation_with_valid_data():
    project = Project.objects.create(name="Test Project")
    capital_investment = CapitalInvestment.objects.create(project=project, description="Test Description")
    assert capital_investment is not None


def capital_investment_string_representation():
    project = Project.objects.create(name="Test Project")
    capital_investment = CapitalInvestment.objects.create(project=project, description="Test Description")
    assert str(capital_investment) == "Test Project"


def capital_investment_creation_without_project():
    with pytest.raises(models.IntegrityError):
        CapitalInvestment.objects.create(description="Test Description")


def capital_investment_creation_without_description():
    project = Project.objects.create(name="Test Project")
    capital_investment = CapitalInvestment.objects.create(project=project)
    assert capital_investment.description == ""
