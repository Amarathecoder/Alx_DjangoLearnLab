from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=bool, null=False)
    """
    Extend Django's AbstractUser with additional fields
    """
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    # Many-to-many relationship for followers (users who follow this user)
    followers = models.ManyToManyField('self', symmetrical=False, related_name="followed_by", blank=True)

    # Many-to-many relationship for following (users this user is following)
    following = models.ManyToManyField('self', related_name='following_users', symmetrical=False, blank=True)

    def __str__(self):
        return self.username