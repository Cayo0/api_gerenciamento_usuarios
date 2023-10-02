from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UsuarioSerializer
from .models import UsuarioPersonalizado


class UsuariosViewSet(viewsets.ModelViewSet):
    """
    Uma ViewSet para realizar operações crud em objetos do modelo UsuarioPersonalizado.
    Utiliza o serializer UsuarioSerializer para serialização e desserialização.
    Requer autenticação JWT (JSON Web Token) para acesso e permissão de autenticação.
    """
    serializer_class = UsuarioSerializer
    queryset = UsuarioPersonalizado.objects.all()
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]
    
