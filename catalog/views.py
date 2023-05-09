from django.shortcuts import render

from catalog.models import Product, Contact, Category


def home(request):
    last_products = Product.objects.order_by('-created_date')[:5]
    for product in last_products:
        print(product.name)
    context = {
        "category_list": Category.objects.all(),
        "product_list": Product.objects.all()[:3],
        "title": "Товары месяца"
    }
    return render(request, 'catalog/home.html', context)


def catalog(request):
    context = {
        "category_list": Category.objects.all(),
        "product_list": Product.objects.all(),
        "title": "Каталог товаров"
    }
    return render(request, 'catalog/catalog.html', context)


def product_items(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'product': product_item,
        'title': product_item.name
    }
    return render(request, 'catalog/product_items.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Contact(name=name, phone=phone, message=message).save()
        print(f'You have new message from {name}({phone}): {message}')
    context = {
        "title": "Обратная связь"
    }
    return render(request, 'catalog/contacts.html', context)
