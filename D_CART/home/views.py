from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    dict_product = {'productDetails':Product.objects.all()}
    return render(request,'index.html',dict_product)
def product(request):
    return render(request,'product.html')