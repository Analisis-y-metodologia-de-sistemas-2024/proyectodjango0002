from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='imagenes_articulos/')
    activo = models.BooleanField(default=True)  

    def __str__(self):
        return self.nombre


class Carrito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[('abierto', 'Abierto'), ('finalizado', 'Finalizado')],
        default='abierto'
    )
    productos = models.ManyToManyField('Producto', through='CarritoProductos')

    def calcular_total(self):
        return sum(
            item.producto.precio * item.cantidad for item in self.carritoproductos_set.all()
        )

    def __str__(self):
        return f"Carrito de {self.usuario.username} ({self.estado})"

    @staticmethod
    def obtener_carrito_abierto(usuario):
        """Obtiene el carrito abierto de un usuario o None si no existe."""
        return Carrito.objects.filter(usuario=usuario, estado='abierto').first()



class CarritoProductos(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=1)  

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en {self.carrito}"
