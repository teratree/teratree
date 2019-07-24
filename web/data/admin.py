from django.contrib import admin

from .models import Questions00001
#
# Results
#
@admin.register(Questions00001)
class Questions00001Admin(admin.ModelAdmin):
    list_display = ('respondant', 'posted', 'location', 'cczero')
    list_filter = ('cczero',)
