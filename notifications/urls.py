from django.urls import path
from .views import (
    NotificationListAPIView,
    NotificationDetailAPIView,
    NotificationUpdateAPIView
)

urlpatterns = [
    path(
        '',
        NotificationListAPIView.as_view(),
        name='notification_list'
    ),
    path(
        '<int:pk>/',
        NotificationDetailAPIView.as_view(),
        name='notification_detail'
    ),
    path(
        '<int:pk>/update/',
        NotificationUpdateAPIView.as_view(),
        name='notification_update'
    ),
]
