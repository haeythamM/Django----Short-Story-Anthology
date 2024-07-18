from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path("<int:pk>", views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
]