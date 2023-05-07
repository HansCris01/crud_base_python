from django.urls import path
from . import views

from django.conf import settings #PARA MOSOTRAR IMAGENES
from django.contrib.staticfiles.urls import static #PARA MOSOTRAR IMAGENES

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'), #agregamos esto
    path('libros', views.libros, name='libros'),
    path('crear/crear', views.crear, name='crear'),
    path('crear/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('libros/editar/<int:id>',views.editar, name="editar")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #PARA MOSTRAR IMAGENES