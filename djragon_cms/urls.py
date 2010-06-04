from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    #(r'^news/', include('content.news_urls')),
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
from content.models import NewsArticle

from tagging.models import TaggedItem

tagged_models = (
  dict(title="News Article",
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
