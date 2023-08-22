from django.shortcuts import render, redirect
from .models import Curso


def probandoTemplates(request):
    # No es recomendable cargar una plantilla de esta manera en Django.
    # En su lugar, usa el sistema de plantillas incorporado.
    return render(request, 'templates1.html')

def curso_list(request):
    curso = Curso.objects.all()
    return render(request, 'curso_list.html', {'curso': curso})

def curso_create(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        numero_comision = request.POST.get('numero_comision')
        curso = Curso(nombre=nombre, numero_comision=numero_comision)
        curso.save()
        return redirect('curso_list')
    return render(request, 'curso_create.html')