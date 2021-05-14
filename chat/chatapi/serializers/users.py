from chat.chatapi.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'nickname', 'created_at']


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50)
    nickname = serializers.CharField(min_length=6)

    class Meta:
        model = User
        fields = ('email', 'password', 'nickname')
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

    def create(self, request):
        email = User.objects.filter(email=request['email'])
        nickname = User.objects.filter(nickname=request['nickname'])

        if nickname:
            raise serializers.ValidationError(
                {'detail': 'El nickname ya esta en uso'})
        if email:
            raise serializers.ValidationError(
                {'detail': 'El email ya esta en uso'})

        user = User.objects.create_user(email=request['email'],
                                        password=request['password'],
                                        nickname=request['nickname'],)

        return user
