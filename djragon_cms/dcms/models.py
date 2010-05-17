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

from IPython.Shell import IPShellEmbed
ipython = IPShellEmbed()


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
Page.create_content_type(MediaFileContent, POSITION_CHOICES=(
        ('block', _('block')),
        ('left', _('left')),
        ('right', _('right')),
    ))
Page.create_content_type(ApplicationContent, APPLICATIONS=(
        ('content.frontpage_news_urls', 'Front Page News'),
        ('content.news_urls', 'News Articles'),
    ))
Page.create_content_type(CommentsContent)

import datetime

from django.template.loader import render_to_string
from feincms.module.page.models import Page
from content.models import NewsArticle

two_weeks_ago = lambda: datetime.date.today() - datetime.timedelta(days=14)

class FrontPageNews(models.Model):

    class Meta:
        abstract = True

    def render(self, **kwargs):
        return render_to_string('content/frontpagenews.html', {
            'featured': NewsArticle.objects.filter(featured=True)[:5],
            'popular': NewsArticle.objects.filter(published_date__gte=two_weeks_ago)[:15],
            'latest': NewsArticle.objects.all()[:15]
        })

Page.create_content_type(FrontPageNews)

class FeaturedDescendantsContent(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def render(self, **kwargs):
        #ipython()
        p = Page.objects.best_match_for_request(kwargs['request'])
        return render_to_string('content/featured_descendants_content.html', {
            'title': self.title,
            'featured_pages': p.get_descendants().filter(featured=True),
        })

Page.create_content_type(FeaturedDescendantsContent)

'''
# http://www.feinheit.ch/media/labs/feincms/page.html#adding-another-content-type

from django.db import models
from django.template.loader import render_to_string
from feincms.module.page.models import Page
from gallery.models import Gallery

class GalleryContent(models.Model):
    gallery = models.ForeignKey(Gallery)

    class Meta:
        abstract = True

    def render(self, **kwargs):
        return render_to_string('gallery/gallerycontent.html', {
            'images': self.gallery.image_set.order_by('?')[:5],
        })

Page.create_content_type(GalleryContent)
'''

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
