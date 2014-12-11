from django.contrib import admin

from .models import *

class SiteBaseSocialShareSettingsAdmin(admin.ModelAdmin):
    pass

admin.site.register(SiteBaseSocialShareSettings, SiteBaseSocialShareSettingsAdmin)