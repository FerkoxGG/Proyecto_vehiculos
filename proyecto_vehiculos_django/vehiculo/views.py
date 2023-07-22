from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.shortcuts import render, redirect
from .forms import VehiculoForm, RegistrationForm  # Asegúrate de tener un formulario de registro
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from .models import Vehiculo


def inicio(request):
    return render(request, 'vehiculo/index.html')

@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def vehiculo_add(request):
    if not request.user.has_perm('vehiculo.add_vehiculo'):
        raise PermissionDenied
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/vehiculo_form.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Aquí es donde asignarías el permiso al usuario.
            permission = Permission.objects.get(codename='visualizar_catalogo')
            user.user_permissions.add(permission)
            
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def vehiculo_list(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/vehiculo_list.html', {'vehiculos': vehiculos})
