from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from hashlib import sha256

from .models import *

# User
def register(request):
    return render(request, 'auth/register.html')

def validate_register(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirmPassword = request.POST.get('confirmPassword')

    user = User.objects.filter(email = email)

    # validation

    # check if the password and password confirmation are the same
    if password != confirmPassword:
        messages.warning(request, 'A senha e a confirmação de senha precisam ser iguais!')
        return redirect('/register')

    # check if the password is longer than 8 characters
    if len(password) < 8:
        messages.warning(request, 'Sua senha deve ter pelo menos 8 caracteres!')
        return redirect('/register')

    # check if user exists
    if len(user) > 0:
        messages.warning(request, 'Por favor, utilize outro e-mail!')
        return redirect('/register')

    try:
        password = sha256(password.encode()).hexdigest()
        user = User.objects.create_user(name, email, password, first_name=name)

        # Designa se este usuário pode acessar o site de administração
        user.is_staff = True
        user.save()
    
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('/register')
    except:
        messages.warning(request, 'Erro interno do sistema!')
        return redirect('/register')

def login(request):
    return render(request, 'auth/login.html') 

def validate_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    # validation
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        password = sha256(password.encode()).hexdigest()
        
        if User.objects.filter(email=email).exists():

            username = User.objects.get(email=email).username

            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('/')

    if not request.user.is_authenticated:
        messages.warning(request, 'E-mail ou senha inválidos!')
        return redirect('/login')
    
    else:
        return redirect('/')

def logout(request):
    auth.logout(request)
    messages.info(request, 'Logout realizado com sucesso!')
    return redirect('/')    

# Store
def home(request):
    try:
        stores = Store.objects.all().order_by('name')
    except Store.DoesNotExist:
        stores = None

    if request.user.is_authenticated:     
        try:
            my_store = stores.get(user=request.user)
        except:
            my_store = None

        return render(request, 'home.html', {'stores': stores, 'my_store': my_store})
    else:
        return render(request, 'home.html', {'stores': stores})

@login_required
def create_store(request):
    if request.method == 'POST':
        user = request.user

        name = request.POST.get('name')
        district = request.POST.get('district')
        address = request.POST.get('address')
        number = request.POST.get('number')
        state = request.POST.get('state')
        city = request.POST.get('city')
        phone = request.POST.get('phone')

        store = Store(
            name = name,
            district = district,
            address = address,
            number = number,
            state = state,
            city = city,
            phone = phone,
            user = user
        )

        store.save()

        messages.success(request, 'Loja criada com sucesso.')
    
        return redirect('/')

    else:
        return render(request, 'create_store.html') 

def store(request, id):
    store = Store.objects.get(id = id)
    
    try:
        products = Product.objects.filter(store = store).order_by('-name')
    except Store.DoesNotExist:
        products = None

    try:
        my_store = Store.objects.get(user=request.user)
    except:
        my_store = None

    return render(request, 'store.html', {'store': store, 'my_store': my_store, 'products': products})

@login_required
def update_store(request, id):
    store = Store.objects.get(id = id)

    if request.method == 'POST':
        store.user = request.user

        store.name = request.POST.get('name')
        store.district = request.POST.get('district')
        store.address = request.POST.get('address')
        store.number = request.POST.get('number')
        store.state = request.POST.get('state')
        store.city = request.POST.get('city')
        store.phone = request.POST.get('phone')

        store.save()

        messages.success(request, 'Loja atualizada com sucesso.')
    
        return redirect(f'/store/{store.id}')

    else:
        return render(request, 'home.html') 

@login_required
def create_product(request, id):
    store = Store.objects.get(id = id)

    if request.method == 'POST':

        image = request.FILES.get('image')
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        description = request.POST.get('description')

        quantity_number = request.POST.get('quantity_number')
        quantity_type = request.POST.get('quantity_type')

        print(quantity_number)
        print(type(quantity_number))
        print(quantity_type)
        print(type(quantity_type))

        quantity = str(quantity_number) + " " + quantity_type

        print(quantity)

        product = Product(
            image = image,
            name = name,
            category = category,
            quantity = quantity,
            price = price,
            description = description,
            store = store
        )

        product.save()

        messages.success(request, 'Produto criado com sucesso.')
    
        return redirect(f'/store/{store.id}')

    else:
        return render(request, 'home.html') 

