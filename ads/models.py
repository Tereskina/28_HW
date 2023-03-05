from django.db import models

from users.models import User


class Category(models.Model):

    # slug = models.SlugField(max_length=50)
    name = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Ad(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User, verbose_name='Автор', related_name='ads', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=2000, null=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name



