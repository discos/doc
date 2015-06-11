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

Unit tests are just what the name suggest: portion of code which ensure that
each code unit is performing as expected. 

C++
===
.. sectionauthor:: :ref:`mbartolini`

Python
======
.. sectionauthor:: :ref:`mbuttu`

