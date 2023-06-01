from django.db import models
from .criteria import Criteria

class CriteriaTemplate(models.Model):
    name = models.CharField(max_length=255)
    criterias = models.ManyToManyField(Criteria)

    def __str__(self):
        return self.name