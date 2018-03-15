White: Black, but brighter (PEP8–inspired)
==========================================

`Black <https://github.com/ambv/black>`_ is an amazing tool for auto–formatting
Python code in a style that I prefer. I use it in all my projects.

It has **one** configuration option — to change its default line–length of ``88``
chars to, say, ``79``, like `PEP8 <http://pep8.org>`_ recommends.

That is exactly what this tool does. It invokes ``$ black --line-length 79`` on your behalf.


Usage
=====

::

    $ white myapp.py
    reformatted myapp.py
    

.. image:: http://share.kennethreitz.org/2L2m1U1A3m0L/Screen%20Shot%202018-03-15%20at%206.21.04%20AM.png


Installation
============

::

	$ pipenv install white
	✨🍰✨
