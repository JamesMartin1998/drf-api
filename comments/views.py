from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    # List - inheritance for get view
    # Create - inheritance for post view

    serializer_class = CommentSerializer
    # Don't want anonymous users to comment
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # Get all comments
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        """
        Check that comments are associated with users upon creation
        """
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    # only owner can update or delete a comment
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
    

