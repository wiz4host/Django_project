from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)  #https://docs.djangoproject.com/en/2.1/ref/models/fields/#charfield
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    summary = models.TextField(default='This is cool')
    featured = models.BooleanField()


