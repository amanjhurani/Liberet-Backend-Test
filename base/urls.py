from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Product", api.ProductViewSet)
router.register("ShoppingCart", api.ShoppingCartViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("base/Product/", views.ProductListView.as_view(), name="base_Product_list"),
    path("base/Product/create/", views.ProductCreateView.as_view(), name="base_Product_create"),
    path("base/Product/detail/<int:pk>/", views.ProductDetailView.as_view(), name="base_Product_detail"),
    path("base/Product/update/<int:pk>/", views.ProductUpdateView.as_view(), name="base_Product_update"),
    path("base/Order/place", views.place_order, name="place_order"),
)
