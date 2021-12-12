from .models import Bags
from rest_framework import generics
from .serializers import BagSerializer


class Baglist(generics.ListCreateAPIView):
    queryset = Bags.objects.all()
    serializer_class = BagSerializer


class BagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bags.objects.all()
    serializer_class = BagSerializer