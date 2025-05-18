from django.urls import path
from .views import (
    ScoutListView,
    ScoutDetailView,
)


urlpatterns = [
    path('', ScoutListView.as_view(), name='Scout-list'),
    path('<int:pk>/', ScoutDetailView.as_view(), name='Scout-detail'),
]
