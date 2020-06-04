from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import *
from django.core.paginator import Paginator
from .filters import ProductFilter

# def product_list(request, category_slug=None):
#     category = None
#     products = Product.objects.all()
#     categories = Category.objects.all()
#     if category_slug:
#         category = get_object_or_404(Category, slug__iexact=category_slug)
#         products = Product.objects.filter(category=category)
#     context = {"products" : products, "categories": categories, "category":category}
#     return render(request, "shop/product/list.html", context)
def is_valid_queryparam(param):
    return param != '' and param is not None


def product_list(request, category_slug=None):
    category = None
    products = Product.objects.all()
    categories = Category.objects.all()
    sorts = Sort.objects.all()
    regions = Region.objects.all()

    name_contains = request.GET.get('name_contains')
    sort = request.GET.get('sort')
    region = request.GET.get('region')


    if category_slug:
        category = get_object_or_404(Category, slug__iexact=category_slug)
        products = Product.objects.filter(category=category)

    if is_valid_queryparam(name_contains):
        products = products.filter(name__icontains=name_contains)

    if is_valid_queryparam(sort) and sort != "Выбор...":
        products = products.filter(sort__sorts=sort)

    if is_valid_queryparam(region) and region !="Выбор...":
        products = products.filter(region__sorts=region)

    pages = Paginator(products, 20)

    if "page" in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1

    page = pages.get_page(page_num)

    products_page = page.object_list

    # sort_form = ProductFilter(request.GET, queryset=products)
    #
    # products_page = sort_form.qs

    context = {"products" : products_page, "categories" : categories, "category": category, "page" : page,
                    "sorts" : sorts, "regions" : regions}
    return render(request, 'shop/product/list_2.html', context)

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
    context = {"products" : products, "categories" : categories, "category": category}
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
