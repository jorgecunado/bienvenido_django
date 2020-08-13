from django.http import HttpResponse
from django.shortcuts import render
from bienvenido.models import Empleado
# Create your views here.
def index(request):
	return HttpResponse("Hola Mundo, estas en bienvenido Hola")

def chau(request):
	return HttpResponse("Adios Mundo")	

def mostrar_empleado(request, id):
	emp = Empleado.objects.get(pk=id)
	return HttpResponse(emp.nombre)	

def borrar_empleado(request, id):
	emp = Empleado.objects.get(pk=id)
	nombre = emp.nombre
	emp.delete()
	return HttpResponse(nombre + "Borrado...")	