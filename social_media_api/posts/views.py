from rest_framework import viewsets, permissions, status, generics, filters
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from notifications.models import Notification
from rest_framework.generics import get_object_or_404

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the author of the post
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            return Response({"detail": "You do not have permission to edit this post."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            return Response({"detail": "You do not have permission to delete this post."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the author of the comment
        post = Post.objects.get(pk=self.request.data['post'])
        serializer.save(author=self.request.user, post=post)

    def update(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user:
            return Response({"detail": "You do not have permission to edit this comment."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user:
            return Response({"detail": "You do not have permission to delete this comment."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
    

# --------------- #####################------------------------------#
#  Classes for the implementation of feeds for post of this social media app.
#----------------######################------------------------------#
class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        feed_data = [
            {
                "id": posts.id,
                "author": posts.author.username,
                "title": posts.title,
                "content": posts.content,
                "created_at": posts.created_at,
            }
            for post in posts
        ]
        return Response(feed_data)

class LikePostView(generics.GenericAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # Using the exact pattern "generics.get_object_or_404(Post, pk=pk)"
        post = generics.get_object_or_404(Post, pk=pk)

        # Add or update the like
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({'error': 'You already liked this post'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a notification for the like action
        Notification.objects.create(
            recipient=post.user,
            actor=request.user,
            verb='liked your post',
            target=post,
        )

        return Response({'message': 'Post liked successfully'}, status=status.HTTP_200_OK)

class UnlikePostView(generics.GenericAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # Using the exact pattern "generics.get_object_or_404(Post, pk=pk)"
        post = generics.get_object_or_404(Post, pk=pk)

        # Remove the like if it exists
        like = Like.objects.filter(user=request.user, post=post).first()
        if not like:
            return Response({'error': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({'message': 'Post unliked successfully'}, status=status.HTTP_200_OK)