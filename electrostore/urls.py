from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    #Lado del cliente
    path('', views.index, name='index'),
    path('sesion', views.sesion, name='iniciar_sesion'),
    path('catalogo',views.catalogo, name='catalogo'),
    path('catalogo/<int:categoria_id>/', views.catalogo, name='catalogo_filtrado'),
    path('detalle/<int:id>/',views.detalle, name='detalle'),
    path('inicio', views.inicio, name='inicio'),
    path('contacto',views.contacto, name='contacto'),
    path('carrito',views.carrito, name='carrito'),
    #seion
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout_view, name='logout'),

    #Lado de Administrador
    #articulos
    path('us_articulos',views.us_articulos, name='us_articulos'),
    path('us_articulos/crear',views.ar_crear, name='ar_crear'),
    path('us_articulos/editar/<int:id>',views.ar_editar, name='ar_editar'),
    path('us_articulos/eliminar/<int:id>',views.ar_eliminar, name='ar_eliminar'),
    #categorias
    path('us_categorias',views.us_categorias, name='us_categorias'),
    path('us_categorias/crear',views.cat_crear, name='cat_crear'),
    path('us_categorias/editar/<int:id>',views.cat_editar, name='cat_editar'),
    path('us_categorias/eliminar/<int:id>',views.cat_eliminar, name='cat_eliminar'),
    #usuarios
    path('us_usuarios',views.us_usuarios, name='us_usuarios'),
    path('us_usuarios/crear',views.usu_crear, name='usu_crear'),
    path('us_usuarios/editar/<int:id>',views.usu_editar, name='usu_editar'),
    path('us_usuarios/eliminar/<int:id>',views.usu_eliminar, name='usu_eliminar'),
    #clientes
    path('us_clientes',views.us_clientes, name='us_clientes'),
    path('us_clientes/crear',views.cli_crear, name='cli_crear'),
    path('us_clientes/editar/<int:id>',views.cli_editar, name='cli_editar'),
    path('us_clientes/eliminar/<int:id>',views.cli_eliminar, name='cli_eliminar'),
    #proveedores
    path('us_proveedores',views.us_proveedores, name='us_proveedores'),
    path('us_proveedores/crear',views.pro_crear, name='pro_crear'),
    path('us_proveedores/editar/<int:id>',views.pro_editar, name='pro_editar'),
    path('us_proveedores/eliminar/<int:id>',views.pro_eliminar, name='pro_eliminar'),
    #facturas
    path('us_factura',views.us_facturas, name='us_facturas'),
    path('us_facturas/crear',views.fac_crear, name='fac_crear'),
    path('us_facturas/editar/<int:id>',views.fac_editar, name='fac_editar'),
    path('us_facturas/eliminar/<int:id>',views.fac_eliminar, name='fac_eliminar'),
    path('us_facturas/detalle/<int:id>',views.fac_detalle, name='fac_detalle'),
    #detalle_factura
    path('us_det_factura',views.us_det_factura, name='us_det_factura'),
    path('us_det_facturas/crear',views.det_fac_crear, name='det_fac_crear'),
    path('us_det_facturas/editar/<int:id>',views.det_fac_editar, name='det_fac_editar'),
    path('us_det_facturas/eliminar/<int:id>',views.det_fac_eliminar, name='det_fac_eliminar'),
    #roles
    path('us_roles',views.us_roles, name='us_roles'),
    path('us_roles/crear',views.rol_crear, name='rol_crear'),
    path('us_roles/editar/<int:id>',views.rol_editar, name='rol_editar'),
    path('us_roles/eliminar/<int:id>',views.rol_eliminar, name='rol_eliminar'),
    #marca
    path('us_marca',views.us_marca, name='us_marca'),
    path('us_marca/crear',views.mar_crear, name='mar_crear'),
    path('us_marca/editar/<int:id>',views.mar_editar, name='mar_editar'),
    path('us_marca/eliminar/<int:id>',views.mar_eliminar, name='mar_eliminar'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)