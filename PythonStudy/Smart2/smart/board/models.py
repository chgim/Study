from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=256,verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    def __str__(self):  # 게시글 생성시 게시글 리스트에 보여질 내용 제목으로
        return f"[{self.id}] {self.title}"
    
    class Meta:
        db_table="smart_board_post"
        verbose_name="게시글"
        verbose_name_plural="게시글"
