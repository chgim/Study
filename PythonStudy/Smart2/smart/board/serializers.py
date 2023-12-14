from rest_framework import serializers

from .models import Post, Comment
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# class PostSerializer(serializers.ModelSerializer):    # ModelSerializer 쓰면 오버헤드 증가, 클래스에 강한 타입 의존.
#     class Meta:
#         model = Post
#         fields = "__all__"   # 안쓰면 ("Creating a ModelSerializer without either the 'fields' attribute or the 'exclude' attribute has been deprecated since 3.3.0, and is now disallowed. Add an explicit fields = '__all__' to the PostSerializer serializer.",)
#         # fields = ["id", "title"]


class PostListSerializer(serializers.Serializer):   # 타입만 명시 하는게 효율적.
    id = serializers.IntegerField(read_only=True)
    # user = serializers.SerializerMethodField()
    # user_id = serializers.IntegerField()
    user = serializers.CharField()  # models.py에서 user=models.ForeignKey...로 설정 되어 있음. user 가져올 때는 객체를 __str__로  문자열로 변환하여 가져옴. User 객체 따라가보면 __str__에서 get_username() 반환. 그래서 user의 이름 가져옴.
    title = serializers.CharField()
    comment_count = serializers.SerializerMethodField()
    tstamp = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    # preview = serializers.SerializerMethodField()
    preview = serializers.CharField()


    # def get_user(self, obj):
        # if obj.user is None:
        #     return {}
        # return {
        #     "id": obj.user.id,
        #     "username": obj.user.username
        # }

    # def get_preview(self, obj):
    #     if len(obj.content) > 10:
    #         return obj.content[:10] + "..."
    #     return obj.content

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
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)  # HiddenField.생성의 결과값으로 주진 않음.default가 키워드 인자 값으로 있어야 함.  : default is a required argument. CurrentUserDefault: context 안의 request 안에있는 user 사용. ['request'].user
    tstamp = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    def create(self, validated_data):
        # return Post.objects.create(title=validated_data["title"], content=validated_data["content"])
        return Post.objects.create(**validated_data)    # 딕셔너리 ** 언패킹 하면 key, value 값 

 
class CommentCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    # post_id = serializers.IntegerField()   
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())  # 예외처리 좋음. 게시글 리스트 쫙 뽑아오기 때문에 입력 범위의 제한을 걸 수 있음.queryset 안에서 데이터를 찾고 없으면 못넣음.
    content = serializers.CharField()
    tstamp = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)  


class CommentDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.CharField()
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