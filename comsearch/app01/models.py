from django.db import models


class Category(models.Model):
    caption = models.CharField(max_length=64)


class Article_type(models.Model):
    caption = models.CharField(max_length=64)


class Article(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=256)
    category = models.ForeignKey(to='Category',on_delete=True)
    article_type = models.ForeignKey(to='Article_type',on_delete=True)