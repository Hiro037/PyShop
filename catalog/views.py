from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from catalog.models import Products, Category
from catalog.forms import ContactsForm
from django.views.generic import ListView, DetailView, CreateView, FormView


class ProductsListView(ListView):
    # Главная страница со списком товаров
    model = Products


class ContactsFormView(FormView):
    # Страница для контактов
    form_class = ContactsForm
    template_name = 'catalog/contacts.html'
    success_url = reverse_lazy('catalog:home')


class ProductsDetailView(DetailView):
    # Страница отображает информацию об одном товаре
    model = Products


class ProductsCreateView(CreateView):
    # Страница создания товара
    model = Products
    fields = ['name', 'description', 'image', 'category', 'price']
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        all_categories = Category.objects.all()
        context = {'categories': all_categories}
        return context
