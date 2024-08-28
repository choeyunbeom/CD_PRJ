from django.db import models

# Create your models here.
class Region(models.Model):
    year = models.CharField("발생년도", max_length=4)    # 연도
    region = models.CharField("범죄장소", max_length=10)    # 설치지역
    category = models.CharField("범죄분류", max_length=200)     # 범죄분류
    cnt = models.IntegerField("발생건수")     # 범죄건수


class Place(models.Model):
    year = models.CharField("발생년도", max_length=4)    # 연도
    place = models.CharField("범죄장소", max_length=10)    # 범죄장소
    category = models.CharField("범죄분류",max_length=10)     # 범죄분류
    cnt = models.IntegerField("발생건수")     # 범죄건수


class TimeRange(models.Model):
    category = models.CharField("범죄분류",max_length=10)     # 범죄분류
    timerange = models.CharField("발생시간대", max_length=20)     # 범죄분류
    cnt = models.IntegerField("발생건수")     # 범죄건수

class Year(models.Model):
    year = models.CharField("발생년도", max_length=4)

class Post(models.Model):
    # user = models.ForeignKey("users.User", verbose_name="작성자", on_delete =models.CASCADE)
    # 유저 migrate 아직
    title = models.CharField("제목", max_length=20)
    content = models.TextField("내용", blank=False)
    image = models.ImageField("이미지", upload_to="post", blank=True)

    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField("댓글 내용")

    def __str__(self):
        return f"{self.post.title}의 댓글 (ID: {self.id})"

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    
    def __str__(self):
        return self.name
