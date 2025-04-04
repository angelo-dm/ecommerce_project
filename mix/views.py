from django.shortcuts import render, get_object_or_404
from .models import Produto

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'home.html', {'produtos': produtos})

def details(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'details.html', {'produto':produto})
