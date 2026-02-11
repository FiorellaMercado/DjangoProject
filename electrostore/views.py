from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import DetalleFactura, articulo, categoria, marca, roles, usuario, proveedor, cliente, factura
from .forms import ArticuloForm, CategoriaForm, DetalleFacturaForm, LoginForm, Marca, RolesForm, UsuarioForm, ProveedorForm, ClienteForm, FacturaForm

# Create your views here.
def index(request):
    ultimos_articulos = articulo.objects.order_by('-id')[:6]
    
    context = {
        'ultimos_articulos': ultimos_articulos
    }
    
    return render(request, 'index.html',context)


#sesion

def sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                usuario_obj = usuario.objects.get(correo=email)
            except usuario.DoesNotExist:
                messages.error(request, 'El correo no está registrado')
                return render(request, 'sesion.html', {'form': form})

            if password == usuario_obj.password:
                # Establecer la sesión del usuario
                request.session['user_id'] = usuario_obj.id
                request.session['user_name'] = f"{usuario_obj.nombre} {usuario_obj.apellido}"
                if usuario_obj.rol_id == 2:  # Asumimos que el rol_id 2 es para administradores
                    messages.success(request, ' ')
                    return redirect('inicio')  # Redirige a inicio.html para administradores
                else:
                    messages.success(request, ' ')
                    return redirect('index')  # Redirige a index.html para usuarios normales
            else:
                messages.error(request, 'Contraseña incorrecta')
    else:
        form = LoginForm()
    return render(request, 'sesion.html', {'form': form})

def logout_view(request):
    request.session.flush()
    return redirect('iniciar_sesion')

def inicio(request):
    user_name = request.session.get('user_name', '')
    context = {
        'user_name': user_name
    }
    return render(request, 'user/inicio.html', context)

#registro
def registro(request):
    if request.method == 'POST':
        print("11")
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save3()
            print("u1")
            messages.success(request, 'Usuario registrado exitosamente')
            return redirect('iniciar_sesion')
        else: 
            print(form.errors)
    else:
        print("22")
        form = UsuarioForm()

    return render(request, 'registro.html', {'form': form})





def carrito(request):
    return render(request, 'carrito.html')


def catalogo(request, categoria_id=None):
    categorias=categoria.objects.all()
    if categoria_id:
        articulos = articulo.objects.filter(categoria_id=categoria_id)
    else:
        articulos = articulo.objects.all()
    context = {
        'articulos': articulos,
        'categorias': categorias,
        'categoria_id': int(categoria_id) if categoria_id else None
    }
    
    return render(request, 'catalogo.html', context)



def detalle(request,id):
    articulo_obj=articulo.objects.get(id=id)
    articulo_obj.precio_formateado = "{:,.0f}".format(articulo_obj.precio).replace(",", ".")
    return render(request, 'detalles.html',{'articulo': articulo_obj})


def contacto(request):
    return render(request, 'contacto.html')


#vistas artículos (index, crear, editar, eliminar)
def us_articulos(request):
    articulos=articulo.objects.all()
    for art in articulos:
        art.precio_formateado = "{:,.0f}".format(art.precio).replace(",", ".")
    print(articulos)
    return render(request, 'user/articulos/index.html',{'articulos':articulos})


def ar_crear(request):
    formulario=ArticuloForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('us_articulos')
    return render(request, 'user/articulos/crear.html',{'formulario':formulario})



def ar_editar(request,id):
    articulo_obj=articulo.objects.get(id=id)
    formulario=ArticuloForm(request.POST or None,request.FILES or None, instance=articulo_obj)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('us_articulos')
    return render(request, 'user/articulos/editar.html',{'formulario':formulario})

def ar_eliminar(request,id):
    articulo_obj=articulo.objects.get(id=id)
    articulo_obj.delete()
    return redirect('us_articulos')


#vistas de categorías (index, crear, editar, eliminar)
def us_categorias(request):
    categorias=categoria.objects.all()
    print(categorias)
    return render(request, 'user/categoria/index.html',{'categorias':categorias})

def cat_crear(request):
    formulario=CategoriaForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('us_categorias')
    return render(request, 'user/categoria/crear.html',{'formulario':formulario})

def cat_editar(request,id):
    categoria_obj=categoria.objects.get(id=id)
    formulario=CategoriaForm(request.POST or None,request.FILES or None, instance=categoria_obj)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('us_categorias')
    return render(request, 'user/categoria/editar.html',{'formulario':formulario})

def cat_eliminar(request,id):
    categoria_obj=categoria.objects.get(id=id)
    categoria_obj.delete()
    return redirect('us_categorias')


#vistas de usuarios (index, crear, editar, eliminar)
def us_usuarios(request):
    usuarios=usuario.objects.all()
    print(usuarios)
    return render(request, 'user/usuarios/index.html',{'usuarios':usuarios})

def usu_crear(request):
    
    formulario=UsuarioForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('us_usuarios')
    return render(request, 'user/usuarios/crear.html',{'formulario':formulario})

def usu_editar(request,id):
   
    usuario_obj=usuario.objects.get(id=id)
    formulario=UsuarioForm(request.POST or None,request.FILES or None, instance=usuario_obj)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('us_usuarios')
    return render(request, 'user/usuarios/editar.html',{'formulario':formulario})

def usu_eliminar(request,id):
    usuario_obj=usuario.objects.get(id=id)
    usuario_obj.delete()
    return redirect('us_usuarios')


