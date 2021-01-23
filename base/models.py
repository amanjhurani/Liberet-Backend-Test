from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

class Product(models.Model):

    # Fields
    product_name = models.CharField(max_length= 100)
    product_amount = models.IntegerField(default=0)
    product_supplier = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("base_Product_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("base_Product_update", args=(self.pk,))


class ShoppingCart(models.Model):
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    service_date = models.DateTimeField(auto_now_add=True, editable=False)
    delivery_type = models.CharField(max_length= 500)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    def __str__(self):
        return str(self.user_name.username+"--"+self.product.product_name +" - "+ self.product.product_supplier + " - " + str(self.product.product_amount))

class Order(models.Model):
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product_detail = models.CharField(max_length=1000)
    delivery_fee = models.IntegerField()
    total_price = models.IntegerField()