from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    # changes the owner field to show the username instead of pk
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            # check if logged in user is following any other profiles
            # if logged in user is following another user, a follower 
            # object will be created with the user as the owner
            # (person following someone)
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            print(following)
            # returns instance or none
            return following.id if following else None
        # Returns None if the user isn't authenticated
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner', 'following_id',
            'posts_count', 'followers_count', 'following_count'
        ]