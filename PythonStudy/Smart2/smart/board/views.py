from rest_framework import mixins, generics
# from rest_framework.views import APIView
# from rest_framework.response import Response

from .models import Post, Comment
from .serializers import (
    PostCreateSerializer,
    PostListSerializer,
    PostDetailSerializer,
    CommentCreateSerializer,
    CommentDetailSerializer,
    )
from django.db.models import Q

# 의존성 주입
# mixins: 다중 상속이 되는 환경에서 핵심 기능을 미리 만들어서 그것을 상속만 받아서 활성화


class PostList(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
               ):    
    # serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.request.method == "post":
            return PostCreateSerializer
        
        return PostListSerializer

    def get_queryset(self):
        query = self.request.query_params.get("query")
        posts = (
            Post.objects.select_related("user")
            .prefetch_related("comment_set")
            .defer("content")
            .all()
            .order_by("-id")
        )
        if query:
            posts = posts.filter(
                Q(title__contains=query) | Q(content__contains=query)
                                 )
        return posts

    def get(self, request, *args, **kwargs):
        # print(request.user)
        # print(request.user.id)
        # print(request.user.is_authenticated)
        # if request.user.is_authenticated:
        return self.list(request, *args, **kwargs)
        # return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class PostDetail(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
               ):
    serializer_class = PostDetailSerializer

    def get_queryset(self):
        return Post.objects.prefetch_related("comment_set").all()    
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)  
    

class CommentList(
    mixins.CreateModelMixin, generics.GenericAPIView
               ):    
   
    def get_serializer_class(self):
        return CommentCreateSerializer
      
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class CommentDetail(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
               ):
    serializer_class = CommentDetailSerializer

    def get_queryset(self):
        return Comment.objects.all()    
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)  


# class PostList(APIView):

#     def post(self, request, *args, **kwargs):
#         title = request.data.get("title")
#         content = request.data.get("content")

#         if not title or not content:
#             return Response({"error": "No required parameters"}, status=status.HTTP_400_BAD_REQUEST,)

#         post = Post(title=title, content=content)
#         post.save()     # insert

#         data = PostSerializer(post).data

#         # return Response({
#         #     "id": post.id,
#         #     "title": post.title,
#         #     "content": post.content,
#         # },status=status.HTTP_201_CREATED)
        
#         return Response(data, status=status.HTTP_201_CREATED)

#     def get(self, request, *args, **kwargs):
#         page = request.query_params.get("page", 1)  # http://127.0.0.1:8000/api/board/posts?page=2
#         page = int(page)

#         query = request.query_params.get("query")
#         posts = Post.objects.all().order_by('-id')
#         # if query:
#         #     posts = posts.filter(title=query)
#         # if query:
#         #     posts = posts.filter(title__contains=query)
#         if query:
#             posts = posts.filter(
#                 Q(title__contains=query) | Q(content__contains=query)
#                                  )
#         total = posts.count()
#         posts = posts[10 * (page - 1) : 10 * page]   # 역순
#         # SELECT * FROM posts ORDER BY id DESC LIMIT 10 OFFSET 0;
#         # SELECT * FROM posts ORDER BY id DESC LIMIT 10 OFFSET 10;
#         data = PostSerializer(posts, many=True).data    # 여기서 데이터 접근 시에 sql 실행. many=True => 데이터가 여러개
#         # posts = [{'id': p.id,'title': p.title,'content': p.content,'tstamp': p.tstamp } for p in posts]
#         # return Response(posts)  # Object of type Post is not JSON serializable 객체는 직렬화가 안됨.
#         # return Response(data, status=status.HTTP_400_BAD_REQUEST)
#         return Response({
#             'total': total,
#             'results': data
#             }) 


# get(self, request, pk=1)
# class PostDetail(APIView):
#     def put(self, request, pk, *args, **kwargs):
#         # print(args, kwargs)
#         # print(request, ",", pk)
#         obj = Post.objects.get(pk=pk)
#         obj.title = request.data.get("title", obj.title)
#         obj.content = request.data.get("content", obj.content)
#         obj.save()
#         ser = PostSerializer(obj)
#         return Response(ser.data)

#     def delete(self, request, pk, *args, **kwargs):
#         # print(args, kwargs)
#         # print(request, ",", pk)
#         obj = Post.objects.get(pk=pk)
#         obj.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def get(self, request, pk, *args, **kwargs):
#         # print(args, kwargs)
#         # print(request, ",", pk)
#         obj = Post.objects.get(pk=pk)
#         # comments = Comment.objects.filter(post=obj)
#         # comments = obj.comment_set.all()
#         # print(dir(obj))
#         ser = PostSerializer(obj)
#         return Response(ser.data)


# class TestAPI(APIView):
#     def get(self, request, *args, **kwargs):
#         obj = Post.objects.prefetch_related("comment_set").all()
#         ser = PostSerializer(obj, many=True)
#         return Response(ser.data)