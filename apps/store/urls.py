from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/', views.store, name='store'),
    path('create/', views.create_store, name='create_store'),
    path('edit/<int:id>', views.edit_store, name='edit_store'),
    path('delete/<int:id>', views.delete_store, name='delete_store'),
]