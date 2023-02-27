from .cart import Cart


def cart(request):
    cart_list = Cart(request).display()
    cart_length = len(cart_list)
    return {'cart': cart_list, 'cart_length': cart_length}
