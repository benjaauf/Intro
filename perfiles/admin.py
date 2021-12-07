from django.contrib import admin
from .models import *
from perfiles.models import Certamen



# Register your models here.

admin.site.register(Exp)
admin.site.register(Nivel)
admin.site.register(Certamen)
