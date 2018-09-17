from django.shortcuts import render

# Create your views here.\

from .models import Product

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title': obj.title,
        'summary': obj.summary
    }
    return render(request, "db_details.html", context)
