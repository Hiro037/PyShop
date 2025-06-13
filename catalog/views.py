from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Products

def home(request):
    latest_products = Products.objects.order_by('-created_at')[:5]
    for product in latest_products:
        print(product)
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'GET':
        return render(request, 'contacts.html')
    if request.method == 'POST':
        return HttpResponse("Данные отправлены!")
