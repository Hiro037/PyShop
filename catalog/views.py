from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from catalog.models import Products, Category
from catalog.forms import ContactsForm, ProductForm, ProductModeratorForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    FormView,
    UpdateView,
    DeleteView,
)


class ProductsListView(ListView):
    # Главная страница со списком товаров
    model = Products


class ContactsFormView(FormView):
    # Страница для контактов
    form_class = ContactsForm
    template_name = "catalog/contacts.html"
    success_url = reverse_lazy("catalog:home")


class ProductsDetailView(LoginRequiredMixin, DetailView):
    # Страница отображает информацию об одном товаре
    model = Products


class ProductsCreateView(LoginRequiredMixin,CreateView):
    # Страница создания товара
    model = Products
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_categories = Category.objects.all()
        context["categories"] = all_categories
        return context

    def form_valid(self, form_class):
        product = form_class.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form_class)


class ProductsUpdateView(LoginRequiredMixin,UpdateView):
    model = Products
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_categories = Category.objects.all()
        context["categories"] = all_categories
        return context

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        if user == self.object.owner:
            return ProductForm
        raise PermissionError


class ProductsDeleteView(LoginRequiredMixin,DeleteView):
    model = Products
    success_url = reverse_lazy("catalog:home")
