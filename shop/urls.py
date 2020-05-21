from django.urls import path
from .models import *
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', index, name='product_list'),
    path('aboutus/', about_us, name="about_us"),
    path("locations_shop", locations, name="locations"),
    path('<slug:category_slug>/', index, name="product_list_by_category"),
    path('<int:id>/<str:slug>/detail/', product_detail_2, name="product_detail"),
    # path('abc', product_list, name="product_list"),
    # path('<int:id>/<str:slug>/detail/', product_detail, name="product_detail"),
]
