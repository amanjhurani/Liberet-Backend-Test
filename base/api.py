from rest_framework import viewsets, permissions
from django.contrib.auth.models import User

from . import serializers
from . import models


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for the Product class"""

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class ShoppingCartViewSet(viewsets.ModelViewSet):
    """ViewSet for the Product class"""

    queryset = models.ShoppingCart.objects.all()
    serializer_class = serializers.ShoppingCartSerializer
    permission_classes = [permissions.IsAuthenticated]