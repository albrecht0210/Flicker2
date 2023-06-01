from rest_framework import serializers
from team_api.models import Team
from person_api.serializers import PersonSerializer

class TeamSerializer(serializers.ModelSerializer):
    # members = PersonSerializer(many=True)
    class Meta:
        model = Team
        fields = ['name', 'members']