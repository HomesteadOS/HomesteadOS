import pytest
from django.core.exceptions import ValidationError
from home.models.role import Role
from home.models.role_classes import RoleClasses


def role_creation_with_valid_data():
    role_class = RoleClasses.objects.create(name="Test Role Class")
    role = Role.objects.create(
        name="Test Role",
        description="Test Description",
        email="test@example.com",
        role_class=role_class
    )
    assert role is not None


def role_string_representation():
    role_class = RoleClasses.objects.create(name="Test Role Class")
    role = Role.objects.create(
        name="Test Role",
        description="Test Description",
        email="test@example.com",
        role_class=role_class
    )
    assert str(role) == "Test Role"


def role_creation_with_invalid_email():
    with pytest.raises(ValidationError):
        role_class = RoleClasses.objects.create(name="Test Role Class")
        Role.objects.create(
            name="Test Role",
            description="Test Description",
            email="invalid_email",
            role_class=role_class
        )


def role_creation_without_role_class():
    with pytest.raises(models.IntegrityError):
        Role.objects.create(
            name="Test Role",
            description="Test Description",
            email="test@example.com"
        )
