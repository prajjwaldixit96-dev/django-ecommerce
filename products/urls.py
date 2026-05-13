from django.urls import path

from .views import *

urlpatterns = [

    path('', home, name='home'),

    path('product/<int:id>/',
         product_detail,
         name='product_detail'),

    path('wishlist/',
         wishlist,
         name='wishlist'),

    path('add-wishlist/<int:id>/',
         add_to_wishlist,
         name='add_to_wishlist'),

    path('remove-wishlist/<int:id>/',
         remove_wishlist,
         name='remove_wishlist'),
]