from django.apps import AppConfig


class BoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name="게시판"
    name = 'board'
