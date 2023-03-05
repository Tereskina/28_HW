from django.db import models


class Ads(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.CharField(max_length=2000, null=True)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.name


class Categories(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.SlugField(max_length=100)
    #
    # def __str__(self):
    #     return self.name