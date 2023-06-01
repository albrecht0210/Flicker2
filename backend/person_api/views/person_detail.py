from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from person_api.models import Person
from person_api.serializers import PersonSerializer

class PersonDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            person = Person.objects.filter(pk=pk)
            serializer = PersonSerializer(person, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            person = Person.objects.filter(pk=pk)
            serializer = PersonSerializer(person, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    