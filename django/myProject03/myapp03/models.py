from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# 기본키는 설정 안했음
# id(primary key)자동 생성된다. default_auto_field

#     writer = models.CharField(null=False, max_length=50)
# 보드의 writer를 왜래키로 잡고 유저와 관계를 잡을 것이다.
#    writer = models.ForeignKey(User, on_delete=models.CASCADE)

class Board(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(null=False, max_length=200)
    content = models.TextField(null=False)
    hit = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=datetime.now, blank=True)
    filename = models.CharField(
        null=False, max_length=500, blank=True, default='')
    filesize = models.IntegerField(default=0)
    down = models.IntegerField(default=0)

    def hit_up(self):
        self.hit += 1

    def down_up(self):
        self.down += 1

# board = models.ForeignKey(Board,on_delete=models.CASCADE)
# 조인하는 방식으로 왜래키 설정

# 댓글
# writer = models.CharField(null=False, max_length=50) 왜래키 설정으로 변경할것임


class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    post_date = models.DateTimeField(default=datetime.now, blank=True)

# 날씨


class Forecast(models.Model):
    city = models.CharField(null=False, max_length=50)
    tmef = models.TextField(null=True)
    wf = models.TextField(null=True)
    tmn = models.IntegerField(default=0)
    tmx = models.IntegerField(default=0)
