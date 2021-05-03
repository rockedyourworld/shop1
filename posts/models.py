from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='authors', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class PostTagModel(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post tag'
        verbose_name_plural = 'post tags'


class PostModel(models.Model):
    title = models.CharField(max_length=512)
    author = models.ForeignKey(
        AuthorModel,
        on_delete=models.PROTECT,
        related_name='posts'
    )
    image = models.ImageField('posts')
    banner = models.ImageField('banners')
    content = RichTextUploadingField()
    tags = models.ManyToManyField(
        PostTagModel,
        related_name='posts'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
