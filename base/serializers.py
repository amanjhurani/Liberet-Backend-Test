from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = [
            "created",
            "last_updated",
            "product_name",
            "product_amount",
            "product_supplier"
        ]

class ShoppingCartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.ShoppingCart
        fields = [
            "user_name",
            "product",
            "service_date",
            "delivery_type",
            "last_updated"
        ]



