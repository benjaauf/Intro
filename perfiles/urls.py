from django.urls import path
from perfiles import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('home/',views.home, name='home'),
    path('register/',views.register, name='register'),
    path('',views.inicio, name='inicio'),
    path('login/', LoginView.as_view(template_name='perfiles/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='perfiles/inicio.html'), name='logout'),
    path('estudio/', views.hora_estudio, name='estudio'),
    path('cumplido/',views.cumplido, name='cumplido'),
    ]