from django.contrib import admin
from .models import Rate
# Register your models here.

class RateAdmin (admin.ModelAdmin):
    list_display = ('id', 'AHT', 'RP', 'SL', 'AS', 'Shrink', 'Calls')
admin.site.register(Rate)