from django import forms
from catalog.models import Products
from django.core.exceptions import ValidationError
import os


class ContactsForm(forms.Form):
    # Форма для контактов
    fields = ["name", "number", "message"]


class ProductForm(forms.ModelForm):
    # Эта форма используется для добавления или изменения товаров на сайте
    class Meta:
        model = Products
        fields = ["name", "description", "image", "category", "price"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'name'
        self.fields["name"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Наименование товара",  # Текст подсказки внутри поля
            }
        )

        # Настройка атрибутов виджета для поля 'description'
        self.fields["description"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Описание товара",  # Текст подсказки внутри поля
                "type": "text",
            }
        )

        # Настройка атрибутов виджета для поля 'image'
        self.fields["image"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Вставьте изображение товара",  # Текст подсказки внутри поля
                "type": "image",
            }
        )

        # Настройка атрибутов виджета для поля 'category'
        self.fields["category"].widget.attrs.update(
            {
                "class": "form-select",  # Добавление CSS-класса для стилизации поля
            }
        )

        # Настройка атрибутов виджета для поля 'price'
        self.fields["price"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "type": "number",  # Указание типа поля как числа
                "placeholder": "Цена товара",
            }
        )

    def clean_price(self):
        # Валидация цены
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

    def clean_name(self):
        # Валидация имени
        banned_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        name = self.cleaned_data.get("name")
        if name:  # Проверяем, что name не None и не пустой
            for word in banned_words:
                if word in name.lower():  # Проверяем, содержится ли слово в name
                    raise ValidationError(
                        f'Нельзя использовать наименование со словом "{word}"'
                    )
        return name

    def clean_description(self):
        # Валидация описания
        banned_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        description = self.cleaned_data.get("description")
        if description:  # Проверяем, что description не None и не пустой
            for word in banned_words:
                if (
                    word in description.lower()
                ):  # Проверяем, содержится ли слово в description
                    raise ValidationError(
                        f'Нельзя использовать описание со словом "{word}"'
                    )
        return description

    def clean_image(self):
        # Валидация изображения
        image = self.cleaned_data.get("image")
        if image:
            # Допустимые расширения
            allowed_extensions = [".jpg", ".jpeg", ".png"]
            max_size = 5 * 1024 * 1024  # 5 МБ в байтах

            # Проверка расширения файла
            _, file_extension = os.path.splitext(image.name)
            file_extension = file_extension.lower()
            if file_extension not in allowed_extensions:
                raise ValidationError(
                    "Недопустимый формат файла. Разрешены только JPEG и PNG."
                )

            # Проверка размера файла
            if (
                image.size > max_size
            ):  # Сравнивает размера изображения (в байтах) с максимально разрешенным размером
                raise ValidationError(
                    f"Файл слишком большой. Максимальный размер: 5 МБ. Ваш файл: {image.size / (1024 * 1024):.2f} МБ."
                )

        return image
