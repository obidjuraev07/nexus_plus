from django.contrib import admin

from .models import Category, Product, ProductImage, Image


class CategoryAdmin(admin.ModelAdmin):
    exclude = ['slug']

class ProductAdmin(admin.ModelAdmin):
    exclude = ['slug']



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Image)