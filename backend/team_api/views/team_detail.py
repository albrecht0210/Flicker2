from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from team_api.models import Team
from team_api.serializers import TeamSerializer

class TeamDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            team = Team.objects.filter(pk=pk)
            serializer = TeamSerializer(team, many=True)
            return Response(serializer.data)
        except Team.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            team = Team.objects.filter(pk=pk)
            serializer = TeamSerializer(team, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Team.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)