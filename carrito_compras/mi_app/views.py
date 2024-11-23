from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Carrito, CarritoProductos
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al login tras registrarse
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def home(request):
    productos = Producto.objects.all()
    return render(request, 'home.html', {'productos': productos})

@login_required
def carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user, estado='abierto').first()
    productos = carrito.carritoproductos_set.all() if carrito else []
    total = carrito.calcular_total() if carrito else 0
    productos_con_subtotal = [
        {
            'producto': item.producto,
            'cantidad': item.cantidad,
            'subtotal': item.producto.precio * item.cantidad
        }
        for item in productos
    ]
    return render(request, 'mycart.html', {'productos': productos_con_subtotal, 'total': total})

def agregar_al_carrito(request, producto_id):
    # Obtén el producto solicitado
    producto = get_object_or_404(Producto, id=producto_id)

    # Obtén o crea el carrito para el usuario actual
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user, estado='abierto')

    # Busca si el producto ya está en el carrito
    carrito_producto, creado = CarritoProductos.objects.get_or_create(
        carrito=carrito,
        producto=producto,
    )

    # Si ya existe en el carrito, incrementa la cantidad
    if not creado:
        carrito_producto.cantidad += 1
    carrito_producto.save()

    return redirect('home')  # Redirige a la vista del carrito

def eliminar_del_carrito(request, producto_id):
    # Obtén el carrito del usuario actual
    carrito = Carrito.objects.filter(usuario=request.user, estado='abierto').first()

    if carrito:
        # Obtén la relación entre el carrito y el producto
        carrito_producto = get_object_or_404(CarritoProductos, carrito=carrito, producto_id=producto_id)

        # Decrementa la cantidad
        if carrito_producto.cantidad > 1:
            carrito_producto.cantidad -= 1
            carrito_producto.save()
        else:
            # Si la cantidad llega a 0, elimina el producto del carrito
            carrito_producto.delete()

    # Redirige al carrito después de eliminar una unidad
    return redirect('carrito')

@login_required
@transaction.atomic
def confirmar_compra(request):
    carrito = Carrito.objects.filter(usuario=request.user, estado='abierto').first()
    if not carrito:
        messages.error(request, "No tienes productos en el carrito.")
        return redirect('carrito')

    productos = carrito.carritoproductos_set.all()


    for item in productos:
        if item.producto.stock < item.cantidad:
            messages.error(request, f"No hay suficiente stock para {item.producto.nombre}.")
            return redirect('carrito')


    total = carrito.calcular_total()


    for item in productos:
        item.producto.stock -= item.cantidad
        item.producto.save()


    carrito.estado = 'finalizado'
    carrito.save()


    productos.delete()


    return render(request, 'confirmacion.html', {'total': total})
