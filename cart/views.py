from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .cart import Cart
from shop.models import Product
from django.views.decorators.http import require_POST
from .forms import CartAddProductForm, ValueForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    value_form = ValueForm(product_id, request.POST)
    if form.is_valid() and value_form.is_valid():
        cd = form.cleaned_data
        cd2 = value_form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'], size=cd2['size'])
        return redirect('cart:cart_detail')
    else:
        return HttpResponse()


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    if cart:
        return redirect('cart:cart_detail')
    else:
        return redirect("/")

def cart_detail(request):
    cart = Cart(request)
    context = {'cart' : cart}
    return render(request, 'cart/detail.html', context)

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('/')
