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
so the receiver will have just a few methods, one property, a
notification channel and an external component reference. The
interface is the following:

.. code-block:: c++

   #ifndef __DUMMY_RECEIVERS__IDL__ 
   #define __DUMMY_RECEIVERS__IDL__

   #include <baci.idl>
   #include <maciErrType.idl>
   #include <ComponentErrors.idl>

   #pragma prefix "alma"


   module DummyReceivers {

       struct DummyReceiversDataBlock {
           boolean ready;
       };

       const string DUMMY_RECEIVERS_DATA_CHANNEL = "DummyReceiversData";

       interface MyReceiver:
           ACS::CharacteristicComponent,
           Management::CommandInterpreter
       {

           /** Take a configuration code and configure the receiver
            * 
            * This method takes a configuration code, gets the corresponding
            * local oscillator and initialize MyReceiver.
            * For instance, by giving the code KKG, MyReceiver gets the 
            * KBand local oscillator reference and performs its setup.
            */
           void setup(in string code) raises (ComponentErrors::ComponentErrorsEx);


           /** Return the actual setup configuration (KKG, etc.) */
           string getActualSetup();
       };
   };
   
   #endif

   /* TO BE DONE:
      - setLO()
      - command()
      - temperature read-only double property
      - the receiver component has to monitor its local oscillator by 
        checking the ``LO.isReady()`` method: if ``isReady()`` returns ``true``
        the receiver publishes ``true`` to the ``ready`` field of the NC,
        otherwise ``false``.
   */



Python components
=================


C++ components
==============

