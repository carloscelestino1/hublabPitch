from django.shortcuts import render,get_object_or_404, redirect
from .forms import PessoafForm
from . models import PessoaF

def homepageView(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', None)
        email = request.POST.get('email', None)
        telefone = request.POST.get('telefone', None) #criar uma forma de não passar a mascara
        PessoaF.objects.create(nomecomp=nome, email=email, telefone=telefone)
        
    
    return render(request, 'main/indexx.html')