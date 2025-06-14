from django.db import models
from unicodedata import category


class Products(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="products-images/",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Добавьте фото продукта",
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return (
            f"Товар {self.name} по цене {self.price}. Категория: {self.category}."
            f" Изображение: {self.image}. Создано: {self.created_at}. Последнее изменение: {self.updated_at}"
        )

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "price", "category", "created_at"]


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание категории"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]
