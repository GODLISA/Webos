from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RecetaSerializer, UsuarioSerializer
from core.models import Receta, Usuario

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def listas_recetas(request):
    if request.method == 'GET':
        receta = Receta.objects.all()
        serializer = RecetaSerializer(receta,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RecetaSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregar_receta(request):
    data = JSONParser().parse(request)
    serializer = RecetaSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def modElimReceta(request,codigo):
    try:
        m = Receta.objects.get(idreceta = codigo)
    except Receta.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RecetaSerializer(m)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RecetaSerializer(m,data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

# Create your views here.
class RecetaViewset(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def listas_usuario(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregar_usuario(request):
    data = JSONParser().parse(request)
    serializer = UsuarioSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def modElimUsuario(request,codigo):
    try:
        m = Usuario.objects.get(id = codigo)
    except Usuario.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UsuarioSerializer(m)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(m,data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)