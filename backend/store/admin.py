from django.contrib import admin
from store.models import Category, Product, Gallery, Specification, Size, Color, Cart, CartOrder, CartOrderItem, Review


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 1
    
class SpecificationInline(admin.TabularInline):
    model = Specification
    extra = 1
    
class SizeInline(admin.TabularInline):
    model = Size
    extra = 1
    
class ColorInline(admin.TabularInline):
    model = Color
    extra = 1
    

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'old_price', 'stock_qty', 'in_stock', 'status', 'featured', 'views', 'rating', 'vendor', 'pid', 'date']
    list_editable = ['price', 'old_price', 'stock_qty', 'in_stock', 'status', 'featured', 'vendor'] 
    list_filter = ['status', 'featured', 'in_stock', 'vendor']
    search_fields = ['title', 'description']
    inlines = [GalleryInline, SpecificationInline, SizeInline, ColorInline]

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'date']
    list_filter = ['rating']
    # search_fields = ['user']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

admin.site.register(Cart)
admin.site.register(CartOrder)
admin.site.register(CartOrderItem)

admin.site.register(Review, ReviewAdmin)
