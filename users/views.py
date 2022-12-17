from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status

from .models import UserFollowing

class FollowCreate(APIView):
    permission_class = [IsAuthenticated,]
    queryset = UserFollowing.objects.all();

    def post(self, request, *args, **kwargs):
        try:
            current_user = self.request.user
        except ValueError:
            return Response({'message': 'User not authenticated'}, status=status.HTTP_400_BAD_REQUEST)

        following_user = User.objects.get(pk=self.kwargs['following_id'])

        try:
            UserFollowing.objects.create(user=current_user, following_user=following_user)
            return Response({'message': 'User successfully followed'})
        except IntegrityError:
            return Response({'message': 'User is already followed'})