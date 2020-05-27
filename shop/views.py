from django.shortcuts import render, get_object_or_404
from .models import Category, Product, AddressAndPhone
from cart.forms import *
from django.core.paginator import Paginator


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

def index(request, category_slug=None):
    category = None
    products = Product.objects.all()
    categories = Category.objects.all()


    if category_slug:
        category = get_object_or_404(Category, slug__iexact=category_slug)
        products = Product.objects.filter(category=category)

    pages = Paginator(products, 20)

    if "page" in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1

    page = pages.get_page(page_num)

    context = {"products" : page.object_list, "categories" : categories, "category": category, "page" : page}
    return render(request, 'shop/product/list_2.html', context)

def product_detail_2(request, slug, id):
    product = Product.objects.get(slug__iexact=slug)
    cart_product_form = CartAddProductForm()
    value_form = ValueForm(id)
    context = {"product" : product, "cart_product_form": cart_product_form, 'value_form' : value_form}
    return render(request, "shop/product/detail_2.html", context)

def about_us(request):
    return render(request, "shop/aboutus.html", {})

def locations(request):
    all_locations = AddressAndPhone.objects.all()
    context = {"locations" : all_locations}
    return render(request, "shop/locations_shop.html", context)
