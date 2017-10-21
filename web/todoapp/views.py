from django.shortcuts import render
from .models import Todo
# Create your views here.

def index(request):
    if request.GET.get('alt') == '1':
        queryset = Todo.objects.all()
    else:
        queryset = Todo.objects.filter(done=False)
    
    todo_list = queryset.order_by('-created_at')
    return render(request, 'index.html', {'todo_list': todo_list})