#vistas de proveedores (index, crear, editar, eliminar)
def us_proveedores(request):
    proveedores=proveedor.objects.all()
    print(proveedor)
    return render(request, 'user/proveedores/index.html',{'proveedores':proveedores})

def pro_crear(request):
    formulario=ProveedorForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('us_proveedores')
    return render(request, 'user/proveedores/crear.html',{'formulario':formulario})

def pro_editar(request,id):
    proveedor_obj=proveedor.objects.get(id=id)
    formulario=ProveedorForm(request.POST or None,request.FILES or None, instance=proveedor_obj)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('us_proveedores')
    return render(request, 'user/proveedores/editar.html',{'formulario':formulario})

def pro_eliminar(request,id):
    proveedor_obj=proveedor.objects.get(id=id)
    proveedor_obj.delete()
    return redirect('us_proveedores')


#vistas de clientes (index, crear, editar, eliminar)
def us_clientes(request):
    clientes=cliente.objects.all()
    print(cliente)
    return render(request, 'user/clientes/index.html',{'clientes':clientes})

def cli_crear(request):
    formulario=ClienteForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('us_clientes')
    return render(request, 'user/clientes/crear.html',{'formulario':formulario})

def cli_editar(request,id):
    cliente_obj=cliente.objects.get(id=id)
    formulario=ClienteForm(request.POST or None,request.FILES or None, instance=cliente_obj)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('us_clientes')
    return render(request, 'user/clientes/editar.html',{'formulario':formulario})

def cli_eliminar(request,id):
    cliente_obj=cliente.objects.get(id=id)
    cliente_obj.delete()
    return redirect('us_clientes')


#vistas de facturas (index, crear, editar, eliminar)
def us_facturas(request):
    facturas=factura.objects.all()
    print(factura)
    return render(request, 'user/factura/index.html',{'facturas':facturas})

def fac_crear(request):
    formulario=FacturaForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('us_facturas')
    return render(request, 'user/factura/crear.html',{'formulario':formulario})

def fac_editar(request,id):
    factura_obj=factura.objects.get(id=id)
    formulario=FacturaForm(request.POST or None,request.FILES or None, instance=factura_obj)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('us_facturas')
    return render(request, 'user/factura/editar.html',{'formulario':formulario})

def fac_detalle(request,factura_id):
    facturas=factura.objects.all()
    if factura_id:
        fac_detalles = DetalleFactura.objects.filter(factura_id=factura_id)
    else:
        fac_detalles  = DetalleFactura.objects.all()
    context = {
        'fac_detalles': fac_detalles,
        'facturas': facturas,
        'factura_id': int(factura_id) if factura_id else None
    }
    
    return render(request, 'user/detalle_factura/index.html', context)


def catalogo(request, categoria_id=None):
    categorias=categoria.objects.all()
    if categoria_id:
        articulos = articulo.objects.filter(categoria_id=categoria_id)
    else:
        articulos = articulo.objects.all()
    context = {
        'articulos': articulos,
        'categorias': categorias,
        'categoria_id': int(categoria_id) if categoria_id else None
    }
    
    return render(request, 'catalogo.html', context)

def fac_eliminar(request,id):
    factura_obj=factura.objects.get(id=id)
    factura_obj.delete()
    return redirect('us_facturas')


#vistas de roles (index, crear, editar, eliminar)
def us_roles(request):
    Roles=roles.objects.all()
    print(Roles)
    return render(request, 'user/roles/index.html',{'roles':Roles})

def rol_crear(request):
    formulario=RolesForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('us_roles')
    return render(request, 'user/roles/crear.html',{'formulario':formulario})

def rol_editar(request,id):
    roles_obj=roles.objects.get(id=id)
    formulario=RolesForm(request.POST or None,request.FILES or None, instance=roles_obj)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('us_roles')
    return render(request, 'user/roles/editar.html',{'formulario':formulario})

def rol_eliminar(request,id):
    roles_obj=roles.objects.get(id=id)
    roles_obj.delete()
    return redirect('us_roles')

#vistas de marca (index, crear, editar, eliminar) 
def us_marca(request):
    Marcas=marca.objects.all()
    print(Marcas)
    return render(request, 'user/marca/index.html',{'marcas':Marcas})

def mar_crear(request):
    formulario=Marca(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('us_marca')
    return render(request, 'user/marca/crear.html',{'formulario':formulario})

def mar_editar(request,id):
    marca_obj=marca.objects.get(id=id)
    formulario=Marca(request.POST or None,request.FILES or None, instance=marca_obj)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('us_marca')
    return render(request, 'user/marca/editar.html',{'formulario':formulario})

def mar_eliminar(request,id):
    marca_obj=marca.objects.get(id=id)
    marca_obj.delete()
    return redirect('us_marca')


#vistas de detalle_factura(index, crear, editar, eliminar)
def us_det_factura(request):
    det_facturas=DetalleFactura.objects.all()
    return render(request, 'user/detalle_factura/index.html',{'det_facturas':det_facturas})

def det_fac_crear(request):
    formulario=DetalleFacturaForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('us_det_factura')
    return render(request, 'user/detalle_factura/crear.html',{'formulario':formulario})

def det_fac_editar(request,id):
    detalle_obj=DetalleFactura.objects.get(id=id)
    formulario=DetalleFacturaForm(request.POST or None,request.FILES or None, instance=detalle_obj)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('us_det_factura')
    return render(request, 'user/detalle_factura/editar.html',{'formulario':formulario})

def det_fac_eliminar(request,id):
    detalle_obj=DetalleFactura.objects.get(id=id)
    detalle_obj.delete()
    return redirect('us_det_factura')