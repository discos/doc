.. _unit-testing:

************
Unit testing
************

Unit tests are just what the name suggests: portion of code which ensure that
each code unit is performing as expected. These are especially useful for
documenting the interface of a class by providing real usage examples, and
whenever someone makes a change to a code unit in order to verify that the
change did not break the behavior of the unit itself.

Principles
==========

Contrary to what may seem obvious, unit testing involves much more the design of
your code rather then the testing of already written code.  That's why we talk
about *Test Driven Development*, because if you develop with testing in your
mind, and also writing tests first, your code will result better conceived,
better designed, more maintanable and easily documented and usable by other
memebers of your team. 

Unit testing and TDD enforce the adoption of `SOLID
<https://en.wikipedia.org/wiki/SOLID_%28object-oriented_design%29>`_ principles
when writing your code, and this is expecially true for C++ code: if your code
module is well concieved in terms of object oriented design, it should contain a
lot of little classes each of which encapsulates a well determined behavior and
is responsible for a well defined set of actions.  That's to say that if you
adhere to the `single responsibility principle
<http://en.wikipedia.org/wiki/Single_responsibility_principle>`_ your code will
naturally be divided into code units. Also, dependency management between code
modules will be better managed if you adhere to `dipendency inversion
<https://en.wikipedia.org/wiki/Dependency_inversion_principle>`_ principles.  We
will see how both of these requirements will be necessary for writing effective
tests and wil lead to better code design and implementation.

.. note::
   Unit tests can be effectively developed also on already written code to
   ensure its stability and safe refactoring. Even if it is not called TDD it
   will provide good value to your code.


DISCOS Implementation
=====================

Within DISCOS we have developed some automation which eases the development and
the execution of unit tests, and this can be applied to every module you write. 

We will demonstrate how to write unit tests and how to integrate the tests
development into your workflow by developing a simple library, 
the same approach can be used for every code unit defined within discos.

C++ implementation
------------------
.. sectionauthor:: :ref:`mbartolini`

Python implementation
---------------------
.. sectionauthor:: :ref:`mbuttu`

