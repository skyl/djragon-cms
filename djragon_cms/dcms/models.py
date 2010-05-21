from django.db import models

from django.utils.translation import ugettext_lazy as _

# Feincms particulars see:
# http://www.feinheit.ch/media/labs/feincms/page.html
from feincms.module.page.models import Page
# some of the available contenttypes
# http://www.feinheit.ch/media/labs/feincms/contenttypes.html
from feincms.content.richtext.models import RichTextContent
from feincms.content.image.models import ImageContent
from feincms.content.medialibrary.models import MediaFileContent
from feincms.content.application.models import ApplicationContent
from feincms.content.raw.models import RawContent
from feincms.content.rss.models import RSSContent
from feincms.content.comments.models import CommentsContent

#from IPython.Shell import IPShellEmbed
#ipython = IPShellEmbed()

Page.register_extensions(
    'changedate',
    'datepublisher',
    'navigation',
    'seo',
    'symlinks',
    'titles',
    'featured',
    #'translations',
)
Page.register_templates({
    'title': _('Standard template'),
    'path': 'base.html',
    'regions': (
        ('banner', _('banner ad'), 'inherited'),
        ('main', _('Main content area')),
        ('sidebar', _('Sidebar'), 'inherited'),
        ('footer', _('Footer'), 'inherited')
    ),
})
Page.create_content_type(RichTextContent)
Page.create_content_type(RawContent)

import datetime

from django.template.loader import render_to_string
from feincms.module.page.models import Page
from content.models import NewsArticle, Blog

two_weeks_ago = lambda: datetime.date.today() - datetime.timedelta(days=14)


class FrontPageNews(models.Model):

    class Meta:
        abstract = True

    def render(self, **kwargs):
        featured = NewsArticle.objects.filter(featured=True)[:5],
        latest = NewsArticle.objects.all()[:15]

        return render_to_string('content/frontpagenews.html', {
            'featured': featured,
            'latest': latest,
        })
Page.create_content_type(FrontPageNews)


class FrontPageBlogs(models.Model):

    class Meta:
        abstract = True

    def render(self, **kwargs):
        return render_to_string('content/frontpageblogs.html', {
            'featured': Blog.objects.filter(featured=True)[:5]
        })
Page.create_content_type(FrontPageBlogs)


class FeaturedDescendantsContent(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def render(self, **kwargs):
        p = Page.objects.best_match_for_request(kwargs['request'])
        return render_to_string('content/featured_descendants.html', {
            'title': self.title,
            'featured_pages': p.get_descendants().filter(featured=True),
        })
Page.create_content_type(FeaturedDescendantsContent)


class LatestDescendants(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def render(self, **kwargs):
        p = Page.objects.best_match_for_request(kwargs['request'])
        return render_to_string('content/latest_descendants.html', {
            'title': self.title,
            'latest_pages': p.get_descendants().order_by('-publication_date')[:10],
        })
Page.create_content_type(LatestDescendants)


class LatestDescendantsByChild(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def render(self, **kwargs):
        p = Page.objects.best_match_for_request(kwargs['request'])
        children = p.get_children() #.order_by('-publication_date')

        return render_to_string('content/latest_descendants_by_child.html', {
            'title': self.title,
            'children': children,
        })
Page.create_content_type(LatestDescendantsByChild)

Page.create_content_type(ApplicationContent, APPLICATIONS=(
        ('content.news_urls', 'News Articles'),
        ('content.blog_urls', 'Blogs and Opinions'),
    ))
Page.create_content_type(CommentsContent)


''' # Using page request processors
def authenticated_request_processor(page, request):
    if not request.user.is_authenticated():
        return HttpResponseForbidden()

Page.register_request_processors(authenticated_request_processor)
'''

''' # using page response processors
def set_random_header_response_processor(page, request, response):
    response['X-Random-Number'] = 42

Page.register_response_processors(set_random_header_response_processor)
'''

'''
# Very stupid etag function, a page is supposed the unchanged as long
# as its id and slug do not change. You definitely want something more
# involved, like including last change dates or whatever.
def my_etag(page, request):
    return 'PAGE-%d-%s' % ( page.id, page.slug )
Page.etag = my_etag

Page.register_request_processors(Page.etag_request_processor)
Page.register_response_processors(Page.etag_response_processor)
'''
