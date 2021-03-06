from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'woh.views.home', name='home'),
    #url(r'^woh/', include('woh.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url('^$', 'woh.data.views.index', name='index'),

    url('^worst-overtime-offenders/$', 'woh.data.views.overtime', name='overtime'),
    url('^woh/(\d*)/$', 'woh.data.views.biz_detail', name='biz_detail'),

)
