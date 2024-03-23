from django.contrib.gis.db import models

from home.models.homestead import Homestead
from home.models.staff import Staff


class Project(models.Model):
    """
    The Project model represents a project in the system.

    Attributes:
        name (CharField): The name of the project. This field is unique.
        description (TextField): A description of the project.
        homestead (ForeignKey): A foreign key that links to the Homestead model.
        start_date (DateField): The start date of the project.
        due_date (DateField): The due date of the project.
        staff_responsible (ForeignKey): A foreign key that links to the Staff model.
    """

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    homestead = models.ForeignKey(Homestead, on_delete=models.CASCADE)
    start_date = models.DateField()
    due_date = models.DateField()
    staff_responsible = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a string representation of the Project model.

        Returns:
            str: The name of the project.
        """
        return self.name
