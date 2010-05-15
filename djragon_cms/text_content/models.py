from django.db import models

from datetime import datetime
from django.db import models

class Author(models.Model):
    '''News author'''

    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

class Blog(models.Model):
    '''The blogs and opinions bit'''
    published_date = models.DateField()
    author = models.ForeignKey('Author')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog_detail', (), {'slug': self.slug,})

class NewsArticle(models.Model):
    published_date = models.DateField()
    author = models.ForeignKey('Author')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField(blank=True)

    class Meta:
        get_latest_by = 'published_date'
        ordering = ['-published_date']

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('entry_detail', (), {'slug': self.slug,})

