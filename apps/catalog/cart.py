from decimal import Decimal
from django.conf import settings
from django.http import QueryDict, HttpResponse, JsonResponse
from .models import Product


class Cart(object):
    def __init__(self, request):
        self.data = QueryDict(request.body)
        self.pk = self.data.get('pk')
        self.quantity = self.data.get('quantity')
        self.session = request.session
        cart = self.session.get(settings.BASKET_SESSION)
        if not cart:
            cart = self.session[settings.BASKET_SESSION] = {}
        self.cart = cart

    def save(self):
        self.session.modified = True

    def post(self):
        product = Product.objects.get(pk=self.pk)
        cart = None
        if self.pk not in self.cart.keys():
            cart = self.cart[self.pk] = {
                'poster': str(product.poster.url),
                'name': str(product.name),
                'price': float(product.price),
                'quantity': 1,
                'totalPrice': str(product.price)
                }
            self.save()
        return {'item': cart, 'id': self.pk, 'cartCounter': len(self.display())}

    def put(self):
        quantity = int(self.data['quantity'])
        cart = None
        if self.pk in self.cart.keys():
            cart = self.cart[self.pk]
            cart['quantity'] = quantity
            price = cart['price']
            cart['totalPrice'] = str(Decimal(price * quantity).quantize(Decimal('1.00')))
            self.save()
        return cart

    def delete(self, pk=None):
        print(pk)
        pk = pk if pk else self.pk
        if pk in self.cart.keys():
            del self.cart[pk]
            self.save()

    def display(self):
        return self.cart.copy()







