from rest_framework import serializers

from .models import Post, Comment
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = "__all__"   # 안쓰면 ("Creating a ModelSerializer without either the 'fields' attribute or the 'exclude' attribute has been deprecated since 3.3.0, and is now disallowed. Add an explicit fields = '__all__' to the PostSerializer serializer.",)
#         # fields = ["id", "title"]


class PostListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    comment_count = serializers.SerializerMethodField()
    tstamp = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    def get_comment_count(self, obj):
        return obj.comment_set.count()
      
    
class PostDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    content = serializers.CharField()
    comments = serializers.SerializerMethodField()
    tstamp = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    def get_comments(self, obj):
        comments = obj.comment_set.all()
        return [
            {
                "id": c.id,
                "content": c.content,
                "tstamp": c.tstamp.strftime("%Y-%m-%d %H:%M:%S"),
            }
            for c in comments
            ]

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance


class PostCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    content = serializers.CharField()
    tstamp = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    def create(self, validated_data):
        # return Post.objects.create(title=validated_data["title"], content=validated_data["content"])
        return Post.objects.create(**validated_data)
    

class CommentCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    # post_id = serializers.IntegerField()   
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())  # 예외처리 좋음.
    content = serializers.CharField()
    tstamp = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)  


class CommentDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.CharField()
    tstamp = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    def get_post_id(self, obj):
        return obj.post_id
    
    def update(self, instance, validated_data):  
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance  
    

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token