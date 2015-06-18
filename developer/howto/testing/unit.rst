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


DISCOS Integration
==================

Within **DISCOS** we have developed some automation which eases the development and
the execution of unit tests, and this can be applied to every module you write. 

We will demonstrate how to write unit tests and how to integrate the tests
development into your workflow by developing a simple library, 
the same approach can be used for every code unit defined within discos.

The library we will develop is a unit of code we can use to connect to an
external backend according to the protocol specified in :ref:`Backend protocol 
<backend_protocols>`.


GOOGLE Tests
------------

Within **DISCOS** we are using the third party libraries
**google test** and **google mock** to ease the writing and execution of tests.
Documentation for these libraries can be found online at:

* `Google test introduction
  <https://code.google.com/p/googletest/wiki/Primer>`_ is a must read for
  everyone using this library for the first time and contains very introductory
  material. You can keep this document at your disposal while writing your first
  tests or reading this guide.

* `Google test advanced guide
  <https://code.google.com/p/googletest/wiki/AdvancedGuide>`_ contains more
  advanced documentation about more complex assert statements, exceptions ecc...

* `Google mock for dummies
  <https://code.google.com/p/googlemock/wiki/ForDummies>`_ is the introductory
  material for the google mock library. Mocking is a slightly advanced topic in
  developing unit tests, expecially when it comes to C++ implementations. you
  should read this guide if you are developing tests which contain dependencies
  from external objects.

Install
~~~~~~~

Google mock and google test frameworks are automatically installed by the
provisioning scripts defined in `azdora <https://github.com/discos/azdora>`_
projects. If you are running on a different machine you can still use `azdora
gmock script <https://github.com/discos/azdora/blob/master/bash/gmock.sh>`_ as a
reference for installation. It is important that you do not change the paths
where libraries are installed if you want to rely on all the automations defined
within the **DISCOS** framework.

C++ implementation
------------------
.. sectionauthor:: :ref:`mbartolini`

We start by writing our first test in our **tests** directory generated with
**getTemplateForTest** script. We thus edit *tests/unittest.cpp* to define a
simple behavior for our **Request** class: this will encapsulate a
request message we'd like to send to our backend server:

.. code-block:: c++
   :linenos:

   #include "gtest/gtest.h"

   #include "grammar.h"

   using namespace backend;

   TEST(MessageTest, MessageRequestConstruction){
       Request request("myrequest");
       EXPECT_EQ("?myrequest", request.toString());
   }

Note how we already define how we'd like the class to behave.

* Line 1 includes the necessary google tests headers.
* Line 3 This file is still not defined but it will contain the necessary
  definitions
* Line 7 defines a new unit test using the **TEST** macro defined in google
  library. The two parameters define a test-case-name and a test-name which will
  be used in the final report to identify and group unit test results.
* Line 8 defines the behaior of our Request class
* Line 9 is the actual test we are performing. We are using the **EXPECT_EQ**
  macro to check that our class is behaving as expected.

.. note::
   We are leaving out some boilerplate code from this online guide for better
   readability. You can download :download:`the complete archive <cpp_unittest_example.tar.gz>`
   containing the full working code.

Next step will be to define the code which will make this test pass. So we
define a simple *ExternalBackendLibrary/include/grammar.h*:

.. code-block:: c++
   :linenos:

    #include <string>
    #include <vector>

    #include <boost/algorithm/string.hpp>

    #define BACKEND_REQUEST '?'
    #define BACKEND_REPLY '!'
    #define BACKEND_REPLY_OK "ok"
    #define BACKEND_REPLY_INVALID "invalid"
    #define BACKEND_REPLY_FAIL "fail"
    #define BACKEND_SEPARATOR ","

    using namespace std;

    namespace backend{

    class Message
    {
        public:
            Message(const char message_type,
                    const char* name,
                    vector<string> arguments = vector<string>()) :
                m_type(message_type),
                m_name(name),
                m_arguments(arguments){};
            virtual ~Message();
            virtual string toString() = 0;
        protected:
            const char m_type;
            string m_name;
            vector<string> m_arguments;
    }; //class Message

    class Request : public Message
    {
        public:
            Request(const char* name,
                    vector<string> arguments = vector<string>()) :
                    Message(BACKEND_REQUEST,
                            name,
                            arguments){};
            virtual string toString();
    }; //class Request

    }; //namespace backend
 

