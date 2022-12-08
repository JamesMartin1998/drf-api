from rest_framework import generics, permissions
from followers.models import Follower
from followers.serializers import FollowerSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class FollowerList(generics.ListCreateAPIView):
    # need to be authenticated to follow
    # anyone can view the followers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        """
        Sets the user performing the follow action
        as the owner of the follow
        """
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    # need to be the owner of a follow to delete it
    # anyone can see the detail
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
