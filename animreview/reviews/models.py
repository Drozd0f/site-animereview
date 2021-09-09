from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from pytils.translit import slugify
# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/", blank=True, verbose_name='Аватар')
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    #
    # def get_absolute_url(self):
    #     return reverse('user', kwargs={'user_slug': self.slug})


class Posts(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    text = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", verbose_name="Фото")
    rating = models.IntegerField(blank=True, verbose_name="Рейтинг")
    universe = models.ForeignKey('Universe', on_delete=models.PROTECT, verbose_name="Вселенная")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name="Пользователь")
    genre = models.ManyToManyField('Genre', verbose_name="Жанры")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Posts, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Посты"
        verbose_name_plural = "Посты"
        ordering = ['title']


class Genre(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Жанр")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre', kwargs={'genre_id': self.pk})

    class Meta:
        verbose_name = "Жанры"
        verbose_name_plural = "Жанры"


class Universe(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вселенные"
        verbose_name_plural = "Вселенные"





