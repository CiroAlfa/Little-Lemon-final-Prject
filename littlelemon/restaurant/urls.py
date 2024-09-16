from django.contrib import admin 
from django.urls import path, include
from rest_framework import routers

#from .views import sayHello 
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    #path('', sayHello, name='sayHello'),
    path('', include(router.urls)),
    path('', views.index, name='index' ),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

    
    ]