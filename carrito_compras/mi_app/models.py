from django.db import models
from django.contrib.auth.models import User

class Direccion(models.Model):
    calle = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    codigo_postal = models.CharField(max_length=20)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.calle}, {self.ciudad}, {self.pais}"

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username  # Usando el nombre de usuario del modelo User

class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Carrito de {self.usuario.user.username}"

class Item(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

class Pago(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.metodo} - {self.estado}"

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    pago = models.ForeignKey(Pago, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Pedido {self.id} de {self.usuario.user.username}"

class Imagen(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    url_imagen = models.URLField()

    def __str__(self):
        return f"Imagen de {self.producto.nombre}"
