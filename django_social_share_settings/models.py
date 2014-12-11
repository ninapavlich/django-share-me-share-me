import urllib

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.sites.models import Site
from django.template import Template


class BaseSocialShareSettings( models.Model ):

    track_social_share_clicks = models.BooleanField( _("Track Social Share Clicks"), default = True )
    
    
    #Share Settings:
    enable_email = models.BooleanField( _("Enable Email"), default = True )
    email_to_template = models.TextField(_("Email To Template"), blank=True, null=True)
    email_subject_template = models.TextField(_("Email Subject Template"), blank=True, null=True)
    email_body_template = models.TextField(_("Email Body Template"), blank=True, null=True)

    enable_twitter = models.BooleanField( _("Enable Twitter"), default = True )
    twitter_share_template = models.TextField(_("Twitter Share Text Template"), blank=True, null=True)

    enable_facebook = models.BooleanField( _("Enable Facebook"), default = True )
    facebook_title_template = models.TextField(_("Facebook Share Title Template"), blank=True, null=True)

    enable_googleplus = models.BooleanField( _("Enable Google Plus"), default = True )

    enable_linkedin = models.BooleanField( _("Enable LinkedIn"), default = True )
    linkedin_title_template = models.TextField(_("LinkedIn Share Title Template"), blank=True, null=True)

    enable_pinterest = models.BooleanField( _("Enable Pinterest"), default = True )
    pinterest_description_template = models.TextField(_("Pinterest Share Description Template"), blank=True, null=True)

    enable_digg = models.BooleanField( _("Enable Digg"), default = True )
    digg_title_template = models.TextField(_("Digg Share Title Template"), blank=True, null=True)

    enable_tumblr = models.BooleanField( _("Enable Tumblr"), default = True )
    tumblr_name_template = models.TextField(_("Tumblr Share Title Template"), blank=True, null=True)
    tumblr_description_template = models.TextField(_("Tumblr Share Description Template"), blank=True, null=True)

    enable_reddit = models.BooleanField( _("Enable Reddit"), default = True )
    reddit_title_template = models.TextField(_("Reddit Share Title Template"), blank=True, null=True)

    enable_stumbleupon = models.BooleanField( _("Enable StumbleUpon"), default = True )
    stumbleupon_title_template = models.TextField(_("StumbleUpon Share Title Template"), blank=True, null=True)

    enable_delicious = models.BooleanField( _("Enable Delicious"), default = True )
    delicious_title_template = models.TextField(_("Delicious Share Title Template"), blank=True, null=True)


    def get_email_share_url(self, page_url, page_title):
        site = Site.objects.get_current()
        query_root = 'mailto:'
        params = { 
            'subject': get_rendered_content(self.email_subject_template, page_url, page_title, site),
            'body': get_rendered_content(self.email_body_template, page_url, page_title, site)
        }
        to_rendered = get_rendered_content(self.email_to_template, page_url, page_title, site) if self.email_to_template else ''
        return '%s%s?%s' % (query_root, to_rendered, urllib.urlencode(params))

    def get_twitter_share_url(self, page_url, page_title):
        site = Site.objects.get_current()
        query_root = 'https://twitter.com/share?'
        params = { 
            'url': page_url,
            'title': get_rendered_content(self.twitter_share_template, page_url, page_title, site)
        }
        return '%s%s' % (query_root, urllib.urlencode(params))

    def get_facebook_share_url(self, page_url, page_title):
        site = Site.objects.get_current()
        query_root = 'http://www.facebook.com/sharer.php?'
        params = { 
            'url': page_url,
            'title': get_rendered_content(self.facebook_title_template, page_url, page_title, site)
        }
        return '%s%s' % (query_root, urllib.urlencode(params))

    def get_googleplus_share_url(self, page_url, page_title):
        site = Site.objects.get_current()
        query_root = 'https://plus.google.com/share?'
        params = { 
            'url': page_url
        }
        return '%s%s' % (query_root, urllib.urlencode(params))

    def get_linkedin_share_url(self, page_url, page_title):
        site = Site.objects.get_current()
        query_root = 'https://www.linkedin.com/shareArticle?'
        params = { 
            'url': page_url,
            'title': get_rendered_content(self.linkedin_title_template, page_url, page_title, site)
        }
        return '%s%s' % (query_root, urllib.urlencode(params))

    def get_pinterest_share_url(self, page_url, page_title):
        site = Site.objects.get_current()
        query_root = 'https://pinterest.com/pin/create/bookmarklet/?'
        params = { 
            'url': page_url,
            'description': get_rendered_content(self.pinterest_description_template, page_url, page_title, site)
        }
        return '%s%s' % (query_root, urllib.urlencode(params))

    def get_digg_share_url(self, page_url, page_title):
        site = Site.objects.get_current()
        query_root = 'http://digg.com/submit?'
        params = { 
            'url': page_url,
            'title': get_rendered_content(self.digg_title_template, page_url, page_title, site)
        }
        return '%s%s' % (query_root, urllib.urlencode(params))

    def get_tumblr_share_url(self, page_url, page_title):
        site = Site.objects.get_current()
        query_root = 'http://www.tumblr.com/share/link?'
        params = { 
            'url': page_url,
            'name': get_rendered_content(self.tumblr_name_template, page_url, page_title, site),
            'description': get_rendered_content(self.tumblr_description_template, page_url, page_title, site)
        }
        return '%s%s' % (query_root, urllib.urlencode(params))

    def get_reddit_share_url(self, page_url, page_title):
        site = Site.objects.get_current()
        query_root = 'http://reddit.com/submit?'
        params = { 
            'url': page_url,
            'title': get_rendered_content(self.reddit_title_template, page_url, page_title, site)
        }
        return '%s%s' % (query_root, urllib.urlencode(params))

    def get_stumbleupon_share_url(self, page_url, page_title):
        site = Site.objects.get_current()
        query_root = 'http://www.stumbleupon.com/submit?'
        params = { 
            'url': page_url,
            'title': get_rendered_content(self.stumbleupon_title_template, page_url, page_title, site)
        }
        return '%s%s' % (query_root, urllib.urlencode(params))

    def get_delicious_share_url(self, page_url, page_title):
        site = Site.objects.get_current()
        query_root = 'https://delicious.com/save?v=5'
        params = { 
            'url': page_url,
            'title': get_rendered_content(self.delicious_title_template, page_url, page_title, site)
        }
        return '%s%s' % (query_root, urllib.urlencode(params))

    def get_rendered_content(self, template_content, page_url, page_title, site):
        if not template_content:
            return "%s | %s"%(page_title, page_url)
        template = Template(template_content)
        context = Context({
            "url": page_url,
            "title": page_title,
            "site": site
        })
        return template.render(context)

    class Meta:
        abstract=True        

class SocialShareTrack( models.Model ):

    created = models.DateTimeField(_('Created Date'), auto_now_add=True, 
        blank=True, null=True)

    service = models.CharField()
    url = models.CharField()
    ipaddress = models.CharField()


class SiteBaseSocialShareSettings(BaseSocialShareSettings):
    site = models.models.ForeignKey(Site)

    @staticmethod
    def get_site_settings():
        current_site = Site.objects.get_current()
        try:
            return SiteBaseSocialShareSettings.objects.filter(site=current_site)[0]
        except:
            return None
