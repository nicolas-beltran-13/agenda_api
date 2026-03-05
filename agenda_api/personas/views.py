from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PersonaSerializer
from .models import Persona
from .services import UbicacionService


class PersonaViewSet(viewsets.ModelViewSet):
    queryset=Persona.objects.all()
    serializer_class=PersonaSerializer
    
    def list(self, request, *args, **kwargs):
        personas = self.get_queryset()
        serializer = self.get_serializer(personas, many=True)
        return Response({
            "success": True,
            "data": serializer.data,
        })
        
@api_view(['GET'])
def paises_api(request):
        paises=UbicacionService.obtener_paises()
        return Response(paises)

@api_view(['GET'])
def ciudades_api(request,pais):
    ciudades = UbicacionService.obtener_ciudades_por_pais(pais)
    return Response(ciudades)

def lista_views(request):
    return render(request, 'personas/lista.html')

def crear_views(request):
    return render(request, 'personas/crear.html')

def editar_views(request):
    return render(request, 'personas/editar.html', {"id":id})
