from django.urls import path
from .views import (
    AthleteListView,
    AthleteDetailView,
)


urlpatterns = [
    path('', AthleteListView.as_view(), name='athlete-list'),
    path('<int:pk>/', AthleteDetailView.as_view(), name='athlete-detail'),
]
