from django.shortcuts import render

# Create your views here.\

from .models import Product
from .forms import ProductForm

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        "object": obj
    }
    return render(request, "db_details.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        print ("form is valid")
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "db_create.html", context)
