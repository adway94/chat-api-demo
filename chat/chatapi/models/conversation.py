from django.db import models
from datetime import datetime


class Conversation(models.Model):
    user_one = models.ForeignKey(
        'chatapi.user', related_name='userOne', on_delete=models.CASCADE)
    user_two = models.ForeignKey(
        'chatapi.user', related_name='userTwo', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '{}'.format(self.pk)
