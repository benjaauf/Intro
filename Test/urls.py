from django.urls import path
from Test import views

urlpatterns = [
    path('', views.test, name='test')
]