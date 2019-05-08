from django.contrib import admin
from webansi.models import HostGroup, Host, Module, Argument

# Register your models here.
# admin.site.register(HostGroup)
# admin.site.register(Host)
# admin.site.register(Module)
# admin.site.register(Argulment)

for item in [HostGroup, Host, Module, Argument]:
    admin.site.register(item)