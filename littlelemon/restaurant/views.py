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

