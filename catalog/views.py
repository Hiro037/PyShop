from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from catalog.models import Products, Category
from catalog.forms import ProductForm

def home(request):
    # Главная
    products = Products.objects.all()
    context = {"products": products}
    return render(request, 'products_list.html', context)


def contacts(request):
    # Контакты
    if request.method == 'GET':
        return render(request, 'contacts.html')
    if request.method == 'POST':
        return HttpResponse("Данные отправлены!")


def product(request, pk):
    # Страницы для отдельного продукта
    product = get_object_or_404(Products, pk=pk)
    context = {'product': product}
    return render(request, 'product.html', context)

def add_product(request):
    # Страница для добавления товара
    if request.method == 'GET':
        # Рендерит саму страницу
        all_categories = Category.objects.all()
        context = {'categories': all_categories}
        return render(request, 'add_product.html', context)
    elif request.method == 'POST':
        # Принимает POST запросы
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():  # Проверяет корректность данных
            form.save()  # Сохраняет товар
            return redirect('catalog:home')  # Перенаправляет на Главную
        else:
            return HttpResponse("Некорректные данные")  # Уведомляет, если данные некорректны