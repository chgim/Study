from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path("^/posts$", views.PostList.as_view()),
    re_path("^/posts/comments$", views.CommentList.as_view()),
    path("/posts/<int:pk>", views.PostDetail.as_view()),
    path("/posts/comments/<int:pk>", views.CommentDetail.as_view()),
    # path("/posts/test", views.TestAPI.as_view())
]