.. _EN_Retrieving-the-data: 

*******************
Retrieving the data
*******************

Open a terminal on the euser machine. Your data folder is::

    ~/data

Inside that folder, subfolders named according to the date (YYYYMMDD) will be 
automatically created during acquisitions. 
Taking into account the choice of the FITS format, the only one so far fully 
tested, the date-dependent folder contains a subfolder for every scan, inside 
which there are the FITS files (one for each subscan).

.. figure:: images/FolderScheme.png
   :scale: 60%
   :alt: Data storage scheme
   :align: left 


Scan folder names are composed as: 

**YYYMMDD-HHMMSS-User-Suffix**

where 
	
    * **HHMMSS** is the UT time associated to the first sample of the 
      acquisition
    * **User** is the user code (at the moment it can only be "euser") 
    * **Suffix** is a user-defined string retrieved from the schedule files. 
	  Though no control can be applied on the choice/check of this string, 
	  the agreement is that it should coincide with the target name. 

FITS files, each corresponding to a subscan, are composed as: 

**YYYYMMDD-HHMMSS-User-Suffix_Scan#_Subscan#.fits**

Data can be copied from *escsConsole* to your laptop using  'ssh’  or   
‘rsync –e ssh’  commands.


.. note:: When recording manually-acquired data in FITS format, the output 
   files are still accessible from the euser machine, yet they are found in a 
   peculiar path, different from the one employed when schedules run.
   You can find these FITS files in /archive/extraData. 
   This implies that they also cannot be automatically showed by the quick-look 
   procedure. 

You can retrieve your logfiles here::

    ~/logs

Its reply will let you know where the logfiles are located. A subfolder named 
*/WindLog* is devoted to the meteoClient output, if this client is used. 
 
