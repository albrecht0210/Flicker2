from django.urls import path
from person_api.views import PersonAPIView, PersonDetailAPIView

urlpatterns = [
    path('', PersonAPIView.as_view(), name='persons'),
    path('detail/<int:pk>/', PersonDetailAPIView.as_view(), name='person-detail'),
]