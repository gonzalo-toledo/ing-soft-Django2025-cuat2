from django.urls import path
from api.views import (
    UserListCreateView,
    UserRetrieveUpdateDestroyView,
    RegistroCreateView,
    # PasajeroNuevoCreateView,
    # PasajeroRetrieveUpdateDestroyView,
    PasajeroListCreateView
)

urlpatterns = [
    # USERS
    path('users/', UserListCreateView.as_view(), name='users-list'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='users-detail'),

    # PASAJEROS
    path('users/<int:user_pk>/pasajeros/', PasajeroListCreateView.as_view(), name='pasajeros-list'),

    # USER + PASAJERO
    path('registro/', RegistroCreateView.as_view(), name='registro'),
    


#     # REGISTRO INICIAL (usuario + pasajero)
#     path('registro/', RegistroCreateView.as_view(), name='registro'),

#     # PASAJEROS ADICIONALES (usuario logueado)
#     path('pasajeros/nuevo/', PasajeroNuevoCreateView.as_view(), name='pasajero-nuevo'),
    
#     path('users/<int:user_pk>/pasajeros/', PasajeroListCreateView.as_view(), name='pasajeros-list'),

#     # DETALLE / ACTUALIZACION / ELIMINACION DE PASAJERO
#     path('pasajeros/<int:pk>/', PasajeroRetrieveUpdateDestroyView.as_view(), name='pasajero-detail'),
]