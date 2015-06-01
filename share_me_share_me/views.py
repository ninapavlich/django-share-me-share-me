from urlparse import urlparse
import datetime

from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.base import RedirectView
from django.views.generic import ListView

from .models import *

DEFAULT_DURATION_DAYS = 30

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

##############################
## ADMIN VIEWS ###############
##############################

def get_latest_shared_paths(queryset, duration_days):
    
    filter_duration = datetime.datetime.now() - datetime.timedelta(days=duration_days)
    queryset = queryset.filter(created__gte=filter_duration)

    path_querset = queryset.values('path').annotate(total=models.Count('path')).order_by('-total')
    
    shared_paths = {
        'title':"Most Shared Paths (Last %s days)"%(duration_days),
        'slug':'most-shared-urls',
        'links':path_querset[:5],
        'more_link_title':"See More",
        'more_link':"%s?%s"%(reverse('dashboard_stats_paths_share_me_share_me'), 'days=365'),
        'display_stat':'path',
        'duration_days':duration_days
    }
    return shared_paths

def get_latest_shared_services(queryset, duration_days):
    
    filter_duration = datetime.datetime.now() - datetime.timedelta(days=duration_days)
    queryset = queryset.filter(created__gte=filter_duration)

    service_queryset = queryset.values('type').annotate(total=models.Count('type')).order_by('-total')

    shared_services = {
        'title':"Most Shared Services (Last %s days)"%(duration_days),
        'slug':'most-shared-networks',
        'links':service_queryset[:5],
        'more_link_title':"See More",
        'more_link':"%s?%s"%(reverse('dashboard_stats_services_share_me_share_me'), 'days=365'),
        'display_stat':'type',
        'duration_days':duration_days
    }
    return shared_services    

class DashboardStatsView(ListView):

    model = SocialShareTrack
    template_name = "admin/share_me_share_me/socialsharetrack/dashboard_stats.html"

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, *args, **kwargs):
        return super(DashboardStatsView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = self.model._default_manager.all()

        duration_days = int(self.request.REQUEST.get('days', DEFAULT_DURATION_DAYS))
        
        self.shared_paths = get_latest_shared_paths(queryset, duration_days)

        self.shared_services = get_latest_shared_services(queryset, duration_days)

        return [self.shared_paths, self.shared_services]


class DashboardMostSharedPathsStatsView(ListView):

    model = SocialShareTrack
    template_name = "admin/share_me_share_me/socialsharetrack/dashboard_most_shared_paths_stats.html"

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, *args, **kwargs):
        return super(DashboardMostSharedPathsStatsView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = self.model._default_manager.all()

        self.duration_days = int(self.request.REQUEST.get('days', DEFAULT_DURATION_DAYS))
        
        self.shared_paths = get_latest_shared_paths(queryset, self.duration_days)

        return self.shared_paths['links']


    def get_context_data(self, **kwargs):
        ctx = super(DashboardMostSharedPathsStatsView, self).get_context_data(**kwargs)
        ctx['title'] = self.shared_paths['title']
        ctx['slug'] = self.shared_paths['slug']
        ctx['display_stat'] = self.shared_paths['display_stat']
        ctx['duration_days'] = self.shared_paths['duration_days']
        return ctx


class DashboardMostSharedServicesStatsView(ListView):

    model = SocialShareTrack
    template_name = "admin/share_me_share_me/socialsharetrack/dashboard_most_shared_services_stats.html"

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, *args, **kwargs):
        return super(DashboardMostSharedServicesStatsView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = self.model._default_manager.all()

        self.duration_days = int(self.request.REQUEST.get('days', DEFAULT_DURATION_DAYS))
        
        self.shared_services = get_latest_shared_services(queryset, self.duration_days)

        return self.shared_services['links']  

    def get_context_data(self, **kwargs):
        ctx = super(DashboardMostSharedServicesStatsView, self).get_context_data(**kwargs)
        ctx['title'] = self.shared_services['title']
        ctx['slug'] = self.shared_services['slug']
        ctx['display_stat'] = self.shared_services['display_stat']
        ctx['duration_days'] = self.shared_services['duration_days']
        return ctx




try:
    from site_admin.dashboard import dashboard_registry, DashboardLoaderModuleRegistry
    dashboard_registry.register(DashboardLoaderModuleRegistry.CATEGORY_COLUMN_THREE, 'Share Stats', 'dashboard_stats_share_me_share_me')
except:
    pass
    #not implemented