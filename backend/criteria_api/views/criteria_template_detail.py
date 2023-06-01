from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from criteria_api.models import CriteriaTemplate
from criteria_api.serializers import CriteriaTemplateSerializer

class CriteriaTemplateDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            criteria_template = CriteriaTemplate.objects.filter(pk=pk)
            serializer = CriteriaTemplateSerializer(criteria_template, many=True)
            return Response(serializer.data)
        except CriteriaTemplate.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            criteria = CriteriaTemplate.objects.filter(pk=pk)
            serializer = CriteriaTemplateSerializer(criteria, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CriteriaTemplate.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)