# Ceres | O desenvolvimento e uso de uma plataforma web para auxiliar na venda de produtos agrícolas de pequenos produtores

## COMANDOS

### Instalar o módulo venv

```
pip install virtualenv
```

### Criar ambiente virtual

```
virtualenv venv
```

### Iniciar ambiente virtual

```
venv/Scripts/activate
```

### Instalar o web framework Django

```
pip install django
```

### Criar projeto Django

```
django-admin startproject setup .
```

### Criar aplicativo

```
python manage.py startapp core
python manage.py startapp store
python manage.py startapp product
python manage.py startapp room
```

### Criar novas migrations com base nas alterações feitas em seus models

```
python manage.py makemigrations
```

### Aplicar e desaplicar migrations

```
python manage.py migrate
```

### Criar um usuário que possa fazer login no Django admin site

```
python manage.py createsuperuser
```

### Instalar a biblioteca de imagens Python

```
pip install pillow
```

### Instalar o projeto Django Channels

```
pip install channels
```