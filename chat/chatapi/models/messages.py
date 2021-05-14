from django.db import models
from django.core.validators import MinLengthValidator


class Message(models.Model):
    user = models.ForeignKey('chatapi.user', verbose_name=(
        'user'), on_delete=models.CASCADE)
    conversation = models.ForeignKey('chatapi.conversation',
                                     verbose_name=('conversation'),
                                     related_name='messages',
                                     on_delete=models.CASCADE)
    content = models.TextField(validators=[MinLengthValidator(limit_value=1,
                                                              message='El mensaje no contiene texto.')])
    send_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-send_time']

    @property
    def message(self):
        return self.content

    @property
    def sended(self):
        return self.send_time

    @property
    def nickname(self):
        return self.user.nickname

    def __str__(self):
        return '{}'.format(self.pk)
