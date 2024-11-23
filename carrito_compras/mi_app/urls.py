from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

     path('', views.home, name='home'),


    path('registro/', views.registro, name='registro'),


    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('carrito/', views.carrito, name='carrito'),

    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),

    path('eliminar_del_carrito/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),

    path('confirmar_compra/', views.confirmar_compra, name='confirmar_compra'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)