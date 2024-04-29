from django.db import models
from userauths.models import User, Profile
from vendor.models import Vendor
from shortuuid.django_fields import ShortUUIDField
from django.utils.text import slugify

# Model for Product Categories
class Category(models.Model):
    id = models.BigAutoField(help_text="Category ID", primary_key=True)
    # Category title
    title = models.CharField(max_length=100)
    # Image for the category
    image = models.FileField(upload_to="category", default="category.jpg", null=True, blank=True)
    # Is the category active?
    active = models.BooleanField(default=True)
    # Slug for SEO-friendly URLs
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Category"
        ordering = ["title"]
    
# Model for Products
class Product(models.Model):
    
    STATUS = (
        ("draft", "Draft"),
        ("disabled", "Disabled"),
        ("rejected", "Rejected"),
        ("in_review", "In Review"),
        ("published", "Published"),
    )  
    id = models.BigAutoField(help_text="Product ID", primary_key=True)
    # Product title
    title = models.CharField(max_length=100)
    # Image for the product
    image = models.FileField(upload_to="products", blank=True, null=True, default="product.jpg")
    # Description for the product using HTML
    description = models.TextField(null=True, blank=True)
    
    # Categories that the product belongs to
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    # Price of the product
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    shipping_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    stock_qty = models.PositiveIntegerField(default=0)
    in_stock = models.BooleanField(default=True)
    status = models.CharField(max_length=100, default="published", choices=STATUS)
    featured = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField(default=0)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True, related_name="Vendor")
    
    pid = ShortUUIDField(unique=True, length=10, alphabet="abcdefghijklmnopqrstuvxyz")
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug is None:
            self.slug = slugify(self.name)    
        super(Product, self).save(*args, **kwargs) 
        
    def __str__(self):
        return self.title
    
class Gallery(models.Model):
    id = models.BigAutoField(help_text="Gallery ID", primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField(upload_to="gallery", default="gallery.jpg")
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    gid = ShortUUIDField(unique=True, length=10, alphabet="abcdefghijklmnopqrstuvxyz")
    
    def __str__(self):
        return self.product.title
    
    class Meta:
        verbose_name_plural = "Product Images"
    
class Specification(models.Model):
    id = models.BigAutoField(help_text="Specification ID", primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Size(models.Model):
    id = models.BigAutoField(help_text="Size ID", primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Color(models.Model):
    id = models.BigAutoField(help_text="Color ID", primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
    