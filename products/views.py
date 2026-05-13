from django.shortcuts import render

from django.db.models import Q

from django.shortcuts import render, redirect

from .models import Product, Category, Review, Wishlist
def home(request):

    query = request.GET.get('q')

    category_id = request.GET.get('category')

    products = Product.objects.all()

    if query:

        products = products.filter(

            Q(title__icontains=query) |

            Q(description__icontains=query)

        )

    if category_id:

        products = products.filter(category_id=category_id)

    categories = Category.objects.all()

    context = {

        'products': products,

        'categories': categories
    }

    return render(request, 'home.html', context)

def product_detail(request, id):
    

    product = Product.objects.get(id=id)

    reviews = Review.objects.filter(product=product)

    if request.method == 'POST':

        rating = request.POST['rating']

        comment = request.POST['comment']

        Review.objects.create(

            product=product,

            user=request.user,

            rating=rating,

            comment=comment
        )

    context = {

        'product': product,

        'reviews': reviews
    }

    return render(request, 'product_detail.html', context)

def add_to_wishlist(request, id):

    product = Product.objects.get(id=id)

    Wishlist.objects.get_or_create(

        user=request.user,

        product=product
    )

    return redirect('wishlist')


def wishlist(request):

    wishlist_items = Wishlist.objects.filter(

        user=request.user
    )

    context = {

        'wishlist_items': wishlist_items
    }

    return render(request, 'wishlist.html', context)


def remove_wishlist(request, id):

    item = Wishlist.objects.get(id=id)

    item.delete()

    return redirect('wishlist')