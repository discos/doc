.. _eventlogging-howto:
 
################################
DISCOS customized logging system
################################

.. sectionauthor:: :ref:`aorlati`, :ref:`mbartolini`


.. topic:: Abstract

	This howto describes how to custom logging API are used inside DISCOS.
	The system is very simple and requires the use of very few APIs or macros.
	It supports (with small differencies both Python and C++). Python implementation
	suffers from several bugs of ACSPy libraries so we put in place some workarounds.
	The basic reference manual of DISCOS custom logging is given in this :download:`document <pdf/logging_subsystem.pdf>`
	from :ref:`mbartolini`. The rest of this section covers some items not described or updated in the above document.
	The general idea behind this implementation is that we'd like to avoid to flood the user with the hundreds of log messages
	generated inside the system. The decision about which message has to be presented to the user is left to the developer.
	The general rule that an exception should be logged only by the initiator of the call sequence (no further throws), remains valid. 
	In summary the following items are covered:
	
	* System loggings (messages are not shown to the user, they are stored in system log file)
	
	* Custom loggings (messages are reported to the user, the same message is stored into both system and user logfile)
	
	* System exceptions (The user is not directly notified of the exception and the event is logged only into system log file)
	 
	* Custom exceptions (The user is notified of the exception and the event is logged into both system and user log file)
	 
	* Interaction with operator input (This is a special case allowing the developer to present a specific message to the user when an exception is risen inside an operation triggered by the user. The message is shown in the operator input)

Contents:

.. toctree::
   :maxdepth: 2
   
   cpp.rst
   python.rst

