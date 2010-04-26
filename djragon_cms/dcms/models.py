from django.db import models






# Feincms particulars see:
# http://www.feinheit.ch/media/labs/feincms/page.html

from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent
from feincms.content.image.models import ImageContent

Page.register_extensions('datepublisher', 'translations') # Example set of extensions

Page.register_templates({
    'title': _('Standard template'),
    'path': 'base.html',
    'regions': (
        ('main', _('Main content area')),
        ('sidebar', _('Sidebar'), 'inherited'),
    ),
})

Page.create_content_type(RichTextContent)
Page.create_content_type(ImageContent, POSITION_CHOICES=(
        ('block', _('block')),
        ('left', _('left')),
        ('right', _('right')),
    )
)


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


