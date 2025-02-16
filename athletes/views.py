from rest_framework import generics
from athletes.models import Athlete
from athletes.serializers import (
    AthleteListSerializer,
    AthleteDetailSerializer,
)
from .permissions import (
    IsAthleteProfileOrReadOnly
)
from rest_framework.permissions import (
    IsAuthenticated,
)


class AthleteListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Athlete.objects.all()
    serializer_class = AthleteListSerializer


class AthleteDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [
        IsAuthenticated,
        IsAthleteProfileOrReadOnly
    ]
    queryset = Athlete.objects.all()
    serializer_class = AthleteDetailSerializer
