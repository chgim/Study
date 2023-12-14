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
# FBV Functional Based View (X)
# CBV Class Based View (O)


class PostList(     # 비즈니스 로직과 직렬화 과정을 분리하여 깔끔해짐.
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
               ):    
    # serializer_class = PostSerializer

    def get_serializer_class(self):     # GenericAPIView -> get_serializer_class
        if self.request.method == "POST":
            return PostCreateSerializer
        
        return PostListSerializer

    def get_queryset(self):
        query = self.request.query_params.get("query")
        posts = (
            Post.objects.select_related("user")
            .prefetch_related("comment_set")
            # .defer("content")
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
               ):   # 의존성 주입. mixin. 모양만 만들어 놓고 끼워넣음.재사용성 증가.
    serializer_class = PostDetailSerializer

    def get_queryset(self):
        return Post.objects.prefetch_related("comment_set").all()    
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):    # partial_update:  부분적으로 수정. 실제로 업데이트 된 부분만.
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

#     def get(self, request, *args, **kwargs):  # 객체는 기본적으로 직렬화 Serializable 불가능. JSON 형태로 바꿔 줘야함. 객체를 가져와서 필드를 재정의 하는 과정. 직렬화는 불필요한 과정. 따라서 Serializer 사용.객체를 JSON 타입으로 바꾸잖아.
#         page = request.query_params.get("page", 1)  # http://127.0.0.1:8000/api/board/posts?page=2
#         page = int(page)

#         query = request.query_params.get("query")
#         posts = Post.objects.all().order_by('-id')    #  QuerySet. 데이터에 실제로 접근 할 때 작동 됨.어떤 방식으로 데이터 접근 할건지 전달. 결국 쿼리를 반영하고 데이터에 접글할 때 실행.가지고 있는 필드 다 가져와라. id 오름차순 으로. QuerySet 이란 데이터베이스에서 전달 받은 객체의 목록이다.
#         # if query:
#         #     posts = posts.filter(title=query)
#         # if query:
#         #     posts = posts.filter(title__contains=query) # contains-> select ? from ? where ? like '%?%'
#         if query:
#             posts = posts.filter(
#                 Q(title__contains=query) | Q(content__contains=query)
#                                  )
#         total = posts.count()
#         posts = posts[10 * (page - 1) : 10 * page]   # 역순
#         # SELECT * FROM posts ORDER BY id DESC LIMIT 10 OFFSET 0;
#         # SELECT * FROM posts ORDER BY id DESC LIMIT 10 OFFSET 10;
#         data = PostSerializer(posts, many=True).data    # 쿼리셋 가져온것을 직렬화. 여기서 데이터 접근 시에 sql 실행. many=True => 데이터가 여러개. 쿼리셋에서 데이터 조작해도 상관 x
#         # posts = [{'id': p.id,'title': p.title,'content': p.content,'tstamp': p.tstamp } for p in posts]
#         # return Response(posts)  # Object of type Post is not JSON serializable 객체는 직렬화가 안됨.
#         # return Response(data, status=status.HTTP_400_BAD_REQUEST)   # 상태 코드를 바꾸고 싶을 경우 정의
#         return Response({ # Response-> 상태 코드 들어가 있기 때문에 분리.
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
#         # comments = Comment.objects.all()
#         # comments = Comment.objects.select_related("post").all() # 조인을 해서 가져옴. 쿼리가 하나로 해결 됨.
#         # return Response(
#         #     [
#         #         {
#         #             "id": comment.id,
#         #             "content": comment.comment,
#         #             "post": {
#         #                 "id": comment.post.id,
#         #                 "content": comment.post.comtent
#         #             },
#         #         }

#         #     ]
#         #     for comment in comments 
#         # )
#         obj = Post.objects.prefetch_related("comment_set").all()  # prefetch_related를 안해주면 댓글이 많을 시 쿼리 여러개가 동시에 실행됨.
#         ser = PostSerializer(obj, many=True)
#         return Response(ser.data)


# select_related:

# 목적: 관련된 객체에 대한 데이터베이스 쿼리 수를 줄이는 것.
# 동작 방식: SQL 조인을 생성하고 SELECT 문에 관련된 객체의 필드를 포함시켜 동작한다. 따라서 select_related는 관련된 객체를 동일한 데이터베이스 쿼리에서 가져온다.
# 제한: select_related는 외래 키 및 일대일 관계와 같은 단일 값 관계에 대해서만 지원된다. 'many' 관계를 횡단하는 조인을 피하기 위해 제한되어 있다.


# prefetch_related:

# 목적: 각 관계에 대해 별도의 조회를 수행하고 Python에서 '조인'을 수행함으로써 데이터베이스 쿼리 수를 최적화하는 것.
# 동작 방식: 각 관계에 대해 별도의 조회를 수행하고 '조인' 작업을 Python에서 처리한다. 이로써 select_related에서 지원하지 않는 다대다, 다대일, GenericRelation 등의 객체를 미리 가져올 수 있다.
# 제한: GenericForeignKey를 지원하긴 하지만, 결과의 일관된 세트로 제한되어야 한다. 예를 들어, GenericForeignKey를 사용하여 참조된 객체를 미리 가져오려면 쿼리가 하나의 ContentType으로 제한되어야 한다.

# 정리
# select_related는 SQL 조인을 사용하여 쿼리를 최적화하는 반면,
# prefetch_related는 별도의 쿼리를 수행하고 그 결과를 Python에서 처리함으로써 최적화를 달성합니다.
# 각각의 장단점이 있으며, 상황에 따라 어떤 것을 사용할지 결정해야 합니다.
# 일반적으로는 select_related가 단일 값 관계에 적합하고, prefetch_related는 여러 값 관계와 GenericRelation 등에 적합하다고 할 수 있습니다.


# values() 메소드:

# 목적: 특정 필드의 값을 가져오고 각 결과를 딕셔너리 형태로 표현.
# 동작 방식: 지정한 필드의 값을 갖는 딕셔너리를 반환하며, 각 딕셔너리는 데이터베이스 테이블의 한 행에 해당한다.
# 예시:
# python
# Copy code
# queryset = MyModel.objects.values('field1', 'field2')
# # [{'field1': 'value1', 'field2': 'value2'}, ...]

# values_list() 메소드:

# 목적: 특정 필드의 값을 가져오고 각 결과를 튜플 형태로 표현.
# 동작 방식: 지정한 필드의 값을 갖는 튜플을 반환하며, 각 튜플은 데이터베이스 테이블의 한 행에 해당한다.
# 예시:
# python
# Copy code
# queryset = MyModel.objects.values_list('field1', 'field2')
# # [('value1', 'value2'), ...]

# only() 메소드:

# 목적: 모델의 특정 필드만 가져옴.
# 동작 방식: 다른 필드는 무시되고, 지정한 필드만 가져온다.
# 예시:
# python
# Copy code
# queryset = MyModel.objects.only('field1', 'field2')
# # [{'field1': 'value1', 'field2': 'value2'}, ...]

# defer() 메소드:

# 목적: 특정 필드를 가져오지 않음 (지연 로딩).
# 동작 방식: 모델의 나머지 필드는 가져오지만, 지정한 필드는 나중에 필요할 때 따로 가져온다. 지연 로딩은 필드가 처음으로 액세스될 때 발생한다.
# 예시:
# python
# Copy code
# queryset = MyModel.objects.defer('field1', 'field2')
# # [{'non_deferred_field': 'value', 'deferred_field1': 'deferred_value1', 'deferred_field2': 'deferred_value2'}, ...]
# # 'field1'과 'field2'는 처음 액세스될 때 가져옴