.. _functional-testing:

******************
Functional testing
******************
.. sectionauthor:: :ref:`mbuttu`

A test is called  *functional* when it aims to verify the component
behavior from the user point of view.
The components usually have two kind of users:

1. **operators** (human beings) who interact with the component 
   through the  *operator input* console
2. **programs** (clients or other components) that interact
   with the component by using its API (calling its methods)

In the first case, we should verify the behavior of the commands the operator
sends to our component. In other words, we we have to test the 
component ``command()`` method. We call this kind of functional tests by the
name of *command tests*.

In the second case, we should verify all the other methods defined
in the component IDL interface. We should prove they give us the expected
results, and when required they raise the expected exceptions. We give this
functional tests the name of *API tests*.

Writing functional tests in Python is really straightforward, and of course
it is easier than C++, so we will use it in this section.
The Python standard library provides a unit test framework, called
`unittest <https://docs.python.org/2/library/unittest.html>`_. Unfortunatly
the Python version we can use with ACS-8.2 is the old Python 2.5, and in its
unittest module there is a lack of useful assertions. The solution
is to install a third part module,
`unittest2 <https://pypi.python.org/pypi/unittest2>`_, in order to use it
in place of the standard library unittest module:

.. code-block:: bash

    $ easy_install unittest2 # Install the unittest2 library

Let's have a real example: the *DewarPositioner* component. We will see 
both how to write a command and an API test. 

Command tests
=============
In this section we will test the ``derotatorSetup`` command. As we said
before, we have to think from the user (the astronomer in that case)
point of view. So, let's see what the user wants to obtain
after executing the command from the *operatorInput* console:

.. code-block:: discos

    > derotatorSetup=KKG
    >

Well, we are ready to write our functional test. The file and the
methods must start
with *test*, so we can create a file called *test_derotatorSetup.py* inside
the *functional/commands* directory::

    # File: test/functional/commands/test_derotatorSetup.py
    import unittest2
    from Acspy.Clients.SimpleClient import PySimpleClient
    from DewarPositioner.DewarPositionerImpl import DewarPositionerImpl
    
    
    class DerotatorSetupCmdTest(unittest2.TestCase):
        """Test the derotatorSetup and derotatorGetActualSetup commands"""
    
        def test_proper_setup(self):
            # Get the component
            client = PySimpleClient()
            dp = client.getComponent('RECEIVERS/DewarPositioner')

            # Send the component a command
            success, answer = dp.command('derotatorSetup=KKG')
            # Verify the command is executed as expected
            self.assertEqual(answer, '') 

            # Release the component and disconnect the client
            client.releaseComponent('RECEIVERS/DewarPositioner')
            client.disconnect()
    
    if __name__ == '__main__':
        unittest2.main()

Before implementing the code, we write just the component interface
without writing the command execution method. We do not write the method
implementation because we want to get an expected failure. In that case, we expect the 
test fails saying the command does not exist.

.. important:: One of the most important things about testing is to be sure
   the tests can fail. It is better do not have a test than to have one
   that does not fails when it should do.

Let's start the test:

.. code-block:: bash

    $ python test_derotatorSetup.py 

    ======================================================================
    FAIL: test_proper_setup (__main__.DerotatorSetupCmdTest)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "test_derotatorSetup.py", line 19, in test_proper_setup
        self.assertEqual(answer, '')
    AssertionError: 'Error - command derotatorSetup does not exist' != ''

    ----------------------------------------------------------------------
    Ran 1 test in 1.388s

    FAILED (failures=1)


As we can see from the output message, only one test has been run, and it
failed as expected, with a straighforward error message.
Now we are ready to write the ``derotatorSetup`` command code. Let's write it,
and than we run again the test, of course offline.
To spin up the test offline we need to simulate the external resources. The  
``DewarPositioner`` gets a reference to a derotator component, and this one 
communicates to the hardware. The best approach is to simulate the external
resource API, but in our case, because the derotator protocol is a bit
complex, we choose to implement a simulator of the ACS derotator component.
To get this component ready, we just have to point to the testing CDB:

.. code-block:: bash

    $ export ACS_CDB=~/Nuraghe/ACS/trunk/SRT/

We can now start ACS and the required containers:

.. code-block:: bash

   $ acsStartContainer -py DerotatorsContainer
   $ acsStartContainer -py DewarPositionerContainer

Let's spin up the test:

.. code-block:: bash

    $ python test_derotatorSetup.py 
    .
    ----------------------------------------------------------------------
    Ran 1 test in 2.825s

    OK


.. todo:: Show the test execution

If we write a wrong setup code we want the component to behave this way:

.. code-block:: discos

    > derotatorSetup=GIGIRIVA
    Error - setup GIGIRIVA not available"

So, we write an additional test that verifies this case:

