from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria', 'activo')
    search_fields = ('nombre', 'categoria')
    list_filter = ('activo', 'categoria')
