from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from store.models import Store

def dashboard(request):
    order = request.GET.get('order', 'name')
    search = request.GET.get('search')

    if search:
        stores = Store.objects.filter(name__contains=search)
    else:
        stores_list = Store.objects.all().order_by(order)

        paginator = Paginator(stores_list, 12)

        page = request.GET.get('page')

        stores = paginator.get_page(page)

    context = {
        'stores': stores,
    }
    
    return render(request, 'core/dashboard.html', context)

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password != password_confirm:
            messages.error(request, 'As senhas não são iguais')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('register')

        arroba = email.find('@')
        username = email[:arroba]

        user = User.objects.create_user(
            username=username, 
            email=email, 
            password=password, 
            first_name=first_name, 
            last_name=last_name
        )
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('login')

    return render(request, 'core/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            username = User.objects.filter(email=email).values_list('username', flat=True).get()
            print(username)
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
                return redirect('dashboard')
            else:
                messages.error(request, 'O e-mail ou senha não conferem')
                return redirect('login')
        else:
                messages.error(request, 'Usuário não cadastrado')
                return redirect('login')
    
    return render(request, 'core/login.html')

def logout(request):
    auth.logout(request)
    return redirect('dashboard')

def profile(request):
    stores = Store.objects.all()

    context = {
        'stores': stores,
    }

    return render(request, 'core/profile.html', context)

def empty_field(field):
    return not field.strip()




