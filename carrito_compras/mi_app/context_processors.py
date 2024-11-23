from .models import Carrito

def carrito_context(request):

    if request.user.is_authenticated:
        carrito = Carrito.objects.filter(usuario=request.user, estado='abierto').first()
        if carrito:
            total_productos = sum(item.cantidad for item in carrito.carritoproductos_set.all())
        else:
            total_productos = 0
    else:
        total_productos = 0

    return {'total_productos': total_productos}
