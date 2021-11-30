from django.urls import path
from Test import views

urlpatterns = [
    path('', views.test, name='test'),
    path('delete/<int:ramo_id>/',views.delete,name='delete'),
    path('descanso/',views.descanso,name='descanso'),
    path('updatet1/', views.updatet1, name='updatet1'),
    path('deletet1/<int:ramo_id>/',views.deletet1,name='deletet1')
]