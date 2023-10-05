from django.contrib import admin

from products.models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quintity', 'category')
    fields = ('name', 'description', 'price', 'quintity', 'image', 'category')
    search_fields = ('name', 'description')
    ordering = ('name', )


class BaskerAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', )
    extra = 0
