from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
from .models import Post
from .serializers import PostSerializer


class PostList(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-id')  # 역순
        data = PostSerializer(posts, many=True).data
        # posts = [{'id': p.id,'title': p.title,'content': p.content,'tstamp': p.tstamp } for p in posts]
        # return Response(posts)  # Object of type Post is not JSON serializable 객체는 직렬화가 안됨.
        # return Response(data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data)