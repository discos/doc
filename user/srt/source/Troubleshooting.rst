.. _Troubleshooting-and-temporary-procedures:

****************************************
Troubleshooting and temporary procedures
****************************************

The following sections list the solutions to the most common problems 
encountered by users, including indications on how to deal with present bugs 
or inefficiencies in the code. The records are sorted according to the main 
operation areas in which the problems arise. 

.. note:: **Users are advised to read these “hints” at the beginning of the 
   session and before attempting a (likely unnecessary) reboot of 
   the system.** 


Hints and warnings
==================

.. warning:: L/P-BAND OBSERVATIONS: INCOMPATIBLE BACKENDS 

   * **When using the LLP configuration, it is recommended not to use the TPB
     for data acquisition, as the ancillary data recorded inside the FITS
     files are at present inconsistent. It is also important to remember 
     that XARCOS is not compatible with the L/P-band receiver**


.. warning:: DEROTATOR:  

   * **When performing typical cross-scans with the derotator configured in BSC 
     mode, the derotator cannot keep up with the fast axis changes. This does 
     not impact on the observations performed with the central feed, yet the 
     tracking flag will be affected.**

If your tools rely on the tracking flag for any operation, they will assume the
pointing was not good, while the central feed was very likely pointing 
correctly. In this case, for cross-scans remember to configure the derotator 
in fixed mode (by editing your schedule). 


Setup
=====

.. admonition:: PROBLEM: 

   * **The initial setup fails, but it is difficult to assess what goes 
     wrong.**

Instead of using the overall setup commands, give in the *operatorInput* the 
**individual commands** which deal with the different sub-systems, so that it 
is easier to identify the misbehaving element.

For example, the setupLLP command can be substituted by (the actual 
receiversMode code to be used depends on the desired setup):: 

    > antennaReset
    > antennaSetup=LP    
    > servoSetup=LLP     
    > receiversSetup=LLP
    > receiversMode=XXC4
    > initialize=LLP
    > device=0
    > calOff

For other receivers, the codes of course vary. 


.. admonition:: PROBLEM: 

   * **I am using correct commands, but they are not recognized or I am told 
     that arguments are missing**

Are you inserting blank spaces in your command line? Remember that they are not 
allowed. 



Schedules
=========

.. admonition:: PROBLEM:  

    * **I’ve launched a surely correct schedule, but Nuraghe replies that 
      it contains errors and does not run it.** 

Check for typos, as the system does not acknowledge with a proper error 
message the impossibility to find the schedule – e.g. because you wrote 
a **wrong schedule name** – instead it replies that “the schedule contains 
errors”. 



.. admonition:: PROBLEM:  

    * **I’ve launched a surely correct schedule, but parts of the system 
      crashed.**

Pay attention to the syntax, you might have inserted unwanted characters like 
an extra “ / ”: the *startSchedule* command must be either given as::

    > startSchedule=[project]/[schedname].scd,[N]

or, if you have already given the project=code command:: 

    > startSchedule=[schedname].scd,[N]



.. admonition:: PROBLEM:  

    * **Dead time between consecutive subscans is much longer than expected**

Maybe you are using old schedules that still contain  ``wait`` commands in the 
post-scan procedures.
With Nuraghe >0.5 it is incorrect to insert post-scan waiting times in the
schedules, as the system takes automatically care of computing and 
applying proper delays, according to the deceleration ramps duration. 
If you specify a wait time in your post-scan procedures, it will **add** to the 
system-computed delays. 


General failures
================

.. admonition:: PROBLEM:  

    * **Power errors are notified in the ACU control panel**

These errors appear *in the monitoring PCP panel* used by the SD operators, not 
on the observing machines. However, as it is very important to properly deal 
with these errors, we report also in this user's guide how to handle them. 

When the ACU power supply is facing misfunctionings, the error labels 
are enabled (thus they are red) and indicate the "err_Power_Error" label. 
In the jlog window, a "MAIN POWER ERROR" message appears, being assigned a 
CRITICAL priority. 

In these cases, give the following commands in the operatorInput console:: 

    > antennaReset
    > antennaTrack
    
These commands do *NOT* change any previous mount, back-end or front-end setup. 
Thus, after their usage, you do not need to re-configure any device.     


.. admonition:: PROBLEM:  

    * **Activities were interrupted and the antenna stowed without my 
      intervention**

For obvious safety reasons, in case of excessively strong winds the system
interrupts the activities and auto-stows the antenna ("wind park"). 
Do **not** unstow the antenna unless you have been given explicit permission 
by the support staff.    

