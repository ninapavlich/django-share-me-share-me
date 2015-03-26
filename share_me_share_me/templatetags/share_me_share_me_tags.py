from django.template import Library
register = Library()

from ..models import *

@register.assignment_tag(takes_context=True)
def get_social_share_links(context):

    settings = SocialShareSettings.get_site_settings()
    if settings:
        return settings.get_social_share_links()
    return []
    
@register.assignment_tag(takes_context=True)
def get_social_share_link(context, share_link, object_url, object_title):

    """
    Construct the social share link for the request object.

    """
    request = context['request']
    url = unicode(object_url)
    if 'http' not in object_url.lower():
        full_path = ''.join(('http', ('', 's')[request.is_secure()], '://', request.META['HTTP_HOST'], url))
    else:
        full_path = url

    return share_link.get_share_url(full_path, object_title)

@register.assignment_tag(takes_context=True)
def get_social_share_count(context, type):

    return SocialShareTrack.get_count(type)   
        

    
