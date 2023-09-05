from django.contrib import admin
from .models import *
from .forms import ClienteForm



# Register your models here.
admin.site.register(Lead)
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    form = ClienteForm
# admin.site.register(ClienteForm)
