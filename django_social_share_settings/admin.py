from django.contrib import admin

from .models import *

class SocialShareLinkInline(admin.TabularInline):
    model = SocialShareLink 
    extra = 0
    sortable_field_name = "order"

class SocialShareSettingsAdmin(admin.ModelAdmin):
    inlines = [SocialShareLinkInline]

class SocialShareTrackAdmin(admin.ModelAdmin):

    list_display = ('full_url', 'domain', 'path', 'type')
    list_filters = ('full_url', 'domain', 'path', 'type', 'created')


admin.site.register(SocialShareSettings, SocialShareSettingsAdmin)
admin.site.register(SocialShareTrack, SocialShareTrackAdmin)