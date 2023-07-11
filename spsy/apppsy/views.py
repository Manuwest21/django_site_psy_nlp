from django.shortcuts import render, redirect
from apppsy.models import Note
from django.contrib.auth.decorators import login_required
from apppsy.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from datetime import datetime, timedelta
from apppsy.models import Le_patient_date
from django.http import HttpResponseBadRequest
from dateutil import parser


def period_view(request):
    # Récupération des mois disponibles dans la plage de 2020 à fin 2023
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 12, 31)
    months = []
    current_date = start_date
    while current_date <= end_date:
        months.append(current_date.strftime('%B %Y'))
        current_date += timedelta(days=30)  # Ajoute 30 jours pour passer au mois suivant
    selected_start_month = request.GET.get('start_month')
    selected_end_month = request.GET.get('end_month')

    # Conversion des mois sélectionnés en dates de début et de fin
    
    start_date = selected_start_month
    end_date = selected_end_month
    # except ValueError:
    #     return HttpResponseBadRequest("Format de date invalide.")
    try:
        start_date = datetime.strptime(selected_start_month, '%B %Y')
        end_date = datetime.strptime(selected_end_month, '%B %Y')
    except:
        start_date=datetime(2020, 1, 1)
        end_date=datetime(2023, 12, 31)
    # Récupération des instances du modèle dans la plage de date sélectionnée
    instances = Le_patient_date.objects.filter(date__range=[start_date, end_date])

    # Calcul de la répartition des valeurs du champ "predicted"
    predicted_counts = {}
    for instance in instances:
        predicted = instance.predicted
        if predicted in predicted_counts:
            predicted_counts[predicted] += 1
        else:
            predicted_counts[predicted] = 1

    context = {
        'months': months,
        'selected_start_month': selected_start_month,
        'selected_end_month': selected_end_month,
        'predicted_counts': predicted_counts,
        # Autres données à passer au template
    }

    return render(request, 'base/period.html', context)



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