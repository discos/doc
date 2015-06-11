************
Introduction
************

DISCOS TDD cycle
=================
From functionals to unit (summary of :ref:`component-dev`).

Where to put the tests
======================
Tests must be defined in the *tests* directory within the module you are writing::

    $ tree tests/

    tests
    |-- Makefile
    |-- external
    |   `-- __init__.py
    |-- functional
    |   `-- __init__.py
    |-- procedure.cfg
    |-- pyunit
    |   `-- __init__.py
    |-- results
    `-- unittest.cpp

This is the default structure for tests definitions but more complex structures
are also possible, depending on your needs.
Unit tests are defined in *tests/unittest.cpp* while 
the *test/functional* directory and its sub-directories contain the *functional
tests* and, as you probably figured out, the *api* sub-directory hosts the API 
while the *commands* one hosts the command tests. 

.. note:: Do not worry if you do not know this terminology, in the 
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
    doc srt tests
