from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Название категории"
    )
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'категория'


class Tag(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Название хештега"
    )
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'тег'


class Orient(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, 
        verbose_name='Категория'
    )
    tags = models.ManyToManyField(Tag, verbose_name='Хештеги')
    img = models.ImageField(
        upload_to='orient/',  verbose_name="Фото",
        blank=True, null=True
    )
    title = models.CharField(max_length=100, verbose_name="Название")
    desc = models.TextField(verbose_name="Короткое описание", null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Направления'
        verbose_name = 'направление'