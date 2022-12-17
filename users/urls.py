
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import FollowCreate, FollowDelete

urlpatterns = [
    path('authenticate/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('follow/<int:following_id>/', FollowCreate.as_view(), name='follow'),
    path('unfollow/<int:following_id>/', FollowDelete.as_view(), name='unfollow')
]