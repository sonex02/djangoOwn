from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # 设置性别在页面显示为汉字
    sex_choices = (
        (0, u'男'),
        (1, u'女'),
    )

    nickname = models.CharField(max_length=30,verbose_name='昵称')
    age = models.IntegerField(default=0,verbose_name='年龄')
    sex = models.IntegerField(default=0,verbose_name='性别')  # 0-男，1-女

    class Meta:
        ordering = ['username']     # 排序


