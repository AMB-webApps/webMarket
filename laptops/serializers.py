from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    # def post(self, validated_data):
    #     new_product = super().create(validated_data=validated_data)
    #     new_product.save()
    #     return new_product
    #
    # def get(self, request):
    #     product = request.product
    #     serializer = ProductSerializer(instance=product, context={'request': request})
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)