And the corresponding *ExternalBackendLibrary/src/grammar.cpp* implementation: 

.. code-block:: c++
   :linenos:

    #include "grammar.h"

    using namespace backend;

    string
    Request::toString()
    {
        ostringstream output;
        output << BACKEND_REQUEST << m_name;
        return output.str();
    }

The Makefile for this library will be composed of:

.. code-block:: make
   :linenos:

    INCLUDES        = grammar.h
    LIBRARIES       = ExternalBackend
    ExternalBackend_OBJECTS   = grammar
    ExternalBackend_LDFLAGS   = -lstdc++

We have to compile and install the library in order to run our test. Once
compiled we need to adjust the test Makefile in
*ExternalBackendLibrary/tests/Makefile* as:

.. code-block:: make
   :linenos:

    EXECUTABLES_L = unittest
    unittest_OBJECTS = unittest
    unittest_LIBS = $(GTEST_LIBS) ExternalBackend
    unittest_LDFLAGS = -lstdc++ -lpthread

Note that in line 3 we are adding the link to the library we want to test, this
could also be a component library or any other unit of code. Now we can try to
compile our test:

.. code-block:: bash

    developer@15:34:02:ExternalBackendLibrary $ cd tests
    developer@15:34:05:tests $ make
    == Creating Missing directories
    /alma/ACS-8.2/ACSSW/include/acsMakefile.all:382: ../object/unittest.d: No such
    file or directory
    /alma/ACS-8.2/ACSSW/include/acsMakefile.all:388: ../object/unittest.dx: No such
    file or directory
    == Dependencies: ../object/unittest.dx
    == Dependencies: ../object/unittest.d


    == C++ Compiling: unittest.cpp
    == Building executable: ../bin/unittest


     . . . 'all' done

And run it with **make unit**:

.. code-block:: bash

    developer@15:34:12:tests $ make unit
    == Creating Missing directories


     . . . 'all' done
     running cpp unit tests
     ../bin/unittest --gtest_output=xml:results/cppunittest.xml
     Running main() from gtest_main.cc
     [==========] Running 1 test from 1 test case.
     [----------] Global test environment set-up.
     [----------] 1 test from MessageTest
     [ RUN      ] MessageTest.MessageRequestConstruction
     [       OK ] MessageTest.MessageRequestConstruction (0 ms)
     [----------] 1 test from MessageTest (2 ms total)

     [----------] Global test environment tear-down
     [==========] 1 test from 1 test case ran. (6 ms total)
     [  PASSED  ] 1 test.
      . . . 'unit' done

From the output it should be clear that one of one tests executed has passed.

Exceptions
~~~~~~~~~~

Now we want to add a function which will parse a line of text and turn it into a
reply message. We can proceed like the previous request case:

.. code-block:: c++

    TEST(MessageTest, ParseGoodReply){
        string message("!prova,ok,1,2,3");
        Reply msg = parseReply(message.c_str());
        EXPECT_EQ(msg.toString(), message);
    }

And we define the necessary Reply class in our library module.
In grammar.h: 

.. code-block:: c++

    class Reply : public Message
    {
        public:
            Reply(const char* name,
                  const char* code,
                  vector<string> arguments = vector<string>()) :
                  Message(BACKEND_REPLY,
                            name,
                            arguments),
                  m_code(code){};
            virtual string toString();
        private:
            string m_code;
    }; //class Reply

    Reply parseReply(const char*);

And in the grammar.cpp:

