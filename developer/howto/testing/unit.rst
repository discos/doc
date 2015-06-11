.. _unit-testing:

************
Unit testing
************

If your code module is well concieved in terms of object oriented design, it
should contain a lot of little classes each of which encapsulates a well 
determined behavior and is responsible for a well defined set of actions.
That's to say that if you adhere to the 
`single responsibility principle <http://en.wikipedia.org/wiki/Single_responsibility_principle>`_
your code will naturally be divided into code units.
Code units should also be as independent as possible one from each 
other so that each code unit can be executed without referencing the others.

Unit tests are just what the name suggests: portion of code which ensure that
each code unit is performing as expected. These are especially useful for 
documenting the interface of a class by providing real usage examples, and
whenever someone makes a change to a code unit in order to verify that the 
change did not break the behavior of the unit itself.

Within DISCOS we have developed some automation which eases the development 
and the execution of unit tests, and this can be applied to every module 
you write. 

A Library example
=================

We will demonstrate how to write unit tests and how to integrate the tests
development into your own workflow by developing a simple library, 
but the same approach can be used for every code unit defined within discos.

C++ implementation
------------------
.. sectionauthor:: :ref:`mbartolini`

Python implementation
---------------------
.. sectionauthor:: :ref:`mbuttu`

