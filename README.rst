Simple, configurable, feature-rich, scalable CMS product.

INSTALL
=======

#. Make a virtualenv and activate it.

#. Run ``pip install -r req/requirements.txt``

#. ``syncdb``

#. ``./manage.py loaddata fixtures/*`` - let's build a good example set of objects.

#. ``./manage.py runserver --adminmedia=./media/grappelli``


