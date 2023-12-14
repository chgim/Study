from django.db import models
from django.contrib.auth.models import User
from django.utils.functional import cached_property
# Create your models here.


class Post(models.Model):   # 객체, DB의 select 하는 매개체
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,  # 회원 탈퇴 시 삭제된 사용자입니다. 라고 남겨두기 위함. 
        null=True,
        blank=True,
        verbose_name="사용자",
    )
    title = models.CharField(max_length=256, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    # @property
    @cached_property    # property를 쓸때 매번 쓰는게 아니라 객체가 로드될 때 그때그때 cache에서 제공. 성능 향상.
    def preview(self):
        if len(self.content) > 10:
            return self.content[:10] + "..."
        return self.content

    def __str__(self):  # admin 게시글 생성시 게시글 리스트에 보여질 내용 제목으로. 문자열로 변경하지 않으면 <__main__.Post object at 0x10546654> 형식으로 나옴. 객체를 바로 출력 하더라도 제대로 보임. 객체를 문자열로 변환했을 때 보고 싶은 문자열 전달
        return f"[{self.id}] {self.title}"
    
    class Meta:    # migration 할 시 테이블 직접 명시
        db_table = "smart_board_post"
        verbose_name = "게시글"    # 지울 시 admin 페이지에서 Posts로 나옴. 직접 명시하여 보여주는 역할. 게시글s 로 나옴.
        verbose_name_plural = "게시글"  # 게시글s -> 게시글


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



