from decimal import Decimal
from shop.models import Product
from django.conf import settings

class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, size=1, update_quantity=False):
        product_id = str(product.id) + str(size)
        price = 0
        for i in product.prices.values():
            if str(i['value']) == size:
                price = i['another_price']
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(price), 'size': size, 'true_product_id' : product.id}

        if update_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity


        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        # product_ids = (i['true_product_id'] for i in product_ids)
        # products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for item in cart.keys():
            cart[item]['product'] = Product.objects.get(id = cart[item]['true_product_id'])

        # for product in products:
        #     cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item["price"]) * item["quantity"] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
