from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .serializers import ProductSerializer
from .models import Product
# Create your views here.

class ProductDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductsList(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
