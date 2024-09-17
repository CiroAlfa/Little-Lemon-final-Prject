from django.contrib import admin 
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
#from .views import sayHello 
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    #path('', sayHello, name='sayHello'),
    path('', include(router.urls)),
    path('', views.index, name='index' ),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),


    
    ]