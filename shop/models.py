from django.db import models
from django.urls import reverse

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
    value = models.DecimalField(max_digits=10, decimal_places = 1, null=True)
    another_price = models.DecimalField(max_digits=10, decimal_places = 2, null=True)

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Величина и цена'
        verbose_name_plural = "Величины и цены"
