from django.contrib import admin
from django.db.models import Model

from .models import Product


admin.site.register(Product)
# Register your models here.
