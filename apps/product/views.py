from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.http import JsonResponse

from decimal import Decimal
from apps.store.views import store

from product.models import Product
from store.models import Store

def create_product(request):
    store = get_object_or_404(Store, user=request.user)
    stores = Store.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']

        quantity = request.POST['quantity']
        unity = request.POST['unity']
        quantity = f'{quantity} {unity}'
    
        price = request.POST['price']
        price = price.replace('.', '')
        price = Decimal(price.replace(',', '.'))

        description = request.POST['description']
        image = request.FILES['image']

        product = Product.objects.create(
            store=store,
            name=name, 
            category=category, 
            quantity=quantity, 
            price=price, 
            description=description, 
            image=image,
        )
        product.save()

        button = request.POST['button']
        if button == 'add':
            return redirect(f'/store/{store.id}')
        if button == 'continue':
            return redirect('create_product')
    else:
        context = {
            'store': store,
            'stores': stores,
        }

        return render(request, 'product/create_product.html', context)

def edit_product(request, id):
    pass

def delete_product(request, id):
    pass

def search_product(request, id):
    try:
        product = get_object_or_404(Product, pk=id)
        response = {
            'id': product.id, 
            'name': product.name, 
            'category': product.category, 
            'quantity': product.quantity, 
            'price': product.price, 
            'description': product.description, 
            'image': product.image.url, 
            'created_at': product.created_at,
        } 
    except:
        response = {
            'id': None, 
            'name': None, 
            'category': None, 
            'quantity': None, 
            'price': None, 
            'description': None, 
            'image': None, 
            'created_at': None,
        }
  
    return JsonResponse(response)
