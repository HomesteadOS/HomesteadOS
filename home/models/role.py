from django.contrib.gis.db import models
from home.models.role_classes import RoleClasses


class Role(models.Model):
    """
    The Role model represents a role that a user can have in the system.

    Attributes:
        name (CharField): The name of the role. This field is unique.
        description (TextField): A description of the role.
        email (EmailField): An email associated with the role.
        role_class (ForeignKey): A foreign key that links to the RoleClasses model.
    """

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    email = models.EmailField()
    role_class = models.ForeignKey(RoleClasses, on_delete=models.PROTECT)

    def __str__(self):
        """
        Returns a string representation of the Role model.

        Returns:
            str: The name of the role.
        """
        return self.name
