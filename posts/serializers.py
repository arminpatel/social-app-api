from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'created_at']
        extra_kwargs = {'id': {'read_only': True},
                        'created_at': {'read_only': True}
                    }

    def create(self, validated_data):
        user = self.context['request'].user

        return Post.objects.create(created_by=user, **validated_data)