.. _Retrieving-the-data: 

*******************
Retrieving the data
*******************


Accessing your disk space
=========================

Each observing project owns disk space on *discos-console*. 
Open a terminal on such machine and use::
   
     $ su - [project-code]

The necessary password is provided by your project friend. 
Once logged in, you will find specific folders under your home folder,
in particular 

     * **data**   Folder containing the data acquired by running schedules
       when observing with XARCOS or the TPB
     * **sardaraData**  Folder containing the data acquired by running schedules
       when observing with SARDARA
     * **extraData**  Folder containing the data acquired by using command lines 
     * **logs**  Folder where logfiles are stored
     * **schedules** Folder where your schedules must be uploaded to
     
Your disk space can also be remotely accessed, as long as you connect to it 
from the SRT campus network. Use::

     $ ssh [project-code]@discos-console

To retrieve your data, open a terminal on your machine and use::

     $ scp -r [project-code]@discos-console:./data/[YYYYMMDD] .
     
For SARDARA data, this becomes::

     $ scp -r [project-code]@discos-console:./sardaraData/[YYYYMMDD] . 

When you need to upload your schedules to the system, instead, open a terminal
on your machine and write::

     $ scp [schedulename].* [project-code]@discos-console:./schedules

   
    
Data structure
==============    
  
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



   
