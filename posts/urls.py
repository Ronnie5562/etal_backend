from django.urls import path
from .views import (
    PostListCreateView,
    PostDetailUpdateDeleteView,
    PostLikeView,
    PostCommentView
)

urlpatterns = [
    path(
        '',
        PostListCreateView.as_view(),
        name='post_list'
    ),
    path(
        '<int:pk>/',
        PostDetailUpdateDeleteView.as_view(),
        name='post_detail'
    ),
    path(
        '<int:post_id>/like/',
        PostLikeView.as_view(),
        name='post_like'
    ),
    path(
        '<int:post_id>/comment/',
        PostCommentView.as_view(),
        name='post_comment'
    ),
]
