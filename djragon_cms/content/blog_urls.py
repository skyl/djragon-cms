from django.conf.urls.defaults import *
from content.models import Blog

entry_dict = {'queryset': Blog.objects.all()}

urlpatterns = patterns('',
    url(r'^$', 'content.views.blog_front_page', name='entry_list'),
    url(r'^articles/(?P<slug>[-\w]+)/$',
        'django.views.generic.list_detail.object_detail',
        dict(entry_dict, **{'slug_field': 'slug'}),
        name='entry_detail'),

    # We could do other generic views and such.
    #url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[^/]+)/',
    #    'django.views.generic.date_based.object_detail',
    #    dict(entry_dict, **{'date_field': 'published_date', 'month_format': '%m', 'slug_field': 'slug'}),
    #    name='entry_detail'),
)

