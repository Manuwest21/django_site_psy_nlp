from django.urls import path, include
from django.contrib.auth import views as auth_views
from apppsy import views

urlpatterns =[
	path('accounts/', include('django.contrib.auth.urls')),
	path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
	path('',views.home, name='home'),
]