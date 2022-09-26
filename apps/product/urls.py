from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_product, name='create_product'),
    path('edit/<int:id>', views.edit_product, name='edit_product'),
    path('delete/<int:id>', views.delete_product, name='delete_product'),
    path('search/<int:id>', views.search_product, name='search_product'),
]

