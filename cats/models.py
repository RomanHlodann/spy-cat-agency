from django.db import models
from django.core.validators import MinValueValidator


class Cat(models.Model):
    name = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()
    breed = models.CharField(max_length=100)
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return self.name
