@register.assignment_tag(takes_context=True)
def social_share_link(context, object_url, object_title, service):

    """
    Construct the social share link for the request object.

    """
    request = context['request']
    if 'http' not in object_url.lower():
        full_path = ('http', ('', 's')[request.is_secure()], '://', request.META['HTTP_HOST'], object_url)
    else:
        full_path = object_url

    settings = SiteBaseSocialShareSettings.get_site_settings()
        

    if share_to == 'email':
        return settings.get_email_share_url(full_path, object_title)
        
    elif share_to == 'twitter':
        return settings.get_twitter_share_url(full_path, object_title)

    elif share_to == 'facebook':
        return settings.get_facebook_share_url(full_path, object_title)

    elif share_to == 'googleplus':
        return settings.get_googleplus_share_url(full_path, object_title)
        
    elif share_to == 'linkedin':
        return settings.get_linkedin_share_url(full_path, object_title)

    elif share_to == 'pinterest':
        return settings.get_pinterest_share_url(full_path, object_title)

    elif share_to == 'digg':
        return settings.get_digg_share_url(full_path, object_title)

    elif share_to == 'tumblr':
        return settings.get_tumblr_share_url(full_path, object_title)

    elif share_to == 'reddit':
        return settings.get_reddit_share_url(full_path, object_title)

    elif share_to == 'stumbleupon':
        return settings.get_stumbleupon_share_url(full_path, object_title)

    elif share_to == 'delicious':
        return settings.get_delicious_share_url(full_path, object_title)
        
