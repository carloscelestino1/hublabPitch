from django import forms
from .models import PessoaF, PessoaJ


class PessoafForm(forms.ModelForm):
    
    class Meta:
        model = PessoaF
        fields = ('nomecomp','email', 'telefone')
