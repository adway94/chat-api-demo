from django.contrib import admin
from .models import Conversation
from .models import User
# Register your models here.

admin.site.register(Conversation)
admin.site.register(User)
