from datetime import datetime
from django.db import models

# Create your models here.

# 기본키는 설정 안했음
# id(primary key)자동 생성된다. default_auto_field


class Board(models.Model):
    writer = models.CharField(null=False, max_length=50)
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


class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    writer = models.CharField(null=False, max_length=50)
    content = models.TextField(null=False)
    post_date = models.DateTimeField(default=datetime.now, blank=True)
