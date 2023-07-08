from django.shortcuts import render
from apppsy.models import Note
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	context ={
	'notes': Note.objects.all()
	}
	return render(request, 'home.html',context)
