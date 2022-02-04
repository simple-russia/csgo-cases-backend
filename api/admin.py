from django.contrib import admin
from api.models import *

# Register your models here.
admin.site.register(Collection)
admin.site.register(Type)
admin.site.register(Color)
admin.site.register(Weapon)
admin.site.register(Description)
admin.site.register(Case)
admin.site.register(Case_has_weapon)
