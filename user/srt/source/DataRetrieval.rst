.. _Retrieving-the-data: 

*******************
Retrieving the data
*******************

    
TPB and XARCOS FILES
====================    
To know where your data folders are located, open a terminal on OBS2 and 
execute::

    $ mySession

.. note:: Please notice that files recorded running a schedule and 
   manually-acquired files are stored in different folders. 
   
Inside the data folders, subfolders named according to the date (YYYYMMDD) 
will be automatically created during acquisitions. 
Taking into account the choice of the FITS format, the date-dependent folder 
contains a subfolder for every scan, inside which there are the FITS files 
(one for each subscan).

.. figure:: images/FolderScheme.png
   :scale: 60%
   :alt: Data storage scheme
   :align: left 

Scan folder names are composed as: 

**YYYMMDD-HHMMSS-Project-Suffix**

where 
	
    * **HHMMSS** is the UT time associated to the first sample of the 
      acquisition
    * **Project** is the code/name specified using the ``project=`` command, 
	  or when starting a schedule with 
	  ``startSchedule=[project/][schedulename].scd,[N]``
    * **Suffix** is a user-defined string retrieved from the schedule files. 
	  Though no control can be applied on the choice/check of this string, 
	  the agreement is that it should coincide with the target name. 

FITS files, each corresponding to a subscan, are composed as: 

**YYYYMMDD-HHMMSS-Project-Suffix_Scan#_Subscan#.fits**

Data can be copied from *nuraghe-obs2* to your laptop using  'ssh’  or   
‘rsync –e ssh’  commands.

.. warning:: Do not send data using the Internet, because bandwidth is 
   insufficient. 

The above-mentioned 'mySession' command also indicates where the logfiles are 
stored. A subfolder named */WindLog* is devoted to the meteoClient output, when 
this client is used. 


SARDARA FILES
=============

To know where your data folders are located, and how to access them, open a 
terminal on OBS2 and execute::

    $ mySession 
    
The acquired raw data do not contain any information other than a timestamp and 
the data streams. In order to complete them with all the info relative to the 
telescope (e.g. the pointed coordinates, etc.) and obtain the usual FITS files, 
it is necessary to perform a merging procedure. 
**Once the schedule has ended** (or was stopped), open a terminal on OBS1 and 
use:: 

    $ _send_backend_command 
  

Browse your data through the web
================================

A really basic web-browsing and retrieving system is available 
from the account observer @nuraghe-obs3

The web link is

  * http://nuraghe-data

For each [project] you will find a browsable folder for schedules, 
manually-acquired data, Total Power and XARCOS data, SARDARA data and logfiles 
respectively at: 

  * http://nuraghe-data/[project]/schedules
  
  * http://nuraghe-data/[project]/auxiliary 
  
  * http://nuraghe-data/[project]/tp-xarcos  
  
  * http://nuraghe-data/[project]/sardara 
  
  * http://nuraghe-data/logs 

You can retrieve your data using wget Linux standard command. The basic 
syntax to download recursively directories starting from [project]/[somefolder] 
is::

  $ wget -r -c -l2 -np http://nuraghe-data/[project]/[somefolder]

This will make a nuraghe-data/[project]/[somefolder] directory tree into your 
home.  

You can also start the 'wget' user interface giving:: 

  $ guiwget 

and choose options by checkbuttons. 


Copying the data
================

If you want to take away your data you can: 

  * start wget or scp command from your laptop, or

  * connect an external usb2/3 disk to the nuraghe-obs3 workstation (usb ports 
    are available on its rear side), then change directory to put yourself into 
    a folder of your disk and finally start a wget or scp command. 

**Please be careful**

If you start getting data from a folder in the local /home/observer home disk 
on observer @nuraghe-obs3, you will have no more than 390 GB of available space, 
depending on the previously loaded files.
This is a only a **scratch and common area**: it will be cleaned at least once 
a week, so don't park there any critical data or info.

   
