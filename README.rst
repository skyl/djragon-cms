Simple, weird, unfinished, configurable, quirky, feature-rich, scalable,
untested, experimental CMS product.

INSTALL
=======

#. Make a virtualenv and activate it.

#. Run ``pip install -r req/requirements.txt``


External Requirements
---------------------

The project currently expects RabbitMQ and Redis to be running locally on their default ports.


RabbitMQ
~~~~~~~~

RabbitMQ is installed on ubuntu with::

    sudo apt-get install rabbitmq-server

On OSX::

    brew install rabbitmq

You will need to setup a broker::

    http://ask.github.com/celery/getting-started/broker-installation.html

In short::

    rabbitmqctl add_user myuser mypass
    rabbitmqctl add_vhost myvhost
    rabbitmqctl set_permissions -p myvhost myuser "" ".*" ".*"

Set the celery settings (perhaps these should all be in local_settings).
I used `skyl` as the user and `transcode` as the vhost.
Then, I put my BROKER_PASSWORD in local_settings.py.

Now you should be able to run celery in development::

    ./manage.py celeryd

Redis
~~~~~

I'm developing against the github master version of redis,
http://github.com/antirez/redis

clone::

    git clone http://github.com/antirez/redis.git

In the created dir, run make::

    path/to/redis$ make

You should be able to run the server with the defaults::

    path/to/redis$ ./redis-server


Now that you have ``RabbitMQ`` and ``redis`` running, you can

#. ``syncdb``

#. ``./manage.py loaddata fixtures/*`` (let's build a good example set of objects.)

