from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from criteria_api.models import CriteriaTemplate
from criteria_api.serializers import CriteriaTemplateSerializer

class CriteriaTemplateAPIView(APIView):
    def get(self, request):
        criteria_template = CriteriaTemplate.objects.all()
        serializer = CriteriaTemplateSerializer(criteria_template, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CriteriaTemplateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)