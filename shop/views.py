from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import *

def product_list(request, category_slug=None):
    category = None
    products = Product.objects.all()
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug__iexact=category_slug)
        products = Product.objects.filter(category=category)
    context = {"products" : products, "categories": categories, "category":category}
    return render(request, "shop/product/list.html", context)

def product_detail(request, slug, id):
    product = Product.objects.get(slug__iexact=slug)
    # cart_product_form.fields['size'] = values
    cart_product_form = CartAddProductForm()
    value_form = ValueForm(id)
    # cart_product_form.fields['size'].choices = values
    context = {"product" : product, "cart_product_form": cart_product_form, 'value_form' : value_form}
    return render(request, "shop/product/detail.html", context)
