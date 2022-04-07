from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="index"),
    path('product/<int:pk>/', views.product, name="product"),
    path('cart/', views.cart, name="cart"),
]
