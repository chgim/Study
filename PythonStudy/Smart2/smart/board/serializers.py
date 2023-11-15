from rest_framework import serializers

from .models import Post


# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = "__all__"   # 안쓰면 ("Creating a ModelSerializer without either the 'fields' attribute or the 'exclude' attribute has been deprecated since 3.3.0, and is now disallowed. Add an explicit fields = '__all__' to the PostSerializer serializer.",)
#         # fields = ["id", "title"]

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    content = serializers.CharField()
    tstamp = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    def create(self, validated_data):
        # return Post.objects.create(title=validated_data["title"], content=validated_data["content"])
        return Post.objects.create(**validated_data)