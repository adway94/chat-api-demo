from rest_framework import viewsets
from chat.chatapi.models import User
from chat.chatapi.serializers import UserRegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    http_method_names = ['POST', 'GET']


class RegisterUserViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    http_method_names = ['POST']
