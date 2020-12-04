from django.shortcuts import render, redirect,get_object_or_404
from scooterlineapp.forms import RegistrarForm,SeleccionarScooter,ActualizaEstado
from .models import Usuarios
from django.contrib.auth.models import User
from django.contrib import messages


def inicio(request):
    return render(request, "inicio.html")


def producto(request):
    return render(request, "producto.html")

def nosotros(request):
    return render(request, "nosotros.html")  

def registrar_usuario(request):
    datos = {'form':RegistrarForm()}
    if request.method == 'POST':
        formulario= RegistrarForm(data=request.POST)
        if formulario.is_valid(): 
            formulario.save()
            return redirect('login')
        datos["form"]=formulario

    return render(request, "registrar_usuario.html", datos)

def redireccion(request):
    if request.user.is_staff:
        return redirect('/admin')
    else:
        return redirect('inicio')

def agregar(request,username):
    usuario = get_object_or_404(User, username = username)
    data = {'form':SeleccionarScooter(instance=usuario)}
    if request.method == 'POST':
        formulario = SeleccionarScooter(data = request.POST)
        if formulario.is_valid():
            
            if Usuarios.objects.filter(activo=True,username=username):
                messages.error(request,"Usted ya tiene un viaje activo")
    
            else:                
                formulario.save()
                return redirect('ubicacion')

    return render(request,"agregar.html",data)



def viajes(request,username):
    usuario = Usuarios.objects.filter(username=username)
    return render(request,"viajes.html",{'usuario':usuario})

def ubicacion(request):
    return render(request,"ubicacion.html")


def actualiza_estado(request, id):
    usuario = get_object_or_404(Usuarios, id = id)
    data = {'form' : ActualizaEstado(instance = usuario)}
    if request.method == "POST":
        formulario = ActualizaEstado(data = request.POST, instance = usuario, files = request.FILES)
        if formulario.is_valid():
            formulario.save()

        data["form"] = formulario
    return render(request, "actualizaestado.html", data)

def elminaviajes(request, id):
    usuario = get_object_or_404(Usuarios, id = id)
    usuario.delete()
    return redirect('inicio')






  