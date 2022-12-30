from django.urls import path
from AppPeliculas import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('terror/', views.terror, name="terror"),
    path('terrorApi/', views.terrorapi),
    path('accion/', views.accion, name="accion"),
    path('accionApi/', views.accionapi),
    path('aventura/', views.aventura, name="aventura"),
    path('aventuraApi/', views.aventuraapi),
    path('cartelera/', views.cartelera, name="cartelera"),
    path('sobrenosotros/', views.nosotros, name = "sobre"),
    path('lasmejores/', views.peliculas, name="peliculas"),
    path('leerTerror/', views.leer_terror),
    path('crearTerror/', views.crear_terror),
    path('editarTerror/', views.editar_terror),
    path('eliminarTerror/', views.eliminar_terror),
    path('leerAccion/', views.leer_accion),
    path('crearAccion/', views.crear_accion),
    path('editarAccion/', views.editar_accion),
    path('eliminarAccion/', views.eliminar_accion),
    path('leerAventura/', views.leer_aventura),
    path('crearAventura/', views.crear_aventura),
    path('editarAventura/', views.editar_aventura),
    path('eliminarAventura/', views.eliminar_aventura),
    
    path('terror/list/', views.TerrorList.as_view(),name='tlist'),
    path('accion/list/', views.AccionList.as_view(),name='alist'),
     path('aventura/list/', views.AventuraList.as_view(),name='avlist'),
    
    path('terror/ver/<pk>', views.TerrorDetail.as_view(),name='tver'),
    path('accion/ver/<pk>', views.AccionDetail.as_view(),name='aver'),
    path('aventura/ver/<pk>', views.AventuraDetail.as_view(),name='avver'),
    
    path('terror/create/', views.TerrorCreate.as_view(),name='tcrear'),
    path('accion/create/', views.AccionCreate.as_view(),name='acrear'),
    path('aventura/create/', views.AventuraCreate.as_view(),name='avcrear'),
    
    path('terror/edit/<pk>',views.TerrorEdit.as_view(),name='teditar'),
    path('accion/edit/<pk>',views.AccionEdit.as_view(),name='aeditar'),
    path('aventura/edit/<pk>',views.AventuraEdit.as_view(),name='aveditar'),
    
    path('terror/borrar/<pk>',views.TerrorDelete.as_view(),name='teliminar'),
    path('accion/borrar/<pk>',views.AccionDelete.as_view(),name='aeliminar'),
    path('aventura/borrar/<pk>',views.AventuraDelete.as_view(),name='aveliminar'),
    
    ]