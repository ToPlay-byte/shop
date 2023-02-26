from django.shortcuts import get_object_or_404
from django.urls import  reverse_lazy
from .models import *
from .forms import OrderForm
from django.views.generic import FormView, View, TemplateView, ListView
from cities_light.models import City, Country
from django.http import JsonResponse, QueryDict, HttpResponse
from django.db.models import Q
from apps.catalog.models import Product
from apps.catalog.cart import Cart
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class OrderView(FormView):
    template_name = 'payment/order.html'
    extra_context = {'cities': City.objects.filter(country__name='Andorra')}
    form_class = OrderForm
    success_url = reverse_lazy('payment:success')

    def get(self,  request, *args, **kwargs):
        print(*args)
        get_object_or_404(Product, pk=kwargs['pk'])
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        cart = Cart(self.request)
        data = self.get_cart(cart)
        cart.delete(pk=self.kwargs['pk'])
        self.save_order(form, data)
        return super().form_valid(form)

    def save_order(self, form, data):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        city = form.cleaned_data['cities'].split(', ')[0]
        order = Order()
        order.first_name = form.cleaned_data['first_name']
        order.last_name = form.cleaned_data['last_name']
        order.email = form.cleaned_data['email']
        order.post_code = form.cleaned_data['post_code']
        order.city = City.objects.get(name=city)
        order.country = Country.objects.get(name=form.cleaned_data['country'])
        order.address = form.cleaned_data['address']
        order.total_price = float(data['totalPrice'])
        order.quantity = data['quantity']
        if self.request.user.is_authenticated:
            order.user = self.request.user
        order.product = product
        order.save()


    def get_cart(self, cart):

        data = cart.display().get(self.kwargs['pk'])
        if not data:
            return data
        else:
            product = Product.objects.get(pk=int(self.kwargs['pk']))
            data = {
                'totalPrice': product.price,
                'quantity': 1,
            }
            return  data


class AjaxCitiesView(View):
    def post(self, request):
        country = request.POST['country']
        cities = list(City.objects.filter(country__name=country).values('name', 'region__name', 'country__name'))
        print(cities)
        return JsonResponse({'cities': cities})

    def put(self, request):
        data = QueryDict(request.body)
        cities = list(City.objects.filter(Q(country__name=data['country']) & Q(name__icontains=data['city'])).values('name', 'region__name', 'country__name'))
        return JsonResponse({'cities': cities})


class SuccessView(TemplateView):
    template_name = 'payment/success.html'


class OrdersList(ListView, LoginRequiredMixin):
    template_name = 'payment/orders_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('active')


class AjaxDeleteOrderView(View):
    def post(self, request, *args, **kwargs):
        pk = request.POST['pk']
        Order.objects.get(Q(user=request.user) & Q(pk=pk)).delete()
        return HttpResponse()
