from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context = {
               "title" : "Home Page",
               "content" : "Welcome to the web page",
              }
    if request.user.is_authenticated is True:
        context["premium_content"] = "YEEEEEAAAAAHHHHHH"

    return render(request, "home_page.html", context)

def contact_page(request):
    form = ContactForm(request.POST or None)
    context = {
               "title" : "Contact",
               "content" : "Welcome to the Contact page", 
               "form" : form
              }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
        # print(request.POST.get('form_full_name'))
        # print(request.POST.get('form_email'))
        # print(request.POST.get('form_content'))
    return render(request, "contact/view.html", context)

def about_page(request):
    context = {
               "title" : "About",
               "content" : "Welcome to the about page"
              }
    return render(request, "home_page.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
               "form" : form
              }
    print("User logged in")
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        print (form.cleaned_data)
        user = authenticate(username=username, password=password)
        # print(user)
        if request.user.is_authenticated is True:
            print("User is authenticated")
        if user is not None:
            login(request, user)
            context['form'] = LoginForm()
            return redirect('/login')
        else:
            print("ERROR")

    return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
               "form" : form
              }
    if form.is_valid():
        print (form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        # print(user)
    return render(request, "auth/register.html", context)

def hello_world(request):
    return HttpResponse("Hello world")
