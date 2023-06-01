from django.urls import path
from team_api.views import TeamAPIView, TeamDetailAPIView

urlpatterns = [
    path('', TeamAPIView.as_view(), name='teams'),
    path('detail/<int:pk>/', TeamDetailAPIView.as_view(), name='team-detail'),
]