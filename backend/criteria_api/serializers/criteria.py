from rest_framework import serializers
from criteria_api.models import Criteria

class CriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteria
        fields = ['name', 'percentage']