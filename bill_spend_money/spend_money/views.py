from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from .models import Products

# Create your views here.
def index(request):
    products_list = Products.objects.order_by('-product_price')[:10]
    template = loader.get_template('spend_money/bill_spend_page.html')
    context = {
        'products_list': products_list,
    }
    return HttpResponse(template.render(context, request))