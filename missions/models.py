from django.db import models

from cats.models import Cat


class Target(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField()
    is_completed = models.BooleanField(default=False)
    mission = models.ForeignKey('Mission', on_delete=models.CASCADE, related_name='targets')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'mission'], name='Target should be unique for a mission')
        ]

    def __str__(self):
        return self.name


class Mission(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='missions', null=True)
    is_completed = models.BooleanField(default=False)
