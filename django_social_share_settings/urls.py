from django.conf.urls.static import static
from django.conf.urls import patterns, url, include


from .views import *

urlpatterns = patterns('',
    
    url(r'^track/shares/$', ShareCounterRedirectView.as_view(), name="share_counter_redirect_view"),

)
