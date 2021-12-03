from django.urls import path
from Avatar import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.avatar,name='avatar'),
    path('/deracc',views.deracc,name='deracc'),
    path('/dercar',views.dercar,name='dercar'),
    path('/derves',views.derves,name='derves'),
    path('/izqacc',views.izqacc,name='izqacc'),
    path('/izqcar',views.izqcar,name='izqcar'),
    path('/izqves',views.izqves,name='izqves'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)