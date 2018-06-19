.. _C++APIs:

***
C++
***

System loggings
===============

This are normal ACS logging macros. 

.. code-block:: discos

   ACS_LOG(LM_FULL_INFO,"MyModule::MyClass::MyMethod",(LM_INFO,"My system log message")); 
   
Custom loggings
===============

.. code-block:: discos

   #include <IRA>
   CUSTOM_LOG(LM_FULL_INFO, "MyModule::MyClass::MyMethod", (LM_ALERT, "My user log message"));
   
System exceptions
=================

.. code-block:: discos

		_EXCPT(ErrorsNamespace::MyErrroEventExImpl,dummy,"MyModule::MyClass::MyMethod");
		dummy.log(LM_DEBUG); // 
		throw dummy; // if required
   
Custom exceptions
=================

.. code-block:: discos
	
	#include <IRA>
	_EXCPT(ErrorsNamespace::MyErrroEventExImpl,dummy,"MyModule::MyClass::MyMethod");
	CUSTOM_EXCPT_LOG(dummy,LM_ERROR);
	throw dummy; // if required

   
Custom exceptions messages
==========================

.. code-block:: discos

	#include <IRA>
	_EXCPT(ErrorsNamespace::MyErrroEventExImpl,dummy,"MyModule::MyClass::MyMethod");
	_ADD_USER_MESSAGE(dummy,"My special message to the user"); // Show in the operator input if the error was triggered by an user command 
	throw dummy; // this will be logged by the caller
