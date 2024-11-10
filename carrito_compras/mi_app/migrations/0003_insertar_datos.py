from django.db import migrations
from django.contrib.auth.models import User

def insertar_datos(apps, schema_editor):
    # Obtener los modelos
    Direccion = apps.get_model('mi_app', 'Direccion')
    Usuario = apps.get_model('mi_app', 'Usuario')
    Producto = apps.get_model('mi_app', 'Producto')
    Carrito = apps.get_model('mi_app', 'Carrito')
    Item = apps.get_model('mi_app', 'Item')
    Pago = apps.get_model('mi_app', 'Pago')
    Pedido = apps.get_model('mi_app', 'Pedido')

    # Insertar direcciones
    Direccion.objects.bulk_create([
        Direccion(calle='Av. Cabildo 5000', ciudad='Buenos Aires', codigo_postal='1426', pais='Argentina'),
        Direccion(calle='Calle Mendoza 750', ciudad='Rosario', codigo_postal='2000', pais='Argentina'),
        Direccion(calle='Av. Belgrano 120', ciudad='CABA', codigo_postal='1414', pais='Argentina'),
        Direccion(calle='Calle Paraguay 345', ciudad='Buenos Aires', codigo_postal='1032', pais='Argentina'),
        Direccion(calle='Av. de Mayo 520', ciudad='La Plata', codigo_postal='1900', pais='Argentina'),
        Direccion(calle='Calle San Juan 890', ciudad='Santa Fe', codigo_postal='3000', pais='Argentina'),
        Direccion(calle='Av. Rivadavia 2100', ciudad='Mendoza', codigo_postal='5500', pais='Argentina'),
        Direccion(calle='Calle Junín 710', ciudad='Buenos Aires', codigo_postal='1123', pais='Argentina'),
        Direccion(calle='Av. Sarmiento 1300', ciudad='CABA', codigo_postal='1415', pais='Argentina'),
        Direccion(calle='Calle 25 de Mayo 333', ciudad='Mar del Plata', codigo_postal='7600', pais='Argentina'),
    ])


    # Insertar usuarios
    users = [
        User.objects.create_user(username='juan.perez', password='password123', email='juan.perez@email.com'),
        User.objects.create_user(username='laura.gomez', password='password123', email='laura.gomez@email.com'),
        User.objects.create_user(username='carlos.fernandez', password='password123', email='carlos.fernandez@email.com'),
        User.objects.create_user(username='maria.lopez', password='password123', email='maria.lopez@email.com'),
        User.objects.create_user(username='pedro.sanchez', password='password123', email='pedro.sanchez@email.com')
    ]

    # Insertar los usuarios en el modelo Usuario
    usuarios = [
        Usuario(user=users[0], direccion=Direccion.objects.get(id=1)),
        Usuario(user=users[1], direccion=Direccion.objects.get(id=2)),
        Usuario(user=users[2], direccion=Direccion.objects.get(id=3)),
        Usuario(user=users[3], direccion=Direccion.objects.get(id=4)),
        Usuario(user=users[4], direccion=Direccion.objects.get(id=5))
    ]
    Usuario.objects.bulk_create(usuarios)

    # Insertar productos
    productos = [
        Producto(nombre='Laptop Lenovo', descripcion='Laptop portátil de 15.6" con procesador i7', precio=65000.0, categoria='Electrónica', stock=200),
        Producto(nombre='Auriculares Bluetooth', descripcion='Auriculares inalámbricos con cancelación de ruido', precio=12000.0, categoria='Accesorios', stock=300),
        Producto(nombre='Smartphone Samsung', descripcion='Smartphone Samsung Galaxy S23 128GB', precio=95000.0, categoria='Electrónica', stock=150),
        Producto(nombre='Tablet Apple', descripcion='Tablet Apple iPad 10.2" 64GB', precio=45000.0, categoria='Electrónica', stock=250),
        Producto(nombre='Reloj Inteligente', descripcion='Reloj inteligente con monitor de actividad', precio=15000.0, categoria='Accesorios', stock=180),
        Producto(nombre='Cámara de Seguridad', descripcion='Cámara de seguridad con visión nocturna', precio=35000.0, categoria='Electrónica', stock=100),
        Producto(nombre='Teclado Mecánico', descripcion='Teclado mecánico RGB con switches mecánicos', precio=8000.0, categoria='Accesorios', stock=250),
        Producto(nombre='Parlantes Bluetooth', descripcion='Parlantes portátiles Bluetooth', precio=9000.0, categoria='Accesorios', stock=180),
        Producto(nombre='Cargador Inalámbrico', descripcion='Cargador inalámbrico rápido para smartphones', precio=3000.0, categoria='Accesorios', stock=350),
        Producto(nombre='Disco Duro Externo', descripcion='Disco duro externo de 1TB USB 3.0', precio=12000.0, categoria='Electrónica', stock=200),
    ]
    Producto.objects.bulk_create(productos)

    # Insertar carritos
    carritos = [Carrito(usuario_id=i) for i in range(1, 11)]
    Carrito.objects.bulk_create(carritos)

    # Insertar items
    items = [
        Item(carrito_id=1, producto_id=1, cantidad=1), 
        Item(carrito_id=1, producto_id=2, cantidad=3),
        Item(carrito_id=2, producto_id=4, cantidad=2),
        Item(carrito_id=3, producto_id=5, cantidad=1),
        Item(carrito_id=4, producto_id=6, cantidad=2),
        Item(carrito_id=5, producto_id=7, cantidad=1),
        Item(carrito_id=6, producto_id=8, cantidad=4),
        Item(carrito_id=7, producto_id=9, cantidad=2),
        Item(carrito_id=8, producto_id=10, cantidad=1),
        Item(carrito_id=9, producto_id=3, cantidad=3),
    ]
    Item.objects.bulk_create(items)

    # Insertar pagos
    pagos = [
        Pago(monto=65000.0, metodo='Tarjeta de Crédito', estado='Completado'),
        Pago(monto=12000.0, metodo='Paypal', estado='Completado'),
        Pago(monto=95000.0, metodo='Transferencia Bancaria', estado='Pendiente'),
        Pago(monto=45000.0, metodo='Paypal', estado='Completado'),
        Pago(monto=15000.0, metodo='Tarjeta de Crédito', estado='Pendiente'),
        Pago(monto=35000.0, metodo='Transferencia Bancaria', estado='Completado'),
        Pago(monto=8000.0, metodo='Paypal', estado='Completado'),
        Pago(monto=9000.0, metodo='Tarjeta de Crédito', estado='Pendiente'),
        Pago(monto=3000.0, metodo='Paypal', estado='Completado'),
        Pago(monto=12000.0, metodo='Transferencia Bancaria', estado='Pendiente'),
    ]
    Pago.objects.bulk_create(pagos)

    # Insertar pedidos
    pedidos = [
        Pedido(usuario_id=1, carrito_id=1, estado='Pendiente', pago_id=1),
        Pedido(usuario_id=2, carrito_id=2, estado='Enviado', pago_id=2),
        Pedido(usuario_id=3, carrito_id=3, estado='Pendiente', pago_id=3),
        Pedido(usuario_id=4, carrito_id=4, estado='Enviado', pago_id=4),
        Pedido(usuario_id=5, carrito_id=5, estado='Pendiente', pago_id=5),
        Pedido(usuario_id=6, carrito_id=6, estado='Enviado', pago_id=6),
        Pedido(usuario_id=7, carrito_id=7, estado='Pendiente', pago_id=7),
        Pedido(usuario_id=8, carrito_id=8, estado='Enviado', pago_id=8),
        Pedido(usuario_id=9, carrito_id=9, estado='Pendiente', pago_id=9),
        Pedido(usuario_id=10, carrito_id=10, estado='Enviado', pago_id=10),
    ]
    Pedido.objects.bulk_create(pedidos)

class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0001_initial'),  # Migración inicial
        ('mi_app', '0002_direccion_pago_remove_carrito_productos_and_more'),  # Migración personalizada
    ]

    operations = [
        migrations.RunPython(insertar_datos),
    ]
