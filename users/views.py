# users/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .models import Gerente
from .serializers import RegisterSerializer

User = get_user_model()

class RegisterView(viewsets.ModelViewSet):
    queryset = Gerente.objects.all()
    serializer_class = RegisterSerializer

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        # Debugging lines
        print(f"Email: {email}")
        print(f"Password: {password}")

        user = authenticate(request, username=email, password=password)
        
        # More debugging
        if user is None:
            print("Autenticação falhou.")
        else:
            print("Usuário autenticado com sucesso.")
            print(f"User: {user.email}, is_active: {user.is_active}")

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)