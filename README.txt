
Carrito de Compras en Django

Descripción
Este proyecto es una aplicación web de carrito de compras desarrollada en Django. Permite a los usuarios ver productos, agregarlos al carrito y realizar una compra simulada. Además, los administradores pueden gestionar el inventario de productos.

Características
- Registro e inicio de sesión de usuarios.
- Añadir productos al carrito de compras.
- Gestión de productos por parte del administrador (añadir, modificar, eliminar).
- Calcular el total del carrito de compras.
- Simular la compra de productos.

Tecnologías Utilizadas
- Python 3.11.5
- Django 5.1.2
- SQLite como base de datos
- Bootstrap para el diseño front-end

Instalación
1. Clona este repositorio:
   git clone https://github.com/TitoWanobacoa/proyectodjango/tree/carritocompras2311
2. Navega al directorio del proyecto:
   cd carrito_compras
3. Crea un entorno virtual y actívalo.
   python -m venv myenv
   myenv\Scripts\activate   
4. Instala las dependencias:
   pip install -r requirements.txt
5. Realiza las migraciones:
   python manage.py migrate
6. Crea un superusuario:
   python manage.py createsuperuser
7. Inicia el servidor de desarrollo:
   python manage.py runserver

Uso
- Visita http://127.0.0.1:8000/ en tu navegador.
- Regístrate como usuario para empezar a añadir productos al carrito. O inicia sesión con el usuario de prueba: Nombre:marcus Contraseña:user1234
- Inicia sesión como administrador en http://127.0.0.1:8000/admin para gestionar productos. Credenciales de prueba: Nombre:user Contraseña:admila1234


Endpoints Principales
- / : Página de inicio con lista de productos
- /carrito/ : Ver carrito de compras
- /admin/ : Panel de administración para la gestión de productos


Licencia
Este es un proyecto de estudio.

Autor
Desarrollado por Liudmila Mashikhina, Marcus Melo Mitidiere y Juan Navaza.
