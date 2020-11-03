from rest_framework import viewsets
from ..models.greeting import Greeting
from ..serializer import GreetingSerializer


class GreetingViewSet(viewsets.ModelViewSet):
    queryset = Greeting.objects.all()
    serializer_class = GreetingSerializer
