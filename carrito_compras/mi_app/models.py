from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='imagenes_articulos/')

    def __str__(self):
        return self.nombre
    
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    productos = models.ManyToManyField(Producto, through='CarritoProductos')

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

class CarritoProductos(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en el carrito de {self.carrito.usuario.username}"