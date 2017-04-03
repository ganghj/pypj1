from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("제목", max_length=100)
    slug = models.SlugField("Slug", unique=True)
    description = models.CharField("설명", max_length=200 , blank=True)
    contents = models.TextField("본문")
    create_date = models.DateTimeField("작성일시", auto_now_add=True)
    modify_date = models.DateTimeField("수정일시", auto_now=True)

    def _str_(self):
        return self.title