.. code-block:: python


    # File: test/functional/commands/test_derotatorSetup.py
    import unittest2
    from Acspy.Clients.SimpleClient import PySimpleClient
    from DewarPositioner.DewarPositionerImpl import DewarPositionerImpl


    class DerotatorSetupCmdTest(unittest2.TestCase):
        """Test the derotatorSetup and derotatorGetActualSetup commands"""

        def test_proper_setup(self):
            # Get the component
            client = PySimpleClient()
            dp = client.getComponent('RECEIVERS/DewarPositioner')

            # Send the component a command
            success, answer = dp.command('derotatorSetup=KKG')
            # Verify the command is executed as expected
            self.assertEqual(answer, '')

            # Release the component and disconnect the client
            client.releaseComponent('RECEIVERS/DewarPositioner')
            client.disconnect()

        def test_wrong_setup(self):
            # Get the component
            client = PySimpleClient()
            dp = client.getComponent('RECEIVERS/DewarPositioner')

            # Send the component a command
            success, answer = dp.command('derotatorSetup=GIGIRIVA')
            # Verify the answer starts with 'Error'
            self.assertTrue(answer.startswith('Error'))

            # Release the component and disconnect the client
            client.releaseComponent('RECEIVERS/DewarPositioner')
            client.disconnect()

    if __name__ == '__main__':
        unittest2.main()

As we can see, we added a new test, called ``test_wrong_setup()``. In that test
we command a ``derotatorSetup`` with a wrong error code, and we assert that the
answer starts with ``'Error'``. We also notice that our code smells,
because there is a lot of duplication among the two tests.
The ``unittest`` framework provides special methods, called ``setUp()`` and
``tearDown()``, that it calls respectively before and after each test. So, we can
refactor our test case moving the common code inside this two methods:

.. code-block:: python

    # File: test/functional/commands/test_derotatorSetup.py
    import unittest2
    from Acspy.Clients.SimpleClient import PySimpleClient
    from DewarPositioner.DewarPositionerImpl import DewarPositionerImpl
    
    
    class DerotatorSetupCmdTest(unittest2.TestCase):
        """Test the derotatorSetup and derotatorGetActualSetup commands"""
    
        def setUp(self):
            self.client = PySimpleClient()
            self.dp = self.client.getComponent('RECEIVERS/DewarPositioner')
    
        def tearDown(self):
            self.client.releaseComponent('RECEIVERS/DewarPositioner')
            self.client.disconnect()
    
        def test_proper_setup(self):
            success, answer = self.dp.command('derotatorSetup=KKG')
            self.assertTrue(success)
            self.assertEqual(answer, '')
    
        def test_wrong_setup(self):
            success, answer = self.dp.command('derotatorSetup=GIGIRIVA')
            self.assertFalse(success)
            self.assertTrue(answer.startswith('Error'))
    
    if __name__ == '__main__':
        unittest2.main()


.. _test api:

API tests
=========
In this section we will see how to write an API test. To follow the previous
example, we will test the ``DewarPositioner.setup()`` method. Let's 
start peeking at the IDL interface:

.. code-block:: cpp

    /* Take a configuration code and configure the component
     * 
     * This method takes a configuration code, gets the corresponding
     * derotator component reference and initializes the DewarPositioner. 
     * For instance, by giving the code KKG, the DewarPositioner gets the 
     * KBandDerotator reference and performs its setup. It also sets the
     * rewinding mode and configuration default values as:
     *
     *     setConfiguration('FIXED')
     *     setRewindingMode('AUTO')
     *
     * @param code the setup mode (for instance: LLP, KKG, CCB, ecc.)
     * @throw ComponentErrors::ComponentErrorsEx in case of wrong
     * configuration code or derotator component not available
     */
    void setup(in string code) raises (ComponentErrors::ComponentErrorsEx);

We should write a test similar to the previous one. In particular, we want the 
the ``setup()`` to raise a ``ComponentErrorsEx`` in case of wrong code.
Our test could be the following one:

.. code-block:: python

    # File: test/functional/test_setup.py
    from __future__ import with_statement
    import unittest2
    import time

    from ComponentErrors import ComponentErrorsEx
    from Acspy.Clients.SimpleClient import PySimpleClient


    class SetupTest(unittest2.TestCase):
        """Test the DewarPositioner.setup() method"""

        def setUp(self):
            self.client = PySimpleClient()
            self.dp = self.client.getComponent('RECEIVERS/DewarPositioner')

        def tearDown(self):
            self.client.releaseComponent('RECEIVERS/DewarPositioner')
            self.client.disconnect()

        def test_proper_setup(self):
            self.dp.setup('KKG')
            self.assertEqual(self.dp.getActualSetup(), 'KKG')

        def test_wrong_setup(self):
            with self.assertRaises(ComponentErrorsEx):
                self.dp.setup('GIGIRIVA')


    if __name__ == '__main__':
        unittest2.main()

.. note:: The import ``from __future__ import with_statement`` is required
   in Python 2.5 when, as in this case, we use the ``with`` statement.
