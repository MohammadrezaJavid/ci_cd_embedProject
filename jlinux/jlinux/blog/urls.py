from django.urls import path, include
from jlinux.blog.apis.products import ProductApi

urlpatterns = [
    path('product/', ProductApi.as_view(), name="product")
]