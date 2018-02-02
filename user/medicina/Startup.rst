.. _ESCS-startup:

************
ESCS startup
************


Logistics
=========

.. note:: **passwords are provided locally**. 
   Be sure to contact the single-dish operations staff before your session 
   starts, in order to get the latest information. 

Observations are always carried out through a VNC remote connection to a 
machine called escsRemote. Once connected, some of the operations must be 
carried out connecting via ssh to another machine called escsConsole.  

escsRemote: ESCS panels
-----------------------
 
Open a VNC session and connect to::

	192.167.189.57:2  (i.e. port 5902) 

You will be asked to insert a password. 
A remote desktop will then appear. In it, the ESCS system should already be up 
and running, and you should see all the textual clients referring to the 
different containers of the system. If you don't see them, first check the 
bottom bar, as they might have been reduced to icons. 
If indeed they are all missing and you need to start the clients, 
open a terminal and use::

	$ escsClients

This opens 9 panels at once: 

    * operatorInput - terminal for command line input
    * antennaBoss 
    * observatory 
    * mount 
    * genericBackend (x2)
    * receiversBoss
    * scheduler
    * logging

Rearrange the panels on the desktop. 

In case any of them does not automatically start, you can manually open them 
by means of individual command lines, to be given in a terminal shell::

	$ operatorInput 
	$ antennaBossTui 
	$ observatoryTui 
	$ mountTui 
	$ genericBackendTui BACKENDS/TotalPower
	$ genericBackendTui BACKENDS/XArcos
	$ receiversBossTui
	$ schedulerTui
	$ loggingDisplay

All the antenna/receiver/backend setup procedures are performed via the 
operatorInput window, which is also used to start/stop the schedules. 

The other panels are monitors used to display a vast amount of information, 
see :ref:`E_Appendix-A-Monitor-panels-full-description` and 
:ref:`E_Appendix-B-Complete-command-list` for a comprehensive description of 
their content and a list of all the commands available for the operatorInput 
(they can be inserted in schedules as well).

escsConsole: access to schedules, logs and data
-----------------------------------------------

Use escsConsole for the data quicklook and retrieval (see dedicated 
sections), for the generation of schedules using basie and for tools 
as DS9 or FV. 
Login credentials are specific to each project, you will connect via ssh 
as follows, using a terminal shell (you can take advantage of the different
virtual desktops, in order not to crowd the system desktop)::  

	$ ssh –X projectName@192.167.189.54

in your home you can find the following folders, whose names are 
self-explanatory::

    ~/data  
    ~/schedules
    ~/logs

.. note:: users can generate subfolders according to their needs to store 
   their schedules, but, in order to be executed, schedules must be places 
   exactly in their ~/schedules folder. 


