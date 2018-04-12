from django.db import models
from user.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='类别')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Category表'


class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='标题')
    desc = models.CharField(max_length=500, verbose_name='描述')
    content = models.TextField(verbose_name='内容')
    createtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modifytime = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='类别')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Article表'
        # verbose_name = 'Article表'
