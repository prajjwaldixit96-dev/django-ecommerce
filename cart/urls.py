from django.urls import path

from . import views

urlpatterns = [

    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('', views.cart_page, name='cart'),

    path('remove/<int:cart_id>/', views.remove_cart, name='remove_cart'),
]