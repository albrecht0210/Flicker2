from django.db import models
from team_api.models import Team

class SessionTeam(models.Model):
    teams = models.ManyToManyField(Team)