from django.urls import path
from session_api.views import SessionAPIView, SessionDetailAPIView, UserSessionAPIView, SessionTeamAPIView

urlpatterns = [
    path('', SessionAPIView.as_view(), name='sessions'),
    path('detail/<int:pk>/', SessionDetailAPIView.as_view(), name='session-detail'),
    path('user/<int:person_id>/', UserSessionAPIView.as_view(), name='user-sessions'),
    path('teams/', SessionTeamAPIView.as_view(), name='session-teams'),
]