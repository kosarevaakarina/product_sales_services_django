from django.shortcuts import render

from catalog.models import Product, Contact


def home(request):
    last_products = Product.objects.order_by('-created_date')[:5]
    for product in last_products:
        print(product.name)
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Contact(name=name, phone=phone, message=message)
        print(f'You have new message from {name}({phone}): {message}')
    return render(request, 'catalog/contacts.html')
