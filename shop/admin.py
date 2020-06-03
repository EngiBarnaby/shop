from django.contrib import admin
from .models import *

class ValueAndPricesLine(admin.TabularInline):
    model = ValueAndPrices
    extra = 1
# class value_inline(admin.TabularInline):
#     model = ValueAndPrices
#     extra = 1

class SubcategoryinLine(admin.TabularInline):
    model = Subcategory.products.through
    extra = 1

@admin.register(Sort)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['sorts']

@admin.register(Region)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['regions']

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = [ 'available']
    prepopulated_fields = {'slug': ('name',)}
    # inlines = (value_inline,)
    inlines = [
        ValueAndPricesLine,
        SubcategoryinLine,
    ]

@admin.register(AddressAndPhone)
class AddressAndPhoneForm(admin.ModelAdmin):
    list_display = ['address', 'phone_number', 'map_image']

admin.site.register(ValueAndPrices)
