from django.urls import path
from . import views

app_name = 'products'


urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<int:pk>/', views.detail, name='detail'),
]