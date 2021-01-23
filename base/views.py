from django.views import generic
from . import models
from . import forms
# from .models import *
from django.contrib.auth.models import User




class ProductListView(generic.ListView):
    model = models.Product
    form_class = forms.ProductForm


class ProductCreateView(generic.CreateView):
    model = models.Product
    form_class = forms.ProductForm


class ProductDetailView(generic.DetailView):
    model = models.Product
    form_class = forms.ProductForm


class ProductUpdateView(generic.UpdateView):
    model = models.Product
    form_class = forms.ProductForm
    pk_url_kwarg = "pk"


def place_order(request):
    if request == "POST":
        user_name = request.user.username
        cart = models.ShoppingCart.objects.filter(user_name__username = request.user.username)
        product_detail = ""
        total_price = 0
        for product in cart:
            product_detail += (cart.product__product_name)
            total_price += (cart.product__product_amount)
        delivery_fee = 20
        total_price += delivery_fee


        new_order = models.Order.objects.create(
            user_name=user_name,
            product_detail= product_detail,
            delivery_fee=delivery_fee,
            total_price = total_price
        )

    else:
        return models.Order.objects.filter(user_name__username = request.user.username)

