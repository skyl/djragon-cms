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
    (r'^comments/', include('django.contrib.comments.urls')),
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



# django-tagging-ext url definitions
from feincms.module.page.models import Page
from news.models import Entry
from tagging.models import TaggedItem

tagged_models = (
  dict(title="Entries",
    query=lambda tag : TaggedItem.objects.get_by_model(Entry, tag).filter(status=2),
  ),
  dict(title="Pages",
    query=lambda tag: TaggedItem.objects.get_by_model(Image, tag).filter(safetylevel=1),
  ),
)

tagging_ext_kwargs = {
  'tagged_models':tagged_models,
  # You can add your own special template to be the default
  #'default_template':'custom_templates/special.html'
}

urlpatterns += patterns('',
  url(r'^tags/(?P<tag>.+)/(?P<model>.+)$', 'tagging_ext.views.tag_by_model',
        kwargs=tagging_ext_kwargs, name='tagging_ext_tag_by_model'),
  url(r'^tags/(?P<tag>.+)/$', 'tagging_ext.views.tag',
        kwargs=tagging_ext_kwargs, name='tagging_ext_tag'),
  url(r'^tags/$', 'tagging_ext.views.index', name='tagging_ext_index'),
)
