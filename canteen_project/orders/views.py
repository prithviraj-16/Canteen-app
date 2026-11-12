from django.shortcuts import render
from .models import FoodOrder

def home(request):
    orders = FoodOrder.objects.all()
    return render(request, 'orders/home.html', {'orders': orders})
