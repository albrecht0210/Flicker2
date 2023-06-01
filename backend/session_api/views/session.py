from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from session_api.models import Session
from session_api.serializers import SessionSerializer

class SessionAPIView(APIView):
    def get(self, request):
        session = Session.objects.all()
        serializer = SessionSerializer(session, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)