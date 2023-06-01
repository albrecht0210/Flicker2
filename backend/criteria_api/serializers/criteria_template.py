from rest_framework import serializers
from criteria_api.models import CriteriaTemplate
from .criteria import CriteriaSerializer

class CriteriaTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CriteriaTemplate
        fields = ['name', 'criterias']