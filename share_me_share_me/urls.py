from django.conf.urls.static import static
from django.conf.urls import include, url


from .views import *

urlpatterns = [
    
    url(r'^track/shares/$', ShareCounterRedirectView.as_view(), name="share_counter_redirect_view"),
    
    url(r'^admin/dashboard_stats/share_me_share_me/socialsharetrack/$', DashboardStatsView.as_view(), name='dashboard_stats_share_me_share_me'),
    url(r'^admin/dashboard_stats/share_me_share_me/socialsharetrack/paths/$', DashboardMostSharedPathsStatsView.as_view(), name='dashboard_stats_paths_share_me_share_me'),
    url(r'^admin/dashboard_stats/share_me_share_me/socialsharetrack/services/$', DashboardMostSharedServicesStatsView.as_view(), name='dashboard_stats_services_share_me_share_me'),
]