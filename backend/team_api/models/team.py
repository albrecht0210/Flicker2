from django.db import models
from person_api.models import Person

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(Person)

    def __str__(self):
        return self.name