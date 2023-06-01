from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from session_api.models import Session
from session_api.serializers import SessionSerializer

class UserSessionAPIView(APIView):
    def get(self, request, person_id):
        try:
            session = Session.objects.filter(host=person_id)
            serializer = SessionSerializer(session, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Session.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, person_id):
        try:
            session = Session.objects.filter(host=person_id)
            serializer = SessionSerializer(session, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Session.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    