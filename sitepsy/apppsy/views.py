from django.shortcuts import render, redirect
from apppsy.models import Note
from django.contrib.auth.decorators import login_required
from apppsy.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
@login_required
def home(request):
	context ={
	'notes': Note.objects.all()
	}
	return render(request, 'home.html',context)


def register(request):
    if request.method == 'POST':          #check si l'user veut envoyer des données
        form = RegisterForm(request.POST)     #si oui, on crée une instance de la classe userform _ avec méthode post(pr laissr entrer des valeurs)  >>> on le met ds une variable appelée 'form'
        if form.is_valid():               #on vérifie si le form est valide   >>> si oui  : on le sauvegarde
            form.save()
                  #on fait une redirection vers une page x
            user= form.cleaned_data.get('username')
            messages.success(request, "votre compte est magnifiquement créé!" + user)
            return redirect('home') 
    else:
        form = RegisterForm()                 #However, if the request is not a POST request, we just create an instance of the empty UserForm. 

    return render (request, "base/register.html", {'form':form})