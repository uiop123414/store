from django.contrib import admin

from products.models import ProductCategory, Product, Basket , History

# Register your models here.

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category')
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity',  #'created_timestamp'
               )
    extra = 0

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('product','quantity','type','price')
    fields = ('product',('quantity','type'),'price','user',)
