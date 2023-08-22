from django.urls import path
from . import views


urlpatterns = [
    path('probandoTemplates/',views.probandoTemplates,name= 'probandoTemplates'),
    path('curso_list/', views.curso_list, name='curso_list'),
    path('curso_create/', views.curso_create, name='curso_create'),
    path('index/', views.index, name='index'),
    ]

