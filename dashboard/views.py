from django.shortcuts import render

from products.models import Product

from orders.models import Order

from django.contrib.auth.models import User

from django.db.models import Sum


def dashboard_view(request):

    total_products = Product.objects.count()

    total_orders = Order.objects.count()

    total_users = User.objects.count()

    revenue = Order.objects.aggregate(

        Sum('total_price')
    )['total_price__sum']

    context = {

        'total_products': total_products,

        'total_orders': total_orders,

        'total_users': total_users,

        'revenue': revenue
    }

    return render(request,
                  'dashboard.html',
                  context)