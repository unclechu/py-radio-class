Radio
=====

Event-bus implementation inspired by `backbone.radio`__.

__ https://github.com/marionettejs/backbone.radio

Install
-------

.. code:: bash

  pip install sleekxmpp

Usage
-----

Here are some small examples that demonstrate how to use it:

on/off/trigger
~~~~~~~~~~~~~~

.. code:: python

  from radio import Radio
  radio = Radio()
  
  def foo(arg): print('argument:', arg)
  radio.on('bar', foo) # bind 'foo' handler on 'bar' event
  radio.trigger('bar', 123) # "argument: 123" will be shown in output
  
  def baz(arg): print('baz handler was triggered')
  radio.on('bar', baz) # bind another handler on same event
  radio.trigger('bar', 456) # "argument: 456" and then "baz handler was triggered" will be shown in output
  
  radio.off('bar', baz) # unbind previously bound handler
  radio.trigger('bar', 789) # now only "argument: 789" will be shown

once
~~~~

You could bind some handler that automatically unbounds after first trigger.

.. code:: python

  from radio import Radio
  radio = Radio()
  
  def foo(arg): print('argument:', arg)
  radio.once('bar', foo) # bind 'foo' handler on 'bar' event
  radio.trigger('bar', 123) # "argument: 123" will be shown in output
  radio.trigger('bar', 456) # nothing shown in output

request/reply/stopReplying
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

  from radio import Radio
  radio = Radio()
  
  def sum(a=5, b=10): return a + b
  radio.reply('get-sum', sum) # bind 'sum' replier-handler on 'get-sum' requests
  x = radio.request('get-sum')
  print(x) # 15 will be shown in output (5 + 10 from default arguments)
  x = radio.request('get-sum', b=2, a=4)
  print(x) # 6 will be shown
  x = radio.request('get-sum', 2)
  print(x) # 12 will be shown
  radio.stopReplying('get-sum', sum)
  radio.request('get-sum') # will raise 'ListenerNotFound' exception

Author
------

`Viacheslav Lotsmanov`__

__ https://github.com/unclechu/

License
-------

`MIT`__

__ LICENSE
