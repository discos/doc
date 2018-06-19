.. _PythonAPIs:

******
Python
******

System loggings
===============

.. code-block:: discos

   from IRAPy import logger
	logger.logNotice("My system log message")   
   
Custom loggings
===============

.. code-block:: discos

	from IRAPy import userLogger
	logger.logNotice("My user log message")
   
System exceptions
=================

.. code-block:: discos

	from IRAPy import logger
	ex=MyErrroExImpl()
	logger.logException(ex)

Custom exceptions
=================

.. code-block:: discos

	from IRAPy import userLogger
	ex=MyErrroExImpl()
	userLogger.logException(ex)
   
Custom exceptions messages
==========================

.. code-block:: discos

	from IRAPy import logger,_add_user_message
	ex=MyErrroExImpl()
	_add_user_message(ex,"My special message to the user")
	raise ex
	
