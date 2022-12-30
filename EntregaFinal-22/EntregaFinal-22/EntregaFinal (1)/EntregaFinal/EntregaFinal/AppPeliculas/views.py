from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from AppPeliculas.forms import TerrorFormulario, AccionFormulario, AventuraFormulario
from AppPeliculas.models import Terror, Accion, Aventura


# Create your views here.

def inicio(request):
    return render(request, "AppPeliculas/inicio.html")

def terror(request):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = TerrorFormulario(request.POST)
        print(miFormulario)        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            terror = Terror(mas_vistas=informacion["mas_vistas"], taquilla=informacion["taquilla"], critica_peliculas=informacion["critica_peliculas"])
            terror.save()
            return render(request, "AppPeliculas/inicio.html")
    else:
        miFormulario = TerrorFormulario()
    return render(request, "AppPeliculas/terror.html", {"miFormulario": miFormulario})

def accion(request):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = AccionFormulario(request.POST)
        print(miFormulario)        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            accion = Accion(mas_vistas=informacion["mas_vistas"], taquilla=informacion["taquilla"], critica_peliculas=informacion["critica_peliculas"])
            accion.save()
            return render(request, "AppPeliculas/inicio.html")
    else:
        miFormulario = AccionFormulario()
    return render(request, "AppPeliculas/accion.html", {"miFormulario": miFormulario})

def aventura(request):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = AventuraFormulario(request.POST)
        print(miFormulario)        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            aventura = Aventura(mas_vistas=informacion["mas_vistas"], taquilla=informacion["taquilla"], critica_peliculas=informacion["critica_peliculas"])
            aventura.save()
            return render(request, "AppPeliculas/inicio.html")
    else:
        miFormulario = AventuraFormulario()
    return render(request, "AppPeliculas/aventura.html", {"miFormulario": miFormulario})



def cartelera(request):
    return render(request, "AppPeliculas/cartelera.html")

def nosotros(request):
    return render(request, "AppPeliculas/nosotros.html")

def peliculas(request):
    return render(request, "AppPeliculas/peliculas.html")

def terrorapi(request):
    terror_todos = Terror.objects.all()
    return HttpResponse(serializers.serialize('json', terror_todos))

def accionapi(request):
    accion_todos = Accion.objects.all()
    return HttpResponse(serializers.serialize('json', accion_todos))

def aventuraapi(request):
    aventura_todos = Aventura.objects.all()
    return HttpResponse(serializers.serialize('json', aventura_todos))





def leer_terror(request):
    terror = Terror.objects.all()
    return HttpResponse(serializers.serialize('json',terror))

def crear_terror(request):
    terror = Terror(mas_vistas = 'TestIngresoCRUD',taquilla = 122, critica_peliculas=55)
    terror.save()
    return HttpResponse(f'La película {terror.mas_vistas} ha sido añadida')

def editar_terror(request):
    mas_vistas = 'TestIngresoCRUD'
    mas_vistas_nuevo = 'NuevoTestIngresoCRUD'
    Terror.objects.filter(mas_vistas=mas_vistas).update(mas_vistas=mas_vistas_nuevo)
    return HttpResponse(f'La película {mas_vistas} ha sido actualizada')

def eliminar_terror(request):
    mas_vistas = 'NuevoTestIngresoCRUD'
    terror = Terror.objects.get(mas_vistas=mas_vistas)
    terror.delete()
    return HttpResponse(f'La película {mas_vistas} ha sido eliminada')




def leer_accion(request):
    accion_all=Accion.objects.all()
    return HttpResponse(serializers.serialize("json",accion_all))

def crear_accion(request):
    accion = Accion(mas_vistas = 'TestIngresoCRUD',taquilla = 122, critica_peliculas=55)
    accion.save()
    return HttpResponse(f'La película {accion.mas_vistas} ha sido añadida')


def editar_accion(request):
    mas_vistas = 'TestIngresoCRUD'
    mas_vistas_nuevo = 'NuevoTestIngresoCRUD'
    Accion.objects.filter(mas_vistas=mas_vistas).update(mas_vistas=mas_vistas_nuevo)
    return HttpResponse(f'La película {mas_vistas} ha sido actualizada')

def eliminar_accion(request):
    mas_vistas = 'NuevoTestIngresoCRUD'
    accion = Accion.objects.get(mas_vistas=mas_vistas)
    accion.delete()
    return HttpResponse(f'La película {mas_vistas} ha sido eliminada')




def leer_aventura(request):
    aventura_all=Aventura.objects.all()
    return HttpResponse(serializers.serialize("json",aventura_all))

def crear_aventura(request):
    aventura = Aventura(mas_vistas = 'TestIngresoCRUD',taquilla = 122, critica_peliculas=55)
    aventura.save()
    return HttpResponse(f'La película {aventura.mas_vistas} ha sido añadida')


def editar_aventura(request):
    mas_vistas = 'TestIngresoCRUD'
    mas_vistas_nuevo = 'NuevoTestIngresoCRUD'
    Aventura.objects.filter(mas_vistas=mas_vistas).update(mas_vistas=mas_vistas_nuevo)
    return HttpResponse(f'La película {mas_vistas} ha sido actualizada')

def eliminar_aventura(request):
    mas_vistas = 'NuevoTestIngresoCRUD'
    aventura = Aventura.objects.get(mas_vistas=mas_vistas)
    aventura.delete()
    return HttpResponse(f'La película {mas_vistas} ha sido eliminada')
    













from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView

class TerrorList(ListView):
    model = Terror
    template = 'AppPeliculas/terror_list.html'

class AventuraList(ListView):
    model = Aventura
    template = 'AppPeliculas/aventura_list.html'

class AccionList(ListView):
    model = Accion
    template = 'AppPeliculas/accion_list.html'
    

class TerrorDetail(DetailView):
    model = Terror
    template_name="AppPeliculas/terror_detail.html"
    
class AccionDetail(DetailView):
    model = Accion
    template_name="AppPeliculas/accion_detail.html"
    
class AventuraDetail(DetailView):
    model = Aventura
    template_name="AppPeliculas/aventura_detail.html"
    


class TerrorCreate(CreateView):
    model = Terror
    fields = '__all__'
    success_url = '/AppPeliculas/terror/list/'

class AccionCreate(CreateView):
    model = Accion
    fields = '__all__'
    success_url = '/AppPeliculas/accion/list/'

class AventuraCreate(CreateView):
    model = Aventura
    fields = '__all__'
    success_url = '/AppPeliculas/aventura/list/'



class TerrorEdit(UpdateView):
    model = Terror
    fields = '__all__'
    success_url = '/AppPeliculas/terror/list'

class AccionEdit(UpdateView):
    model = Accion
    fields = '__all__'
    success_url = '/AppPeliculas/accion/list'

class AventuraEdit(UpdateView):
    model = Aventura
    fields = '__all__'
    success_url = '/AppPeliculas/aventura/list'
    

    
    
class TerrorDelete(DeleteView):
    model = Terror
    fields = '__all__'
    success_url = '/AppPeliculas/terror/list'

class AccionDelete(DeleteView):
    model = Accion
    fields = '__all__'
    success_url = '/AppPeliculas/accion/list'

class AventuraDelete(DeleteView):
    model = Aventura
    #fields = '__all__'
    success_url = '/AppPeliculas/aventura/list'










    
    
