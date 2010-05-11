from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^djragon_cms/', include('djragon_cms.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    #(r'^news/', include('news.urls')),
)

urlpatterns += patterns('',
    #url(r'^$|^(.*)/$', 'feincms.views.base.handler'),
    url(r'^$|^(.*)/$', 'feincms.views.applicationcontent.handler'),
    url(r'^$', 'feincms.views.base.handler', { 'path': '/news' }),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT}),
    )
