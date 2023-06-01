from rest_framework import serializers
from session_api.models import SessionTeam
from team_api.serializers import TeamSerializer

class SessionTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionTeam
        fields = ['id', 'teams']