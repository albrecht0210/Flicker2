from django.urls import path
from criteria_api.views import CriteriaAPIView, CriteriaDetailAPIView, CriteriaTemplateAPIView, CriteriaTemplateDetailAPIView

urlpatterns = [
    path('', CriteriaAPIView.as_view(), name='criterias'),
    path('detail/<int:pk>/', CriteriaDetailAPIView.as_view(), name='criteria-detail'),
    path('templates/', CriteriaTemplateAPIView.as_view(), name='criteria-templates'),
    path('templates/detail/<int:pk>/', CriteriaTemplateDetailAPIView.as_view(), name='criteria-templates-detail'),
]