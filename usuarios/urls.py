from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

app_name= 'usuarios'
urlpatterns = [
    
    path('login/', views.login, name='login'),
    path('editar/', views.editar_usuario, name='editar'),
    path('logout/', LogoutView.as_view(template_name='inicio/logout.html'), name='logout'),
    path('', views.registrarse, name='registrarse'),   
    path('cambiar-contrasenia/', views.CambiarContrasenia.as_view(), name='cambiar_contrasenia'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)