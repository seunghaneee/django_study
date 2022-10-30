from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10) # data type: VARCHAR(10)
    content = models.TextField() # data type: TEXT
    # 추가 모델 필드 작성 후 다시 makemigrations 진행
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
