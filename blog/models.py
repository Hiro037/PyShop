from django.db import models

class BlogPost(models.Model):
    # Модель поста для блога
    title = models.CharField(verbose_name='Заглавие', help_text='Введите заглавие поста')
    content = models.TextField(verbose_name='Содержание', help_text='Введите содержание поста')
    preview = models.ImageField(
        upload_to="BlogPosts-preview",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Добавьте фото продукта",
    )
    created_at = models.DateField(auto_now_add=True, verbose_name='Статус опубликования', help_text='Нажмите, если хотите опубликовать пост')
    is_published = models.BooleanField()
    views = models.IntegerField(verbose_name='Количество просмотров', help_text='Количество просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["title", "views", "is_published", "created_at"]