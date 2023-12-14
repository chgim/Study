from django.apps import AppConfig


class BoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = "게시판"  # 앱 이름을 board-> 게시판으로 지정
    name = 'board'
