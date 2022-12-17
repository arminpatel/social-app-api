from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserFollowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="following")
    following_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="followers")