from django.urls import re_path

from . import views

urlpatterns = [
    re_path("^/posts$", views.PostList.as_view())
]