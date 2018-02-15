from django.shortcuts import render

# Create your views here.
def cart_home(request): # why there is no self arg?
    print(request.session)
    print(dir(request.session))
    return render(request, "carts/home.html", {})
