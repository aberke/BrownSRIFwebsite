from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from main_site import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SRIFsite.views.home', name='home'),
    # url(r'^SRIFsite/', include('SRIFsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    

    url(r'^portfolio/', views.serve_portfolio, name = 'serve_portfolio'),
    url(r'^education/', views.serve_education, name = 'serve_education'),
    url(r'^guide/', views.serve_guide, name = 'serve_guide'),
    url(r'^pitches/(?P<semester_id>\d+)/', views.serve_pitches_by_id, name = 'serve_pitches_by_id'),
    url(r'^pitches/', views.serve_pitches, name = 'serve_pitches'),
    url(r'^$', views.serve_index, name = 'serve_index'),
)
