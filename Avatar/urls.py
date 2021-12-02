from django.urls import path
from Avatar import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.avatar,name='avatar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)