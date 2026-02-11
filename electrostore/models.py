from django.db import models


class categoria(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, verbose_name="Descripción")

    def __str__(self):
        return self.descripcion

class proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    ruc = models.TextField(verbose_name="RUC")
    nombre = models.TextField(verbose_name="Nombre")
    direccion = models.TextField(verbose_name="Dirección")
    telefono = models.IntegerField(verbose_name="Teléfono")
    correo = models.TextField(verbose_name="Correo")

    def __str__(self):
        return self.nombre

class marca(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, verbose_name="Descripción")

    def __str__(self):
        return self.descripcion

class articulo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255,verbose_name="Nombre")
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name="Imagen")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.IntegerField(verbose_name="Precio")
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE, verbose_name="Categoría")
    proveedor = models.ForeignKey(proveedor, on_delete=models.CASCADE, verbose_name="Proveedor")
    marca = models.ForeignKey(marca, on_delete=models.CASCADE, verbose_name="Marca")

    def __str__(self):
        return self.nombre

class roles(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, verbose_name="Descripción")

    def __str__(self):
        return self.descripcion

class usuario(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.TextField(verbose_name="Usuario")
    password = models.TextField(verbose_name="Contraseña")
    cedula = models.IntegerField(verbose_name="Cédula")
    nombre = models.TextField(verbose_name="Nombre")
    apellido = models.TextField(verbose_name="Apellido")
    direccion = models.TextField(verbose_name="Dirección")
    telefono = models.IntegerField(verbose_name="Teléfono")
    correo = models.TextField(verbose_name="Correo", unique=True)
    rol = models.ForeignKey(roles, on_delete=models.CASCADE, verbose_name="Rol")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"




class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.IntegerField(verbose_name="Cédula")
    nombre = models.TextField(verbose_name="Nombre")
    apellido = models.TextField(verbose_name="Apellido")
    direccion = models.TextField(verbose_name="Dirección")
    telefono = models.IntegerField(verbose_name="Teléfono")
    correo = models.TextField(verbose_name="Correo")

    def __str__(self):
        return str(self.cedula)

class factura(models.Model):
    id = models.AutoField(primary_key=True)
    numero_factura = models.TextField(verbose_name="Nro. factura")
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    fecha= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de emisión")
    descripcion = models.TextField(verbose_name="Descripción")
    #items = models.TextField(verbose_name="Items")
    #cantidad = models.IntegerField(verbose_name="Cantidad de items")
    precio_total = models.IntegerField(verbose_name="Precio total")

    def __str__(self):
        return self.numero_factura
    

class DetalleFactura(models.Model):
    id = models.AutoField(primary_key=True)
    factura = models.ForeignKey(factura, on_delete=models.CASCADE, related_name='detalles', verbose_name="Factura")
    articulo = models.ForeignKey(articulo, on_delete=models.CASCADE, verbose_name="Artículo")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    precio = models.IntegerField(verbose_name="Precio")

    def __str__(self):
        return f'{self.factura.numero_factura} - {self.articulo.nombre}'

    @property
    def subtotal(self):
        return str(self.cantidad * self.precio)
    

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = usuario.objects.get(id=user_id)
                request.user = user
            except usuario.DoesNotExist:
                request.user = None
        else:
            request.user = None

        response = self.get_response(request)
        return response
        


