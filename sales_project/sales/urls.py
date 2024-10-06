from django.urls import path
from .views import buyers_list, sellers_list, products_list, sales_list

urlpatterns = [
    path('buyers/', buyers_list, name='buyers_list'),
    path('sellers/', sellers_list, name='sellers_list'),
    path('products/', products_list, name='products_list'),
    path('sales/', sales_list, name='sales_list'),
]
from django.urls import path
from .views import (
    buyers_list,
    sellers_list,
    products_list,
    sales_list,
    add_buyer,
    add_seller,
    add_product,
    add_sale
)

urlpatterns = [
    path('buyers/', buyers_list, name='buyers_list'),
    path('buyers/add/', add_buyer, name='add_buyer'),
    path('sellers/', sellers_list, name='sellers_list'),
    path('sellers/add/', add_seller, name='add_seller'),
    path('products/', products_list, name='products_list'),
    path('products/add/', add_product, name='add_product'),
    path('sales/', sales_list, name='sales_list'),
    path('sales/add/', add_sale, name='add_sale'),
]
