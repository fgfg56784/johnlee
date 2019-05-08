from django.contrib import admin
from .models import HostGroup, Hosts, Modules, Argument

# Register your models here.
for item in [HostGroup, Hosts, Modules, Argument]:
    admin.site.register(item)
