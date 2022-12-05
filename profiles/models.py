from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    # blank = true, means that the field isn't required
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_f7y9cq'
    )

    class Meta:
        # - means reverse, so the profiles are returned in reverse order
        #  newest first
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    sender = User model
    instance = specific user
    created = boolean, whether the User has just been created

    If the User has been created, that user will have a profile created for 
    them
    """
    if created:
        Profile.objects.create(owner=instance)


# when a new user is created, the create_profile function is called
post_save.connect(create_profile, sender=User)
