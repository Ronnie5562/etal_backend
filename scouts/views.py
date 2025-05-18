from rest_framework import generics
from scouts.models import Scout
from scouts.serializers import (
    ScoutListSerializer,
    ScoutDetailSerializer,
)
from .permissions import (
    IsScoutProfileOrReadOnly
)
from rest_framework.permissions import (
    IsAuthenticated,
)


class ScoutListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Scout.objects.all()
    serializer_class = ScoutListSerializer


class ScoutDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [
        IsAuthenticated,
        IsScoutProfileOrReadOnly
    ]
    queryset = Scout.objects.all()
    serializer_class = ScoutDetailSerializer
