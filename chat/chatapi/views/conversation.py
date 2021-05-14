from django.db.models import Q
from chat.chatapi.models import Conversation, Message
from chat.chatapi.serializers import ConversationSerializer, MessageSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['POST', 'GET']

    def create(self, request):
        request.data['user_one'] = request.user.id
        conversation = self.get_serializer(data=request.data)
        conversation.is_valid(raise_exception=True)
        conversation.save()

        return Response(conversation.data.copy())

    def get_queryset(self):

        return Conversation.objects.filter(Q(user_one=self.request.user) | Q(user_two=self.request.user))


class ObteinConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['delete', 'put', 'post', 'get'], detail=True)
    def messages(self, request, pk=None):
        if request.method == 'GET':
            messages_sended = Message.objects.filter(conversation_id=pk)
            serializer = MessageSerializer(messages_sended, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            request.data['user'] = request.user.id
            request.data['content'] = request.data['message']
            request.data['conversation'] = pk
            message = self.get_serializer(data=request.data)
            message.is_valid(raise_exception=True)
            message.save()
            return Response(message.data.copy())

        elif request.method == 'DELETE':
            last_message = Message.objects.filter(
                conversation_id=pk, user_id=request.user.id).first()
            if last_message:
                last_message = last_message.delete()
                return Response({'Detail': 'Ultimo Mensaje borrado exitosamente'})
            else:
                return Response({'Detail': 'El usuario no es el dueño del ultimo mensaje o no existe mensaje para borrar'})

        elif request.method == 'PUT':
            last_message = Message.objects.filter(
                conversation_id=pk, user_id=request.user.id).first()
            if last_message:
                last_message.content = request.data['message']
                last_message.save()
                return Response({'Detail': 'Ultimo Mensaje se actualizo exitosamente'})
            else:
                return Response({'Detail': 'El usuario no es el dueño del ultimo mensaje o no existe mensaje para editar'})
