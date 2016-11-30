.. _ESCSN-startup:

************
ESCS startup
************


Logistics
=========

.. note:: **passwords are provided locally**. Be sure to contact the local 
   personnel before your session starts, in order to get the latest information. 

Observations involve the use of two machines, called escs and euser, located 
in the 32-m dish control room: 

.. figure:: images/Postazioni_ESCSN.png
   :scale: 80%
   :alt: Observing machine
   :align: center
 
On-site observations
====================

The involved hardware is composed by two PCs with displays on the table facing 
the window, just next to the AS control panel.
When the observers perform their acquisitions on-site, they exploit the 
euser machine only (the one on the right). 

escs: input terminal and system monitors
----------------------------------------------

Login to euser using the provided credentials. 
Then, click on the "ESCS" icon located on the Desktop. It will connect you to 
escs via a Remote Desktop (vinagre).
On escs, you should find the input terminal and all the monitors already 
running. If, instead, you need to start them, open a terminal on the escs 
remote desktop and give::

	> escsClients 

This opens 8 panels at once: 

    * operatorInput - terminal for command line input
    * antennaBoss 
    * observatory 
    * mount 
    * genericBackend
    * receiversBoss
    * scheduler
    * logging

Rearrange the panels on the desktop. 

In case any of them does not automatically start, you can manually open them 
by means of individual command lines, to be given in the open terminal::

	> operatorInput 
	> antennaBossTui 
	> observatoryTui 
	> mountTui 
	> genericBackendTui BACKENDS/TotalPower  
	> receiversBossTui
	> schedulerTui
	> loggingDisplay

All the antenna/receiver/backend setup procedures are performed via the 
operatorInput window, which is also used to start/stop the schedules. 

The other panels are monitors used to display a vast amount of information, 
see :ref:`EN_Appendix-A-Monitor-panels-full-description` and 
:ref:`EN_Appendix-B-Complete-command-list` for a comprehensive description of 
their content and a list of all the commands available for the operatorInput 
(they can be inserted in schedules as well).

euser: access to schedules, logs and data
-----------------------------------------------

Directly use euser for the data quicklook and retrieval (see dedicated 
sections), for the generation of schedules using the "basie" tool and for tools 
as FV.
Once logged in, in your home you can find the following folders, whose names 
are self-explanatory::

    ~/data  
    ~/schedules
    ~/logs

.. note:: users can generate subfolders according to their needs to store 
   their schedules, but, in order to be executed, schedules must be places 
   *exactly* in their ~/schedules folder. 


(Remotely controlled observations): under development
=====================================================

It is possible to remotely perform the observations, exploiting a VNC 
connection to escs. Open a VNC session and connect to::

	192.167.187.XXX:1  (i.e. port 5901) 

You will be asked to insert a password (again, passwords are provided by the 
local staff). If you need to start the clients, open a terminal and command::

	> escsClients

and follow the same instructions provided for observations carried out on site. 

To access your data, schedules and logs, simply open a terminal on your 
computer and use::

	> ssh –X euser@192.167.187.16 

Hence you can launch IDL, use basie, retrieve your data, etc… 