.. code-block:: c++
   :linenos:

    Reply
    backend::parseReply(const char* msg)
    {
        string msg_string(msg);
        // first character must be BACKEND_REPLY
        if(!(msg_string[0] == BACKEND_REPLY))
            throw GrammarError("not a valid reply");
        // type + name + separator + reply_code
        if(!(msg_string.length() >= 4))
            throw GrammarError("reply must contain at least 4 characters");
        vector<string> split_msg;
        boost::split(split_msg, msg_string, boost::is_any_of(BACKEND_SEPARATOR));
        if(split_msg.size() < 2)
            throw GrammarError("reply must contain at least a name and a reply code");
        string msg_name = split_msg[0].substr(1, string::npos);
        string msg_code = split_msg[1];
        if((!(msg_code == BACKEND_REPLY_OK)) &&
           (!(msg_code == BACKEND_REPLY_FAIL)) &&
           (!(msg_code == BACKEND_REPLY_INVALID)))
            throw GrammarError("not a valid reply code");
        vector<string> msg_arguments(split_msg.begin() + 2, split_msg.end());
        return Reply(msg_name.c_str(), msg_code.c_str(), msg_arguments);
    }

As you can see in lines 7, 10, 14 and 20, the parsing function raises an exception if the reply string does
not conform to the protocol. We want to add a check to our test, that the
exception does not get risen if the string is correct, and obviously we want to
make sure that the exception is risen when appropriate. Our test will become:

.. code-block:: c++

    TEST(MessageTest, ParseGoodReply){
        string message("!prova,ok,1,2,3");
        Reply msg;
        ASSERT_NO_THROW({
            msg = parseReply(message.c_str());
        });
        EXPECT_EQ(msg.toString(), message);
    }

    TEST(MessageTest, ParseBadReply){
        string bad_type_reply("#prova,ok,1,2,3");
        string bad_code_reply("!prova,badcode,1,2,3");
        EXPECT_THROW(parseReply(bad_type_reply.c_str()), GrammarError);
        EXPECT_THROW(parseReply(bad_code_reply.c_str()), GrammarError);
    }

We introduced the **ASSERT_NO_THROW** and **EXPECT_THROW** macros, defined in
google test framework. Every macro in the framework appears with both the
*ASSERT_* and the *EXPECT_* prefixes, if the assert fails the unit test is
interrupted while if the expect fails the unit test is not interrupted and
successive instructions within the unittest are also executed.

Test Fixtures
~~~~~~~~~~~~~

As you can see we are using some variables within our tests. Now we'll show how
to add some code to every test by using test fixtures: we will demonstrate it by
adding the message strings to the test case initialization and using the strings
so defined in each successive test:

.. code-block:: c++
   :linenos:

    class Messages : public ::testing::Test {
        public:
            static const char *good_request, *bad_request, *good_reply_ok,
                              *good_reply_fail, *good_reply_invalid, *bad_reply_type,
                              *bad_reply_code; //*
    };

    const char * Messages::good_request = "?prova,1,2,3";
    const char * Messages::bad_request = "#prova,1,2,3";
    const char * Messages::good_reply_ok = "!prova,ok,1,2,3";
    const char * Messages::good_reply_fail = "!prova,fail,1,2,3";
    const char * Messages::good_reply_invalid = "!prova,invalid,1,2,3";
    const char * Messages::bad_reply_type = "#prova,invalid,1,2,3";
    const char * Messages::bad_reply_code = "!prova,badcode,1,2,3";

    TEST_F(Messages, ParseBadReply){
        EXPECT_THROW(parseReply(bad_reply_type), GrammarError);
        EXPECT_THROW(parseReply(bad_reply_code), GrammarError);
    }

* In line 1 we defined a new class inheriting from **::testing::Test** , this is
  the base class for our unit tests. 
* In line 16 we use the **TEST_F** macro which tells the framework that this
  unit test has fixtures and must inherit from the type specified as the first
  argument of the macro.
* Within the unit test with fixtures now we have access to all the variables and
  methods defined in the fixture class.

Test Fixtures can be much more complex than this simple example, in particular
they can define special methods such as **setUp** and **tearDown** which get
executed for each unit test. We will see how to use those procceding in our
example.

Mocking
~~~~~~~

.. todo::
   Add example implementation of a connection to an external server and use
   google mock for testing the implementation.

Python implementation
---------------------
.. sectionauthor:: :ref:`mbuttu`

