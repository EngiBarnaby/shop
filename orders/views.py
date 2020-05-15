from django.shortcuts import render
from .models import *
from .forms import OrderForm
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product = item['product'],
                                        price = item['price'], quantity = item['quantity'], size = item['size'])

            cart.clear()
            context = {'order' : order}
            return render(request, 'orders/order/created.html', context)
    else:
        form = OrderForm()
        context = {'form' : form, 'cart': cart}
        return render(request, 'orders/order/create.html', context)
