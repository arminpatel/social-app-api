from django.db import models
from django.contrib.auth.models import User

# user follows following_user
class UserFollowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="following")
    following_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="followers")

    class Meta:
        unique_together = [['user'], ['following_user']]