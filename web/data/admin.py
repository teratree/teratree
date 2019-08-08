from django.contrib import admin

from .models import Questions00001
#
# Results
#
@admin.register(Questions00001)
class Questions00001Admin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'posted', 'location', 'cczero')
    list_filter = ('cczero',)
