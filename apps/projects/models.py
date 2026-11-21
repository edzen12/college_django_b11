from django.db import models
from apps.orientation.models import Tag


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название") 
    tags = models.ManyToManyField(Tag, verbose_name='Хештеги')
    desc = models.TextField(verbose_name="Описание")
    img = models.ImageField(upload_to='projects/', verbose_name="Фото")
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural="Проекты"
        verbose_name="проект"