from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

'''def sayHello(request):
 return HttpResponse('Hello World')

from django.shortcuts import render'''

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
# views.py
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


