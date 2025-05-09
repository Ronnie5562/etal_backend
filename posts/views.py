from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import (
    Post,
    PostLike,
    PostComment
)
from .serializers import (
    PostSerializer,
    PostLikeSerializer,
    PostCommentSerializer
)
from .permissions import (
    IsOwnerOrReadOnly
)
from notifications.models import Notification



class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly
    ]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PostLikeView(generics.CreateAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        post = Post.objects.get(id=post_id)

        notifiation_sender_name = None

        if (post.user.profile.first_name and post.user.profile.last_name):
            notifiation_sender_name = f"{post.user.profile.first_name} {post.user.profile.last_name}"
        elif post.user.profile.first_name:
            notifiation_sender_name = post.user.profile.first_name
        elif post.user.profile.last_name:
            notifiation_sender_name = post.user.profile.last_name
        else:
            notifiation_sender_name = post.user.email

        Notification.objects.create(
            user=post.user,
            sender=self.request.user,
            title=f"{notifiation_sender_name} liked your post",
            message=f"{notifiation_sender_name} liked your post",
            type='post_like',
        )
        serializer.save(user=self.request.user, post=post)


class PostCommentView(generics.CreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        post = Post.objects.get(id=post_id)

        notifiation_sender_name = None

        if (post.user.profile.first_name and post.user.profile.last_name):
            notifiation_sender_name = f"{post.user.profile.first_name} {post.user.profile.last_name}"
        elif post.user.profile.first_name:
            notifiation_sender_name = post.user.profile.first_name
        elif post.user.profile.last_name:
            notifiation_sender_name = post.user.profile.last_name
        else:
            notifiation_sender_name = post.user.email

        Notification.objects.create(
            user=post.user,
            sender=self.request.user,
            title=f"{notifiation_sender_name} added a comment to your post",
            message=f"{notifiation_sender_name} added a comment to your post",
            type='post_comment',
        )

        serializer.save(user=self.request.user, post=post)
