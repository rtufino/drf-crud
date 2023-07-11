from rest_framework import routers
from django.urls import path
from .api import ProjectViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')
# router.register('api/token-auth', obtain_auth_token, 'api_token_auth')

urlpatterns = router.urls

urlpatterns.append(path('api/token-auth', obtain_auth_token, name='api_token_auth'))