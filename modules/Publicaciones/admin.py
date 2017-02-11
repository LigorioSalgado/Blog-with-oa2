from django.contrib import admin
from .models import Publicacion

class PublicacionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Publicacion, PublicacionAdmin)
# Register your models here.
