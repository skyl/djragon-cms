import datetime

from django.db import models

from filebrowser.fields import FileBrowseField


class Author(models.Model):
    '''News author'''

    name = models.CharField(max_length=150)
    image = FileBrowseField("Portrait",
        max_length=200, format='Image', directory='images/authors/', blank=True, null=True)

    def __unicode__(self):
        return self.name

class Blog(models.Model):
    '''The blogs and opinions bit'''
    published_date = models.DateField(default=datetime.date.today)
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
    published_date = models.DateField(default=datetime.date.today)
    author = models.ForeignKey('Author')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField(blank=True)
    featured = models.BooleanField()

    image = FileBrowseField("Image",
        max_length=200, format='Image', directory='images/news/', blank=True, null=True)

    class Meta:
        get_latest_by = 'published_date'
        ordering = ['-published_date']

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('entry_detail', (), {'slug': self.slug,})

