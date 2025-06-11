from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def contacts(request):
    if request.method == 'GET':
        return render(request, 'contacts.html')
    if request.method == 'POST':
        return HttpResponse("Данные отправлены!")
