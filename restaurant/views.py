from django.shortcuts import render
from .models import Hall, Board
from .forms import OrderHeaderForm

def board_list_hall(request):
    boards = Board.objects.all();
    return render(request, 'restaurant/board_list_hall.html', {'boards': boards})

def order(request):
    form = OrderHeaderForm
    return render(request, 'restaurant/order.html', {'form': form})

