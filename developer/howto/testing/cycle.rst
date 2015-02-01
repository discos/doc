************
Introduction
************

Nuraghe TDD cycle
=================
From functionals to unit (summary of :ref:`component-dev`).

Where to put the tests
======================
The *test* component directory::

    $ tree test/
    test/
    ├── external
    │   └── __init__.py
    ├── functional
    │   ├── api
    │   │   └── __init__.py
    │   ├── command
    │   │   └── __init__.py
    │   └── __init__.py
    ├── Makefile
    ├── pyunit
    │   └── __init__.py
    ├── results
    └── unittest.cpp

The *test/functional* directory and its sub-directories contain the *functional
tests* and, as you probably figured out, the *api* sub-directory hosts the API 
while the *commands* one hosts the command tests. 

.. note:: Do not warry if you do not now that terminology, in the 
   next sections we will give a definition and
   an explanation of every of these words.

You can create that directory using the ``getTemplateForTest`` 
command. For instance, if you want to create that directory for the
*DewarPositioner* component::

    $ cd $NURAGHE_ROOT/Common/Servers/DewarPositionier
    $ ls
    doc  srt 
    $ getTemplateForTest
    $ ls
    doc srt test
