from catalog.models import Products, Category
from config.settings import CACHE_ENABLED
from django.core.cache import cache


def get_products_from_cache():
    # Функция возвращает список продуктов из кеша, если он там есть, и кеширует список из базы данных, если его там нет
    if not CACHE_ENABLED:
        return Products.objects.all()
    key = 'products_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Products.objects.all()
    cache.set(key,products)
    return products

def get_products_by_category(self, **kwargs):
    # Функция возвращает список продуктов, профильтрованный по категории
    category_id = self.kwargs.get('pk')
    category = Category.objects.get(pk=category_id)
    products = Products.objects.filter(category=category)
    context = {}
    context['products'] = products
    context['category_name'] = category.name
    all_categories = Category.objects.all()
    context["categories"] = all_categories
    return context

def add_categories_to_context(self, **kwargs):
    # Функция создает контекст, включающий все продукты и все категории
    context = {}
    products = Products.objects.all()
    all_categories = Category.objects.all()
    context['products'] = products
    context["categories"] = all_categories
    print(context)
    return context