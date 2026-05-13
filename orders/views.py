from django.shortcuts import render, redirect

from cart.models import Cart

from .models import Order
import razorpay

from django.conf import settings



def checkout(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:

        total += item.product.price * item.quantity

    total_in_paise = total * 100

    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )

    payment = client.order.create({

        'amount': total_in_paise,

        'currency': 'INR',

        'payment_capture': '1'
    })

    if request.method == 'POST':

        address = request.POST['address']

        for item in cart_items:

            Order.objects.create(

                user=request.user,

                product=item.product,

                quantity=item.quantity,

                total_price=item.product.price * item.quantity,

                address=address
            )

        cart_items.delete()

        return redirect('my_orders')

    context = {

        'cart_items': cart_items,

        'total': total,

        'payment': payment,

        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
    }

    return render(request, 'checkout.html', context)

def my_orders(request):

    orders = Order.objects.filter(user=request.user)

    context = {
        'orders': orders
    }

    return render(request, 'my_orders.html', context)