from django.urls import path
from.import views

urlpatterns = [
    path('',views.test2, name='Test2'),
    # path('estudio/', views.estudio, name= 'estudio')
]