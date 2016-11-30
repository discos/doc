.. _EN_Generating-and-launching-a-schedule: 

***********************************
Generating and launching a schedule 
***********************************

A schedule is a set of files where all the geometry/timing/frequency details 
of a sequence of data acquisitions are specified, according to a syntax that 
enables ESCS to read and execute them. 
The detailed structure of the several files composing a schedule is explained 
in this separate guide :download:`pdf <attachments/MED-MAN-SCHEDULES-02.pdf>`
Schedules for the most common observing modes (OTF 
cross-scans and maps, raster maps and ON-OFF) can be easily generated using a 
tool called **basie**. It can be found, together with its user manual, here:
`Basie repository <http://github.com/discos/basie/>`_ 
  
Once a schedule is ready, it must be copied to the folder reserved to the 
schedules.
There, the schedule formal consistency can be tested using the scheduleChecker 
command given within a terminal (*not* in the operatorInput)::

    > scheduleChecker [schedname].scd 

Only the syntax correctness will be verified. If errors are present, a reply 
will briefly address them indicating their position inside the files.  

To launch a schedule, simply use:: 

    > startSchedule=[schedname].scd,[N]

The schedule name is the name of the SCD file. *N* is 
the identifier of the scan or subscan from which ESCS must start reading it 
– it is particularly useful in case of a sequential (i.e. not time-based) 
schedule. *N* can be the scan number, e.g. 2, or the scan_subscan 
specification, e.g. 2_5. 

You can specify **when to start** the schedule (in UT)::

    > startSchedule=[schedname].scd,[N]@[DOY-HH:MM:SS]

ESCS reads the configuration parameters from the schedule, which can be 
relative both to the receiver and the backend, and accordingly sets these 
devices. This might take several seconds, especially when using the MF 
receiver. While the setup takes place, several values change in the TPB 
monitor.
The last operation is the upload of the first pointing/scan read from the 
schedule, whose parameters will show up in the bottom section of the 
AntennaBoss monitor.
During the scans, all the three flags in the lower part of the AntennaBoss 
monitor must be a green “@”. Pay attention to the “Tracking” one. It should 
turn to a red “o” only when the antenna is slewing between scans on the same 
source, or when slewing to/from a new source. **If tracking is not correct for 
some consecutive seconds during a scan, something is wrong.**
Sequential schedules run ad libitum. 
To abruptly interrupt the running schedule, truncating the ongoing 
acquisition::

    > stopSchedule

Instead, to stop the schedule allowing the completion of the present file::

    > haltSchedule








