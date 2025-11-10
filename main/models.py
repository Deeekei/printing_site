from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name    
    

class Size(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    

class Product_size(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE,
                                related_name='product_size')
    size = models.ForeignKey('Size', on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.size.name} ({self.stock} в наличии) ({self.product.name})"


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products')
    color = models.BooleanField(default=False, verbose_name='Цветной')
    price = models.DecimalField(max_digits=10, decimal_places= 2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to= 'products/main/')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

