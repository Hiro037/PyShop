from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductsListView, ProductsDetailView, ProductsCreateView, ContactsFormView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view()),
    path('home/', ProductsListView.as_view(), name='home'),
    path('contacts/', ContactsFormView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductsDetailView.as_view(), name='product'),
    path('add_product/', ProductsCreateView.as_view(), name='add_product')
]