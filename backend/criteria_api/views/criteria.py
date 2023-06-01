from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from criteria_api.models import Criteria
from criteria_api.serializers import CriteriaSerializer

class CriteriaAPIView(APIView):
    def get(self, request):
        criteria = Criteria.objects.all()
        serializer = CriteriaSerializer(criteria, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CriteriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)