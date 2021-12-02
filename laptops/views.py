from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from .serializers import ProductSerializer
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Product


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter().order_by('id')

    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super(ProductViewSet, self).get_queryset()
        return queryset

    def post(self, request, *args, **kwargs):
        user_data = request.data

        new_user = Product.objects.create(brand=user_data.get(),
                                          name=user_data.get(),
                                          display=user_data.get(),
                                          memory=user_data.get(),
                                          ssd_hdd=user_data.get(),
                                          graphic_card=user_data(),
                                          uses=user_data.get(),
                                          model=user_data.get(),
                                          price=user_data.get(),
                                          image=user_data.get()
                                          )
        new_user.save()
        serializer = ProductSerializer(new_user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        product = request.product
        serializer = ProductSerializer(instance=product, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]
