from django.urls import path
from Avatar import views

urlpatterns = [
    path('',views.avatar,name='avatar'),
]