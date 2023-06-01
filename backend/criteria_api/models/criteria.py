from django.db import models

class Criteria(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name