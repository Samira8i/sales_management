from django.shortcuts import render
from .models import Buyer, Seller, Product, Sale

def buyers_list(request):
    buyers = Buyer.objects.all()
    return render(request, 'sales/buyers_list.html', {'buyers': buyers})

def sellers_list(request):
    sellers = Seller.objects.all()
    return render(request, 'sales/sellers_list.html', {'sellers': sellers})

def products_list(request):
    products = Product.objects.all()
    return render(request, 'sales/products_list.html', {'products': products})

def sales_list(request):
    sales = Sale.objects.all()
    return render(request, 'sales/sales_list.html', {'sales': sales})



from django.shortcuts import render, redirect
from .forms import BuyerForm, SellerForm, ProductForm, SaleForm

# Функция для добавления покупателя
def add_buyer(request):
    if request.method == 'POST':
        form = BuyerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buyers_list')
    else:
        form = BuyerForm()
    return render(request, 'sales/add_buyer.html', {'form': form})

# Функция для добавления продавца
def add_seller(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sellers_list')
    else:
        form = SellerForm()
    return render(request, 'sales/add_seller.html', {'form': form})

# Функция для добавления товара
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = ProductForm()
    return render(request, 'sales/add_product.html', {'form': form})

# Функция для добавления продажи
def add_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales_list')
    else:
        form = SaleForm()
    return render(request, 'sales/add_sale.html', {'form': form})
from django.shortcuts import render

def home(request):
    return render(request, 'sales/home.html')  # Убедитесь, что этот шаблон существует
