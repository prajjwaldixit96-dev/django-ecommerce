from django.shortcuts import render, redirect

from .models import Cart

from products.models import Product


def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:

        cart_item.quantity += 1

        cart_item.save()

    return redirect('cart')


def cart_page(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:

        total += item.product.price * item.quantity

    context = {
        'cart_items': cart_items,
        'total': total
    }

    return render(request, 'cart.html', context)


def remove_cart(request, cart_id):

    cart_item = Cart.objects.get(id=cart_id)

    cart_item.delete()

    return redirect('cart')