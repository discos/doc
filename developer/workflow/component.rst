.. _component-dev:

*******************
Write the component
*******************

In this section we will see how to write a component, adopting 
the TDD in each and every step.
We will write a receiver component, both in Python and in C++. 

IDL interface
=============
We would like the example to be as clear and simple as possible,
so the receiver will have just a few methods, one property, one
notification channel and an external component reference. The
interface is the following:

.. code-block:: c++

    #ifndef __DUMMY_RECEIVER__IDL__ 
    #define __DUMMY_RECEIVER__IDL__

    #include <baci.idl>
    #include <maciErrType.idl>
    #include <ComponentErrors.idl>
    #include <ManagmentDefinitions.idl>

    #pragma prefix "alma"


    module DummyReceiver {
     
        struct DummyReceiverDataBlock {
            boolean ready;
        };

        const string DUMMY_RECEIVER_DATA_CHANNEL = "DummyReceiverData";

        interface MyReceiver: 
            ACS::CharacteristicComponent,
            Management::CommandInterpreter
        {
            /** Take a configuration code (VLBI or SD) and set the receiver */
            void setConfiguation(in string code) raises (ComponentErrors::ComponentErrorsEx);


            /** Return the actual configuration (VLBI, SD) */
            string getConfiguration();


            /** Set the local oscillator value */
            void setLO(in ACS::doubleSeq value);


            /** Get the local oscillator value */
            ACS::doubleSeq getLO();


            readonly attribute ACS::RWdouble temperature;
        };
    };

    #endif

The default configuration is the described below::

    >>> from Acspy.Clients.SimpleClient import PySimpleClient
    >>> client = PySimpleClient()
    >>> receiver = client.getComponent('RECEIVERS/MyReceiver')
    >>> receiver.getConfiguration() # Default configuration
    'SD'
    >>> receiver.getLO() # Default LO value
    [1500, 1500]

We can change the configuration at any time::
   
    >>> receiver.setLO([2000, 2000])
    >>> receiver.getLO()
    [2000, 2000]

Eventually, the receiver has to monitor the ``LO`` component
status, by checking the ``LO.isReady()`` method. When that
method returns ``true``, the ``ready`` field of the
``DummyReceiverDataBlock`` must be ``true``, otherwise it must
be ``false``.


Python components
=================


C++ components
==============

