from chat.chatapi.models import Conversation, Message
from rest_framework import serializers
from datetime import datetime


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('nickname', 'conversation', 'content', 'send_time',)
        read_only_fields = ('send_time',)
        ref_name = 'messages'

    def create(self, request):

        conversationObject = Conversation.objects.filter(
                             pk=request['conversation'].id)

        user = self.context.get('request').user
        conversation = conversationObject
        content = request['content']

        message = Message.objects.create(user=user,
                                         conversation=conversation[0],
                                         content=content)

        conversationObject.updated_at = datetime.now()

        return message
