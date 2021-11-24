from django.urls import path
from Test import views

urlpatterns = [
    path('', views.test, name='test'),
    path('delete/<int:ramo_id>/',views.delete,name='delete'),
    path('horario/', views.horario, name='horario'),
]