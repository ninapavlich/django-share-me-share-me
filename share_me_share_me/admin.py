from django.contrib import admin

from .models import *

class SocialShareLinkInline(admin.TabularInline):
    model = SocialShareLink 
    extra = 0
    sortable_field_name = "order"

class SocialShareSettingsAdmin(admin.ModelAdmin):
    inlines = [SocialShareLinkInline]

    list_display = ('title', 'site',)
    readonly_fields = ('title',)
    list_filter = ('site',)

class SocialShareTrackAdmin(admin.ModelAdmin):

    list_display = ('created', 'full_url', 'domain', 'path', 'type')
    list_filter = ('full_url', 'domain', 'path', 'type', 'created')
    search_fields = ('full_url','domain','path', 'type')
    fields = ['domain','path','full_url','type','created']
    csv_fields = ['domain','path','full_url','type','created']
    readonly_fields = ('created',)

admin.site.register(SocialShareSettings, SocialShareSettingsAdmin)
admin.site.register(SocialShareTrack, SocialShareTrackAdmin)