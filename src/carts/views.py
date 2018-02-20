from django.shortcuts import render

from .models import Cart


def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    return cart_obj

def cart_home(request): # why there is no self arg?
    # del request.session['cart_id']
    cart_id = request.session.get("cart_id", None)
    # if cart_id is None and isinstance(cart_id, int):
        # print('create new cart')
        # cart_obj = cart_create()
        # # request.session['cart_id'] = 2
    # else:
    qs = Cart.objects.filter(id=cart_id)
    if qs.count()==1:
        print("Cart ID exists")
        print(cart_id)
        cart_obj = qs.first()
    else:
        print('create new cart')
        cart_obj = cart_create()
        request.session['cart_id']=cart_obj.id
    # cart_obj = Cart.objects.get(id=cart_id)
    # print(request.session)
    # print(dir(request.session))
    return render(request, "carts/home.html", {})
