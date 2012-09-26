Lightning talk for PythonKC on using Mock to test HTTP requests
===============================================================

This is just a very simple illustration of how to use patch and patch.object
in Mock to make testing code that makes HTTP request much faster in your test
suite.

http://www.voidspace.org.uk/python/mock/

Installation
------------

::

    $ git clone git://github.com/andrewschoen/mock_lightning_talk.git
    $ cd mock_lightning_talk
    $ virtualenv env
    $ source evn/bin/activate
    $ pip install -r requirements.txt
    $ python http_tests.py 
    $ python mocked_http_tests.py

Usage
-----

In http_tests.py and mocked_http_test.py there is a ``HTTP_REQUESTS`` varible.
Increase that number to see how added more HTTP requests to a test suite can
slow it down drastically.

You'll notice that the mocked_http_tests.py doesn't slow down much at all as
the number of http requests increases.  This is why mock is awesome.