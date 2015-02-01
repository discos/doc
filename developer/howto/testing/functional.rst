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

In the first case, we have to verify the behavior of the commands the operator
sends to our component. In other words, we we have to test the 
component ``command()`` method. We call this kind of functiona tests by the
name of *command tests*.

In the second case, we have to verify all the other methods defined
in component IDL interface. We should prove they give the expected
results and when required, they raise the expected exceptions. We give this
functional tests the name of *API tests*.

Writing functional test in Python is really straightforward, and of course
it is easier than C++, so we will use it in this section.
In the Python standard library there is a unit test framework, called
`unittest <https://docs.python.org/2/library/unittest.html>`_. Unfortunatly
the Python version provied by ACS-8.2 is the old Python 2.5, and its
unittest module does not have a lot of useful assertions. The solution
is to install a third part module,
`unittest2 <https://pypi.python.org/pypi/unittest2>`_, in order to use it
in place of the standard library unittest module.

Let's have a real example: the *DewarPositioner* component. We will see 
both how to write a command and an API test (one method and one property).

Command tests
=============
In this section will test the ``derotatorSetup`` command. As we said
before, we have to think from the user (the astronomer in that case)
point of view. So, let's see what the user wants to obtain
after executing the command from the *operatorInput* console::

    > derotatorSetup=KKG
    >

Well, we are ready to write our functional test. The file and the
methods must start
with *test*, so we can create a file called *test_derotatorSetup.py* inside
the *functional/commands* directory::

    # File: test/functional/commands/test_derotatorSetup.py
    import unittest2
    from DewarPositioner.DewarPositionerImpl import DewarPositionerImpl


    class DerotatorSetupCmdTest(unittest2.TestCase):

        def test_proper_setup(self):
            dp = DewarPositionerImpl()
            success, answer = dp.command('derotatorSetup=KKG')
            self.assertTrue(success) # assertEqual(success, True)
            self.assertEqual(answer, '')

    if __name__ == '__main__':
        unittest2.main()


.. todo:: Show the test execution

In case of wrong setup code, the command returns an error message::

    > derotatorSetup=GIGIRIVA
    Error...

We can add the related test, called ``test_wrong_setup()``::

    # File: test/functional/commands/test_derotatorSetup.py
    import unittest2
    from DewarPositioner.DewarPositionerImpl import DewarPositionerImpl


    class DerotatorSetupCmdTest(unittest2.TestCase):

        def setUp(self):
            self.dp = DewarPositionerImpl()

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

The ``setUp()`` method is called before each test.

Although the ``DerotatorSetupCmdTest`` looks easy, it is very effective because
now we can modify the component and run the tests. If it passes, we did not
break the command.

To verify the whole setup behavior, we should write an API test, as described
in the section :ref:`test api`.


Guidelines
----------
The ``derotatorGetActualSetup`` command prints the actual 
``DewarPositioner`` setup::

        > derotatorGetActualSetup
        none
        > derotatorSetup=KKG
        > derotatorGetActualSetup
        KKG

So we can think to write  the ``test_proper_setup()`` in the following
way::

        def test_proper_setup(self):
            success, answer = self.dp.command('derotatorSetup=KKG')
            self.assertTrue(success)
            self.assertEqual(answer, '')
            success, answer = self.dp.command('derotatorGetActualSetup')
            self.assertTrue(success)
            self.assertEqual(answer, 'KKG')

That's not a good idea, because the tests must be as simple as possible,
because we want to take easy both their maintenance and readability. 
We have to avoide code duplication between tests and ideally, each test 
should have only one assertion. As a rule ot thumb, we can think a long 
test is an indication of code smell.

Our first version of ``test_proper_setup()`` does already everything
we need, because it check the ``derotatorSetup`` command:

    * exists
    * is correctly executed in case of right setup code
    * prints an error message in case of failure
    
In that case, the problem of the duplication of code between tests
can happen only if we write the code before the test. 
In fact, if the component code is not yet written, we start by
writing the setup test, and that test must check only the 
``derotatorSetup`` command. Once the test is written, we write the
``setup()`` method and then the ``derotatorSetup`` command.
Our test can not pass if we put a ``derotatorGetActualSetup``
check inside it, because the ``getActualSetup()`` method and the
related ``derotatorGetActualSetup`` command do not exist.
That's one of the reasons we have to follow the 
`TDD <http://en.wikipedia.org/wiki/Test-driven_development>`_
approach. Another one is the TDD ensures a bigger code coverage
than a *testing after coding* approach.

So, if we want to verify the ``derotatorGetActualSetup`` returns
the ``KKG`` code, first of all we have to write the test::

    # File: test/functional/commands/test_derotatorGetActualSetup.py
    import unittest2
    from DewarPositioner.DewarPositionerImpl import DewarPositionerImpl


    class DerotatorGetActualSetupCmdTest(unittest2.TestCase):

        def test_rigth_code(self):
            dp = DewarPositionerImpl()
            dp.command('derotatorSetup=KKG')
            success, answer = dp.command('derotatorGetActualSetup')
            self.assertEqual(success, True) 
            self.assertEqual(answer, 'KKG')

    if __name__ == '__main__':
        unittest2.main()

Now we have to verify the test does not pass (of course, if it pass there is
a problem in the test itself). That is called an *expected failure*.
After we get an expected failure, we can start writing the code.

.. _test api:

API tests
=========
In this section we will see how to write an API test, for instance
a test for the ``DewarPositioner.setup()`` method. Here is
its IDL interface:

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
