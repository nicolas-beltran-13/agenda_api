from django.urls import path, include
from rest_framework.routers import DefaultRouter
from personas.views import (PersonaViewSet, 
                    paises_api, ciudades_api
                    , lista_views, crear_views, 
                    editar_views)

router = DefaultRouter()
router.register(r'personas', PersonaViewSet)
urlpatterns = [
    path('',lista_views, name= 'index'),
    path('crear/',crear_views, name= 'crear'),
    path('editar/<int:id>/',editar_views, name= 'editar'),
    path('api/paises', paises_api),
    path('api/ciudades/<str:pais>/', ciudades_api),
    path('api/', include(router.urls)),
]
