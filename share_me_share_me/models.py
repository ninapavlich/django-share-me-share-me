import urllib

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.sites.models import Site
from django.template import Template, Context





class SocialShareSettings( models.Model ):

    site = models.ForeignKey(Site, null=True, blank=True)

    track_social_share_clicks = models.BooleanField( _("Track Social Share Clicks"), default = True )
    
    def get_social_share_links(self):
        return SocialShareLink.objects.filter(parent=self).order_by('order')

    @staticmethod
    def get_site_settings():
        current_site = Site.objects.get_current()
        try:
            return SocialShareSettings.objects.filter(site=current_site)[0]
        except:
            try:
                return SocialShareSettings.objects.all()[0]
            except:
                return None

    @property
    def title(self):
        if self.site:
            return 'Social Share Settings %s'%(self.site.domain)
        return "Default Social Share Settings"

    class Meta:
        verbose_name_plural = _("Social Share Settings")

    def __unicode__(self):
        return self.title
     

# class SocialShareTrack( models.Model ):

#     created = models.DateTimeField(_('Created Date'), auto_now_add=True, 
#         blank=True, null=True)

#     service = models.CharField()
#     url = models.CharField()
#     ipaddress = models.CharField()


class SocialShareLink( models.Model ):

    parent = models.ForeignKey(SocialShareSettings)
    order = models.PositiveIntegerField('order', null = True, blank=True)


    TYPE_EMAIL = 'email'
    TYPE_TWITTER = 'twitter'
    TYPE_FACEBOOK = 'facebook'
    TYPE_GOOGLEPLUS = 'googleplus'
    TYPE_LINKEDIN = 'linkedin'
    TYPE_PINTEREST = 'pinterest'
    TYPE_DIGG = 'digg'
    TYPE_TUMBLR = 'tumblr'
    TYPE_REDDIT = 'reddit'
    TYPE_STUMBLEUPON = 'stumbleupon'
    TYPE_DELICIOUS = 'delicious'
    

    SERVICE_TYPES = (
        (TYPE_EMAIL, "Email"),
        (TYPE_TWITTER, "Twitter"),
        (TYPE_FACEBOOK, "Facebook"),
        (TYPE_GOOGLEPLUS, "Google Plus"),
        (TYPE_LINKEDIN, "LinkedIn"),
        (TYPE_PINTEREST, "Pinterest"),
        (TYPE_DIGG, "Digg"),
        (TYPE_TUMBLR, "Tumblr"),
        (TYPE_REDDIT, "Reddit"),
        (TYPE_STUMBLEUPON, "StumbleUpon"),
        (TYPE_DELICIOUS, "Delicious"),
    )

    FONT_AWESOME_CLASSES = {
        TYPE_EMAIL: "envelope",
        TYPE_TWITTER: "twitter",
        TYPE_FACEBOOK: "facebook",
        TYPE_GOOGLEPLUS: "google-plus",
        TYPE_LINKEDIN: "linkedin",
        TYPE_PINTEREST: "pinterest",
        TYPE_DIGG: "digg",
        TYPE_TUMBLR: "tumblr",
        TYPE_REDDIT: "reddit",
        TYPE_STUMBLEUPON: "stumbleupon",
        TYPE_DELICIOUS: "delicious",
    }


    type = models.CharField("Service Type", max_length=255, 
        null=True, blank=True, choices=SERVICE_TYPES)

    title_template = models.TextField(_("Title Template"), blank=True, null=True, help_text="Applicable to all types but Facebook and Google Plus. Available contact variables: {{url}}, {{title}}, {{site}}")
    description_template = models.TextField(_("Description Template"), blank=True, null=True, help_text="Applicable to type Email and Tumblr. Available contact variables: {{url}}, {{title}}, {{site}}")
    to_template = models.TextField(_("To Template"), blank=True, null=True, help_text="Applicable to type Email. Available contact variables: {{url}}, {{title}}, {{site}}")

    @property
    def font_awesome_class(self):
        return SocialShareLink.FONT_AWESOME_CLASSES[self.type]

    def get_share_url(self, full_path, object_title):

        if self.parent.track_social_share_clicks and self.type != SocialShareLink.TYPE_EMAIL:
            return self._get_track_url(full_path, object_title)
        else:
            return self._get_share_url(full_path, object_title)

    def _get_track_url(self, full_path, object_title):

        path = reverse('share_counter_redirect_view')
        
        params = { 
            'url': full_path,
            'type': self.type,
            'title': object_title
        }
        track_url = '%s?%s' % (path, urllib.urlencode(params))

        return track_url

    def _get_share_url(self, full_path, object_title):
        if self.type == SocialShareLink.TYPE_EMAIL:
            return self.get_email_share_url(full_path, object_title)
            
        elif self.type == SocialShareLink.TYPE_TWITTER:
            return self.get_twitter_share_url(full_path, object_title)

        elif self.type == SocialShareLink.TYPE_FACEBOOK:
            return self.get_facebook_share_url(full_path, object_title)

        elif self.type == SocialShareLink.TYPE_GOOGLEPLUS:
            return self.get_googleplus_share_url(full_path, object_title)
            
        elif self.type == SocialShareLink.TYPE_LINKEDIN:
            return self.get_linkedin_share_url(full_path, object_title)

        elif self.type == SocialShareLink.TYPE_PINTEREST:
            return self.get_pinterest_share_url(full_path, object_title)

        elif self.type == SocialShareLink.TYPE_DIGG:
            return self.get_digg_share_url(full_path, object_title)

        elif self.type == SocialShareLink.TYPE_TUMBLR:
            return self.get_tumblr_share_url(full_path, object_title)

        elif self.type == SocialShareLink.TYPE_REDDIT:
            return self.get_reddit_share_url(full_path, object_title)

        elif self.type == SocialShareLink.TYPE_STUMBLEUPON:
            return self.get_stumbleupon_share_url(full_path, object_title)

        elif self.type == SocialShareLink.TYPE_DELICIOUS:
            return self.get_delicious_share_url(full_path, object_title)
        

    def get_email_share_url(self, page_url, page_title):
        site = Site.objects.get_current()
        query_root = 'mailto:'
        
        to_rendered = self.get_rendered_content(self.to_template, page_url, page_title, site) if self.to_template else ''
        
        #body_cleaned = body.replace("$linebreak", "%0D%0A")
        body_cleaned = urllib.quote_plus(self.get_rendered_content(self.description_template, page_url, page_title, site))
        body_cleaned = body_cleaned.replace("+", "%20")
        

        #subject_cleaned = subject.replace("|", "%7C")
        subject_cleaned = urllib.quote_plus(self.get_rendered_content(self.title_template, page_url, page_title, site),)
        subject_cleaned = subject_cleaned.replace("+", "%20")

        return '%s%s?body=%s&subject=%s' % (query_root, to_rendered, body_cleaned, subject_cleaned)
        

    def get_twitter_share_url(self, page_url, page_title):
        site = Site.objects.get_current()
        query_root = 'https://twitter.com/intent/tweet?'
        params = { 
            'text': self.get_rendered_content(self.title_template, page_url, page_title, site)
        }
        return '%s%s' % (query_root, urllib.urlencode(params))

    def get_facebook_share_url(self, page_url, page_title):
        site = Site.objects.get_current()
        query_root = 'https://www.facebook.com/sharer.php?'
        params = { 
            'u': page_url,
            'title': self.get_rendered_content(self.title_template, page_url, page_title, site)
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
            'title': self.get_rendered_content(self.title_template, page_url, page_title, site)
        }
        return '%s%s' % (query_root, urllib.urlencode(params))

    def get_pinterest_share_url(self, page_url, page_title):
        site = Site.objects.get_current()
        query_root = 'https://pinterest.com/pin/create/bookmarklet/?'
        params = { 
            'url': page_url,
            'description': self.get_rendered_content(self.title_template, page_url, page_title, site)
        }
        return '%s%s' % (query_root, urllib.urlencode(params))

    def get_digg_share_url(self, page_url, page_title):
        site = Site.objects.get_current()
        query_root = 'https://digg.com/submit?'
        params = { 
            'url': page_url,
            'title': self.get_rendered_content(self.title_template, page_url, page_title, site)
        }
        return '%s%s' % (query_root, urllib.urlencode(params))

    def get_tumblr_share_url(self, page_url, page_title):
        site = Site.objects.get_current()
        query_root = 'https://www.tumblr.com/share/link?'
        params = { 
            'url': page_url,
            'name': self.get_rendered_content(self.title_template, page_url, page_title, site),
            'description': self.get_rendered_content(self.description_template, page_url, page_title, site)
        }
        return '%s%s' % (query_root, urllib.urlencode(params))

    def get_reddit_share_url(self, page_url, page_title):
        site = Site.objects.get_current()
        query_root = 'https://reddit.com/submit?'
        params = { 
            'url': page_url,
            'title': self.get_rendered_content(self.title_template, page_url, page_title, site)
        }
        return '%s%s' % (query_root, urllib.urlencode(params))

    def get_stumbleupon_share_url(self, page_url, page_title):
        site = Site.objects.get_current()
        query_root = 'https://www.stumbleupon.com/submit?'
        params = { 
            'url': page_url,
            'title': self.get_rendered_content(self.title_template, page_url, page_title, site)
        }
        return '%s%s' % (query_root, urllib.urlencode(params))

    def get_delicious_share_url(self, page_url, page_title):

        site = Site.objects.get_current()
        query_root = 'https://delicious.com/save?v=5&provider=CCL&noui&jump=close&'
        params = { 
            'url': page_url,
            'title': self.get_rendered_content(self.title_template, page_url, page_title, site)
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


class SocialShareTrack( models.Model ):

    domain = models.CharField(_("Domain"), blank=True, null=True, max_length=255,)
    path = models.CharField(_("Path"), blank=True, null=True, max_length=255,)
    full_url = models.CharField(_("Full URL"), blank=True, null=True, max_length=255,)

    created = models.DateTimeField(_('Created Date'), auto_now_add=True, 
        blank=True, null=True)

    type = models.CharField("Service Type", max_length=255, 
        null=True, blank=True, choices=SocialShareLink.SERVICE_TYPES)
    
    @staticmethod
    def get_count(type=None, from_datetime=None, to_datetime=None, domain=None, path=None, full_url=None ):
        all_tracks = SocialShareTrack.objects.all()
        if type:
            all_tracks = all_tracks.filter(type=type)

        if from_datetime:
            all_tracks = all_tracks.filter(created__gte=from_datetime)

        if to_datetime:
            all_tracks = all_tracks.filter(created__lte=to_datetime)

        if domain:
            all_tracks = all_tracks.filter(domain=domain)

        if path:
            all_tracks = all_tracks.filter(path=path)

        if full_url:
            all_tracks = all_tracks.filter(full_url=full_url)

        return all_tracks

    @classmethod
    def track(cls, domain, path, full_url, type):
        track = cls(
            domain=domain,
            path=path,
            full_url=full_url,
            type=type
        )
        track.save()
        return track
