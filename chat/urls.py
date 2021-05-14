"""chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from rest_framework.authtoken.views import obtain_auth_token
from chat.chatapi import views

schema_view = get_schema_view(
    openapi.Info(
        title="Chat Api",
        default_version='v1',
        description="Aplicacion creada para demo de DevsAr",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.SimpleRouter()

router.register(r'register', views.RegisterUserViewSet)
router.register(r'api/users', views.UserViewSet)
router.register(r'api/conversations', views.ConversationViewSet)
router.register(r'api/conversations',
                views.ObteinConversationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'swagger/$', schema_view.with_ui('swagger',
                                              cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
                                             cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('login/', obtain_auth_token, name='login'),
]
