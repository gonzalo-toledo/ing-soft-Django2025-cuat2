from django.contrib.auth.models import User
from pasajeros.models import Pasajero
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.serializers import UserSerializer, PasajeroSerializer, RegistroSerializer

from pasajeros.models import Pasajero 


# USERS

# class UserListView(ListAPIView):
#     '''
#     GET /api/users/
#       return -> [<UserSerializer>, ...]
#     '''
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    


class UserListCreateView(ListCreateAPIView):
    '''
    GET /api/users/
        return -> [<UserSerializer>, ...]
    POST /api/users/ - crea un nuevo usuario
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    '''
    GET /api/users/
        return -> [<UserSerializer>, ...]
    PUT /api/users/1/ -> actualiza el usuario 1
    PATCH /api/users/1/ -> actualiza parcialmente el usuario 1
    DELETE /api/users/1/ -> elimina el usuario 1   
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_destroy(self, instance):
        if instance.is_active:
            instance.is_active = False
            instance.save()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance=instance)
        return Response(
            {"detail": "Usuario desactivado correctamente."},
            status=status.HTTP_200_OK
        )
        


#PASAJEROS
class PasajeroListCreateView(ListCreateAPIView):
    """
    GET /api/users/<user_pk>/pasajeros/ -> lista pasajeros del usuario
    POST /api/users/<user_pk>/pasajeros/ -> crea pasajero para el usuario
    """

    serializer_class = PasajeroSerializer

    # redefino el queryset para filtrar por usuario:
    def get_queryset(self):
        user_pk = self.kwargs['user_pk']
        return Pasajero.objects.filter(usuario_id=user_pk)

    def perform_create(self, serializer):
        user_pk = self.kwargs['user_pk'] # obtengo el user_pk de la URL
        usuario = get_object_or_404(User, pk=user_pk)
        serializer.save(usuario=usuario)



#USUARIO + PASAJERO
class RegistroCreateView(CreateAPIView):
    """
    POST /api/registro/ -> crea un nuevo usuario + pasajero
    """
    queryset = Pasajero.objects.all()
    serializer_class = RegistroSerializer







# #REGISTRO INICIAL (USUARIO + PASAJERO)
# class RegistroCreateView(ListCreateAPIView):
#     """
#     POST /api/registro/ -> crea un nuevo usuario + pasajero
#     GET /api/registro/ -> lista pasajeros creados (opcional)
#     """
#     queryset = Pasajero.objects.all()
#     serializer_class = RegistroSerializer


# # -----------------------------------
# # Pasajeros adicionales para usuario logueado
# # -----------------------------------
# class PasajeroNuevoCreateView(ListCreateAPIView):
#     """
#     POST /api/pasajeros/nuevo/ -> crea un pasajero adicional para el usuario logueado
#     GET /api/pasajeros/nuevo/ -> lista los pasajeros del usuario logueado
#     """
#     serializer_class = PasajeroNuevoSerializer
#     # permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         # Solo los pasajeros del usuario logueado
#         return Pasajero.objects.filter(usuario=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(usuario=self.request.user)

# class PasajeroListCreateView(ListCreateAPIView):
#     """
#     GET /api/users/<user_pk>/pasajeros/ -> lista pasajeros del usuario
#     POST /api/users/<user_pk>/pasajeros/ -> crea pasajero para el usuario
#     """
#     serializer_class = PasajeroSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         user_pk = self.kwargs['user_pk']
#         return Pasajero.objects.filter(usuario_id=user_pk)

#     def perform_create(self, serializer):
#         user_pk = self.kwargs['user_pk']
#         usuario = get_object_or_404(User, pk=user_pk)
#         serializer.save(usuario=usuario)


# # -----------------------------------
# # Detalle / Actualización / Eliminación de un pasajero
# # -----------------------------------
# class PasajeroRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     """
#     GET /api/pasajeros/1/ -> detalle pasajero 1
#     PUT /api/pasajeros/1/ -> actualiza pasajero 1
#     PATCH /api/pasajeros/1/ -> actualiza parcialmente pasajero 1
#     DELETE /api/pasajeros/1/ -> elimina pasajero 1
#     """
#     queryset = Pasajero.objects.all()
#     serializer_class = PasajeroSerializer
#     # permission_classes = [IsAuthenticated]

#     def perform_destroy(self, instance):
#         instance.delete()