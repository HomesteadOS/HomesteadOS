import pytest
from django.core.exceptions import ValidationError
from home.models.homestead import Homestead
from home.models.staff import Staff
from home.models.project import Project


def project_creation_with_valid_data():
    homestead = Homestead.objects.create(name="Test Homestead")
    staff = Staff.objects.create(name="Test Staff")
    project = Project.objects.create(
        name="Test Project",
        description="Test Description",
        homestead=homestead,
        start_date="2022-01-01",
        due_date="2022-12-31",
        staff_responsible=staff
    )
    assert project is not None


def project_string_representation():
    homestead = Homestead.objects.create(name="Test Homestead")
    staff = Staff.objects.create(name="Test Staff")
    project = Project.objects.create(
        name="Test Project",
        description="Test Description",
        homestead=homestead,
        start_date="2022-01-01",
        due_date="2022-12-31",
        staff_responsible=staff
    )
    assert str(project) == "Test Project"


def project_creation_with_past_due_date():
    with pytest.raises(ValidationError):
        homestead = Homestead.objects.create(name="Test Homestead")
        staff = Staff.objects.create(name="Test Staff")
        Project.objects.create(
            name="Test Project",
            description="Test Description",
            homestead=homestead,
            start_date="2022-01-01",
            due_date="2021-12-31",
            staff_responsible=staff
        )


def project_creation_without_staff_responsible():
    with pytest.raises(models.IntegrityError):
        homestead = Homestead.objects.create(name="Test Homestead")
        Project.objects.create(
            name="Test Project",
            description="Test Description",
            homestead=homestead,
            start_date="2022-01-01",
            due_date="2022-12-31"
        )
