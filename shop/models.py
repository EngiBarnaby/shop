from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

class Category(models.Model):
    name = models.CharField(max_length = 100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    products = models.ManyToManyField("Product", related_name="subcategories")


    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегорий'

    def get_absolute_url(self):
        return reverse("shop:product_list_by_subcategory", args=[self.slug])


class Sort(models.Model):
    sorts = models.CharField(max_length=150)

    def __str__(self):
        return self.sorts

class Region(models.Model):
    regions = models.CharField(max_length=150)

    def __str__(self):
        return self.regions

class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length = 200, db_index = True)
    slug = models.SlugField(max_length = 200, db_index = True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    # price = models.DecimalField(max_digits=10, decimal_places = 2, null=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sort = models.ForeignKey("Sort", related_name="product_sort", on_delete=models.CASCADE, null=True)
    region = models.ForeignKey("Region", related_name="product_region", on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])

class ValueAndPrices(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="prices")
    value = models.DecimalField(max_digits=10, decimal_places = 3, null=True)
    another_price = models.DecimalField(max_digits=10, decimal_places = 2, null=True)
    image = models.ImageField(upload_to='products/%Y/%d/%m',blank=True)

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Величина и цена'
        verbose_name_plural = "Величины и цены"

class AddressAndPhone(models.Model):
    address = models.TextField()
    map_image = models.ImageField(upload_to='map_image',blank=True)
    phone_number = models.CharField(max_length=25)

    def __str__(self):
        return str(self.address)

    class Meta:
        verbose_name = "Адрес и номер телефона"
        verbose_name_plural = "Адреса и номера телефонов"
