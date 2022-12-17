from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

class ListCreatePostView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer