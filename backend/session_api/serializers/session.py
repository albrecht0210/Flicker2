from rest_framework import serializers
from session_api.models import Session
from person_api.serializers import PersonSerializer
from criteria_api.serializers import CriteriaTemplateSerializer
from .session_team import SessionTeamSerializer

class SessionSerializer(serializers.ModelSerializer):
    date_time = serializers.SerializerMethodField()
    type = serializers.CharField(source='get_type_display')
    status = serializers.CharField(source='get_status_display')
    
    def get_date_time(self, obj):
        return str(obj.date) + ' ' + str(obj.time)
    
    class Meta:
        model = Session
        fields = ['id', 'title', 'type', 'status', 'date', 'time', 'code', 'host', 'criteria_template', 'session_team', 'date_time']
