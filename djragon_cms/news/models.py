from django.db import models

from datetime import datetime
from django.db import models

class Entry(models.Model):
    published_date = models.DateField()
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField(blank=True)

    class Meta:
        get_latest_by = 'published_date'
        ordering = ['-published_date']
        verbose_name_plural = 'entries'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('entry_detail', (), {
            'year': self.published_date.strftime('%Y'),
            'month': self.published_date.strftime('%m'),
            'day': self.published_date.strftime('%d'),
            'slug': self.slug,
            })


