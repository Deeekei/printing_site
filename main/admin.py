from django.contrib import admin
from .models import Product, Product_size, Size, Category

# Register your models here.
class ProductSizeInline(admin.TabularInline):
    model = Product_size
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price','color']
    list_filter = ['category', 'price']
    search_fields = ['name', 'category']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductSizeInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Product, ProductAdmin)        
