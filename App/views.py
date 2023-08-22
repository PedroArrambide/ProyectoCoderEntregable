from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from .models import Curso

# Create your views here.
def probandoTemplates(self): 
    mi_html = open ("C:/Users/Pedro M. Arrambide/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/LocalCache/local-packages/Python311/Scripts/ProyectoCoderEntregable/App/Templates/templates1.html")
    plantilla = Template(mi_html.read())
    mi_html.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def curso_list(request):
    curso = Curso.objects.all()
    return render(request,'curso_list.html', {'curso': curso})

def curso_create(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        numero_comision = request.POST.get('numero_comision')
        curso = Curso(nombre=nombre, numero_comision=numero_comision)
        curso.save()
        return redirect('curso_list.html')
    return render(request, 'curso_create.html')

def index(request):
    return render(request, 'index.html')