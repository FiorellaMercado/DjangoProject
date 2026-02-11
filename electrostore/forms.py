from django import forms
from django.contrib.auth.hashers import make_password
from .models import DetalleFactura, articulo,categoria, marca, roles,usuario,proveedor,factura,cliente

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = articulo
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = categoria
        fields = '__all__'


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = proveedor
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'

class FacturaForm(forms.ModelForm):
    class Meta:
        model = factura
        fields = '__all__'

class RolesForm(forms.ModelForm):
    class Meta:
        model = roles
        fields = '__all__'

class DetalleFacturaForm(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        fields = '__all__'

class Marca(forms.ModelForm):
    class Meta:
        model = marca
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = usuario
        fields = ['user', 'correo', 'password', 'nombre', 'apellido', 'cedula', 'direccion', 'telefono','rol']

    def clean_correo(self):
        correo = self.cleaned_data['correo']
        if usuario.objects.filter(correo=correo).exists():
            raise forms.ValidationError("Este correo ya está registrado.")
        return correo

    def save3(self, commit=True):
        print("u2")
        user = super().save(commit=False)
        print("Setting password")
        user.password = self.cleaned_data['password']
        if commit:
            user.save()
        return user
    

class LoginForm(forms.Form):
    email = forms.EmailField(label="Correo")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")