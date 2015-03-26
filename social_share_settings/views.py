from urlparse import urlparse

from django.views.generic.base import RedirectView

from .models import *

class ShareCounterRedirectView(RedirectView):

    permanent = False
    query_string = True
    
    def get_redirect_url(self, *args, **kwargs):


        full_url = self.request.GET.get('url', None)
        if full_url == None:
            return None

        type = self.request.GET.get('type', None)
        if type == None:
            return None

        title = self.request.GET.get('title', None)
        
        #Retreieve settings
        settings = SocialShareSettings.get_site_settings()
        link_settings = SocialShareLink.objects.get(type=type,parent=settings)



        parsed_uri = urlparse( full_url )
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

        #Store 
        SocialShareTrack.track(domain, parsed_uri.path, full_url, type)

        #return full_url
        share_url = link_settings._get_share_url(full_url, title)

        return share_url