


from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.template import loader
from .models import Product
 
def index(request):
    product_list = Product.objects.order_by('-product_price')[:10]
    template = loader.get_template('spend_money/index.html')
    context = {
        'product_list': product_list,
    }
    return HttpResponse(template.render(context, request))

