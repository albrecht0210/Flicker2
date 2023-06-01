from django.db import models
from criteria_api.models import CriteriaTemplate
from person_api.models import Person
from .session_team import SessionTeam

class Session(models.Model):
    STATUS_CHOICES = (
        (0, 'Pending'),
        (1, 'Ongoing'),
        (2, 'Ended'),
    )

    TYPE_CHOICES = (
        (0, 'Offline'),
        (1, 'Online'),
    )

    title = models.CharField(max_length=255)
    type = models.IntegerField(choices=TYPE_CHOICES)
    status = models.IntegerField(choices=STATUS_CHOICES)
    date = models.DateField()
    time = models.TimeField()
    code = models.CharField(max_length=10)
    host = models.ForeignKey(Person, on_delete=models.CASCADE)
    criteria_template = models.ForeignKey(CriteriaTemplate, on_delete=models.CASCADE)
    session_team = models.ForeignKey(SessionTeam, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_type_display(self):
        return dict(self.TYPE_CHOICES).get(self.type)

    def get_status_display(self):
        return dict(self.STATUS_CHOICES).get(self.status)