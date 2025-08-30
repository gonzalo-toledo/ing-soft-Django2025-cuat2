from django.contrib.auth.models import User
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

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