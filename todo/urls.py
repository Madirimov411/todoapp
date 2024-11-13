from rest_framework import routers
from .api import TodoViewSet

routers = routers.DefaultRouter()
routers.register('api/todo', TodoViewSet, 'todo')

urlpatterns = routers.urls
