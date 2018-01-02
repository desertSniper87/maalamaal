from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Product

class ProductFeaturedView(ListView):
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
        # context = super(ProductFeaturedView, self).get_context_data(*args, **kwargs)
        # print(context)
        # return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured-detail.html"

    # def get_context_data(self, *args, **kwargs):
        # context = super(ProductFeaturedDetailView, self).get_context_data(*args, **kwargs)
        # print(context)
        # # context['abc'] = '123'
        # return context

    # def get_object(self, *args, **kwargs):
        # request = self.request
        # pk = self.kwargs.get('pk')
        # instance = Product.objects.get_by_id(pk)
        # if instance == None:
            # raise Http404("Product does not exist")
        # return instance


class ProductListView(ListView):
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
        # context = super(ProductListView, self).get_context_data(*args, **kwargs)
        # print(context)
        # return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
               'object_list' : queryset
              }
    return render(request, "products/list.html", context)


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # return Product.objects.get(slug=slug, active=True)


        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug = slug, active = True)
            instance = qs.first()
        except:
            raise Http404("Hmmm")
        return instance


class ProductDetailView(DetailView):
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        # context['abc'] = '123'
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance == None:
            raise Http404("Product does not exist")
        return instance
    
def product_detail_view(request, pk=None, *args, **kwargs):
    instance = Product.objects.get_by_id(pk)
    print(instance)
    if instance is None:
        raise Http404("Product does not exist")

    # qs = Product.objects.filter(id=pk)
    # if qs.exists() and qs.count()==1:
        # instance = qs.first()
    # else:

    context = {
               'object' : instance 
              }
    print(context)
    return render(request, "products/detail.html", context)
