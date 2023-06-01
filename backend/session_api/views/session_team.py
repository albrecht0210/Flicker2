from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from session_api.models import SessionTeam
from session_api.serializers import SessionTeamSerializer

class SessionTeamAPIView(APIView):
    def get(self, request):
        session_team = SessionTeam.objects.all()
        serializer = SessionTeamSerializer(session_team, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SessionTeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)