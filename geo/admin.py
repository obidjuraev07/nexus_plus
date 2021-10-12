from django.contrib import admin
from .models import Region,District
# Register your models here.

class RegionAdmin(admin.ModelAdmin):
    list_display = ["name_uz","name_ru","ordering"]

class DistrictAdmin(admin.ModelAdmin):
    list_display = ["name_uz","name_ru","ordering","region"]

admin.site.register(Region,RegionAdmin)
admin.site.register(District,DistrictAdmin)