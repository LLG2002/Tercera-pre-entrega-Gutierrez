from django.urls import path
from inicio import views
from django.contrib.auth.views import LogoutView
app_name= 'usuarios'
urlpatterns = [
    
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='inicio/logout.html'), name='logout'),
    path('', views.registrarse, name='registrarse'),   
]