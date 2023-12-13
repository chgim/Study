from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="사용자",
    )
    title = models.CharField(max_length=256, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    def __str__(self):  # 게시글 생성시 게시글 리스트에 보여질 내용 제목으로
        return f"[{self.id}] {self.title}"
    
    class Meta:
        db_table = "smart_board_post"
        verbose_name = "게시글"
        verbose_name_plural = "게시글"


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="사용자",
    )
    post = models.ForeignKey(
        "board.Post",
        on_delete=models.CASCADE,
        verbose_name="게시글",
    )
    content = models.TextField(verbose_name="내용")
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    def __str__(self): 
        return f"[{self.id}] {self.content[:10]}..."
    
    class Meta:
        db_table = "smart_board_post_comment"
        verbose_name = "댓글"
        verbose_name_plural = "댓글"



