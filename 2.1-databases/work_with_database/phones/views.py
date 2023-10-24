from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones_list = Phone.objects.all()
    template = 'catalog.html'
    sort_phone = request.GET.get('sort')
    if sort_phone == 'name':
        phones_list = Phone.objects.all().order_by('name')
    elif sort_phone == 'min_price':
        phones_list = Phone.objects.all().order_by('price')
    elif sort_phone == 'max_price':
        phones_list = Phone.objects.all().order_by('-price')
    context = {'phones': phones_list}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
