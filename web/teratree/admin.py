from django.contrib import admin

class AdminSite(admin.AdminSite):
    site_header = 'TeraTree Administration'

from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
