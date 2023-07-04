
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='IND'),
    path('galeria/', galeria,name='GALE'),
    path('contacto/',contacto,name='CONTAC'),
    path('registrarse/',registrarse,name='REGI'),
    path('base/',base,name='BASE'),
    path('agendar/',agendar,name='AGENDA'),
    path('admin_reparaciones/',admin_reparaciones,name='ADM_REP'),
    path('filtro_desc/',filtro_descripcion,name='FILTRO_DESC'),
    path('filtro_categoria/<id>/',filtro_categoria,name='FILTRO_CATEGORIA'),
    path('filtro_cate/',filtro_cate,name='FILTRO_CATE'),
    path('logout/',cerrar_sesion,name='LOGOUT'),
    path('ficha/<nombre>/', ficha, name='FICHA'),
    path('login/', user_login, name='LOGIN'),
    path('eliminar/<id>/', eliminar,name='ELI'),
    path('modificar/<id>/',modificar,name='MOD'),
    path('mod_reparacion/',modificar_reparacion,name='MR'),
    path('eliminar_repu/<id>/',eliminar_repuesto,name='ELI_REP'),
    path('grabar_g/',grabar_galeria,name='GG'),
    path('admin_repuestos/',admin_repuestos,name='ADM_REPUESTOS'),
    path('registrar_normal/',registrar_normal,name='REG_NORMAL'),
    path('agregar/<id_articulo>/',agregar_articulo,name='AA'),
    path('agregar_carrito/<id_articulo>/',agregar_articulo_carrito,name='AAC'),
    path('quitar/<id_articulo>/',quitar_articulo,name='QA'),
    path('vaciar/',vaciar,name='VACIAR'),
    path('eliminar_arti/<id_articulo>/',eliminar_arti,name='ELIMINAR'),
    path('carrito/',carrito,name='CARRITO'),
    
    path('guardar_contacto/', guardar_contacto, name='GUARDAR_CONT'),
]