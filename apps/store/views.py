from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User

from store.models import Store
from product.models import Product

def store(request, id):
    store = get_object_or_404(Store, pk=id)
    stores = Store.objects.all()
    products = Product.objects.filter(store=store)
    
    context = {
        'stores': stores,
        'store': store,
        'products': products,
    }

    return render(request, 'store/store.html', context)

def create_store(request):
    stores = Store.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        district = request.POST['district']
        address = request.POST['address']
        number = request.POST['number']
        state = request.POST['state']
        city = request.POST['city']
        phone = request.POST['phone']

        user = get_object_or_404(User, pk=request.user.id)

        store = Store.objects.create(
            user=user,
            name=name, 
            district=district, 
            address=address, 
            number=number, 
            state=state, 
            city=city, 
            phone=phone
        )
        store.save()

        user.is_staff = True
        user.save()
        return redirect('dashboard')
    else:
        context = {
            'stores': stores,
        }

        return render(request, 'store/create_store.html', context)

def edit_store(request, id):
    store = get_object_or_404(Store, pk=id)
    stores = Store.objects.all()

    if request.method == 'POST':
        store.name = request.POST['name']
        store.district = request.POST['district']
        store.address = request.POST['address']
        store.number = request.POST['number']
        store.state = request.POST['state']
        store.city = request.POST['city']
        store.phone = request.POST['phone']
        store.save()
        return redirect(f'/store/{store.id}')
    else:
        context = {
            'stores': stores,
            'store': store,
        }

        return render(request, 'store/edit_store.html', context)

def delete_store(request, id):
    store = get_object_or_404(Store, pk=id)

