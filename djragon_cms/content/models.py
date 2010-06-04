import datetime

from django.db import models

from filebrowser.fields import FileBrowseField
from tagging.fields import TagField

from djredis.models import DredisMixin

class Author(models.Model):
    '''News author'''

    name = models.CharField(max_length=150)
    image = FileBrowseField("Portrait",
        max_length=200, format='Image', directory='images/authors/', blank=True, null=True)

    def __unicode__(self):
        return self.name


import djredis.models
from djongobj.models import Mongo, Document, Collection


class MyDoc(Document):
    foo = 'MyDoc wuz here'


class MyCollection(Collection):
    bar = 'MyCollection wuz here'


class Blog(models.Model, DredisMixin):
    '''The blogs and opinions bit'''
    published_date = models.DateField(default=datetime.date.today)
    author = models.ForeignKey('Author')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    description = models.TextField(blank=True, editable=False)
    featured = models.BooleanField()
    tags = TagField(blank=True)
    image = FileBrowseField("Image",
        max_length=200, format='Image', directory='images/news/', blank=True, null=True)

    views = models.PositiveIntegerField(blank=True, null=True, editable=False)
    object_pickle = models.TextField(blank=True, editable=False)


    # djredis http://github.com/skyl/djredis
    viewcount = djredis.models.Incr()
    mystring = djredis.models.String()
    myobject = djredis.models.Object()
    myhash = djredis.models.Dict()
    mylist = djredis.models.List()
    followers = djredis.models.Set()
    group = djredis.models.Zset()

    mongo = Mongo(document_class=MyDoc, collection_class=MyCollection)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog_detail', (), {'slug': self.slug,})


# http://github.com/skyl/djredis
Blog.add_incr_to_class('blog_counter')
Blog.add_string_to_class('nocase')
Blog.add_object_to_class('classobject')
Blog.add_dict_to_class('classdict')
Blog.add_list_to_class('classlist')
Blog.add_set_to_class('classset')
Blog.add_zset_to_class('classzset')


class NewsArticle(models.Model):
    published_date = models.DateField(default=datetime.date.today)
    author = models.ForeignKey('Author')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField(blank=True)
    featured = models.BooleanField()
    tags = TagField(blank=True)
    image = FileBrowseField("Image",
        max_length=200, format='Image', directory='images/news/', blank=True, null=True)

    mongo = Mongo()

    class Meta:
        get_latest_by = 'published_date'
        ordering = ['-published_date']

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('entry_detail', (), {'slug': self.slug,})

"""
class CategorizedArticle(models.Model):
    '''For Content that is neither news nor opinion but meant to be included under specific pages'''
    category = models.ForeignKey('Category')
    published_date = models.DateField(default=datetime.date.today)
    author = models.ForeignKey('Author')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField(blank=True)
    featured = models.BooleanField()
    tags = TagField(blank=True) #we need some tags to categorize the content (not news)
    image = FileBrowseField("Image",
        max_length=200, format='Image', directory='images/news/', blank=True, null=True)

    class Meta:
        get_latest_by = 'published_date'
        ordering = ['-published_date']

    def __unicode__(self):
        return self.title
    '''
    # these will get included in the page explicitly
    # special Content objects for feincms will be created for "latest" etc as needed
    @models.permalink
    def get_absolute_url(self):
        return ('entry_detail', (), {'slug': self.slug,})
    '''
"""

'''
#Metaprogramming test

from functools import partial


#what I want to mixin
def foo(self, key=None):
    full_key = '%s:%s' % (self.base_key(), key)
    return full_key


class FooMixin:
    @classmethod
    def register(cls, key):
        cls.add_to_class(key, partial(foo, key=key))


#define and register
class Bar(models.Model, FooMixin):
    def base_key(self):
        return '%s:%s:%s' % (self._meta.app_label, self._meta.module_name, self.id)

#Bar.register('this')

class C(object):
    def __getattr__(self, attr):
        key, meth = attr.partition("_")
        def temp():
            return getattr(self, meth)(key)
        return meth

     def bar(self, key):
         return 'yp'

c = C()
c.foo_bar()
'''
