from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField('标签', max_length=32)


class Blog(models.Model):
    blogTitle = models.CharField('标题', max_length=32)
    blogAuthor = models.CharField('作者', max_length=16)
    blogReleasedTime = models.DateTimeField('发布时间', auto_now_add=True)
    blogContext = models.TextField('博客内容')
    tags = models.ManyToManyField(Tag, verbose_name='标签')


class Comment(models.Model):
    commentContext = models.TextField('评论内容', max_length=200)
    commentReleasedTime = models.DateTimeField('评论时间', auto_now_add=True)
    blog = models.ForeignKey(Blog, verbose_name='博客')
