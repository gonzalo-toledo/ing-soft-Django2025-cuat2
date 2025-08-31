from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.response import Response

from api.serializers import UserSerializer

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