from chat.chatapi.models import Conversation, Message, User
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('nickname', 'message', 'sended',)


class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = '__all__'
        ref_name = 'conversations'

    def create(self, request):

        user_one = self.context.get('request').user
        user_two = User.objects.all().filter(email=request['user_two'])

        if user_one == user_two[0]:
            raise serializers.ValidationError(
                {'detail': 'El usuario es el mismo'})

        if not user_one or not user_two:
            raise serializers.ValidationError(
                {'detail': 'El usuario no existe'})

        if self._does_conversation_exits(user_one, user_two[0]):
            raise serializers.ValidationError(
                {'detail': 'La conversacion ya existe'})
        else:
            conversation = Conversation.objects.create(user_one=user_one,
                                                       user_two=user_two[0])
            conversation.save()

        return conversation

    def _does_conversation_exits(self, user_one: object, user_two: object) -> bool:
        conversation_exist = Conversation.objects.filter(user_one_id__in=[user_one.id, user_two.id],
                                                         user_two_id__in=[user_one.id, user_two.id]).exists()
        return conversation_exist
