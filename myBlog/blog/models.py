from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    """
    分类
    """
    name = models.CharField('名称', max_length=16)
    count = models.CharField('数量', max_length=10)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    标签
    """
    name = models.CharField('名称', max_length=16)

    def __str__(self):
        return self.name


class Blog(models.Model):
    """
    博客
    """
    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    content = RichTextUploadingField('正文')
    created = models.DateTimeField('发布时间', auto_now_add=True)
    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')

    def save(self, *args, **kwargs):
        super(Blog, self).save(*args, **kwargs)
        Categorys = Category.objects.all()
        for category in Categorys:
            category.count = Blog.objects.filter(category=category).count()
            category.save()

    def delete(self, using=None, keep_parents=False):
        super(Blog, self).delete(using=None, keep_parents=False)
        Categorys = Category.objects.all()
        for category in Categorys:
            category.count = Blog.objects.filter(category=category).count()
            category.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    评论
    """
    blog = models.ForeignKey(Blog, verbose_name='博客')
    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容', max_length=140)
    created = models.DateTimeField('发布时间', auto_now_add=True)

    def __str__(self):
        return self.content