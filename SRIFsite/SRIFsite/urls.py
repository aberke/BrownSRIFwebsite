from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import main_site.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SRIFsite.views.home', name='home'),
    # url(r'^SRIFsite/', include('SRIFsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    

    url(r'^portfolio/', main_site.views.server_portfolio),
    url(r'^$', main_site.views.server_index),
)
