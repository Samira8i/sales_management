from django.contrib import admin
from .models import Buyer, Seller, Product, Sale

admin.site.register(Buyer)   # Регистрация модели покупателя
admin.site.register(Seller)   # Регистрация модели продавца
admin.site.register(Product)   # Регистрация модели товара
admin.site.register(Sale)      # Регистрация модели продажи
