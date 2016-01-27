.. _Retrieving-the-data: 

*******************
Retrieving the data
*******************

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
 
