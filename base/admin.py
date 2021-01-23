from django.contrib import admin
from django import forms

from . import models


class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = "__all__"


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = [
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]



admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ShoppingCart)
