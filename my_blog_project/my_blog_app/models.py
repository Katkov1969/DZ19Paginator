from django.db import models

# Create your models here.

class Post(models.Model):
    """Модель, представляющая пост блога."""
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self) -> str:
        return self.title
