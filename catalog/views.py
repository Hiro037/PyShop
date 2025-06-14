from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Products

def home(request):
    products = Products.objects.all()
    context = {"products": products}
    return render(request, 'products_list.html', context)


def contacts(request):
    if request.method == 'GET':
        return render(request, 'contacts.html')
    if request.method == 'POST':
        return HttpResponse("Данные отправлены!")


def product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    context = {'product': product}
    return render(request, 'product.html', context)