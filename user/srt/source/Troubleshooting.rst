.. _Troubleshooting-and-temporary-procedures:

****************************************
Troubleshooting and temporary procedures
****************************************

The following sections list the solutions to the most common problems 
encountered by users, including indications on how to deal with present bugs 
or inefficiencies in the code. The records are sorted according to the main 
operation areas in which the problems arise. 

.. note:: **Users are advised to read these “hints” at the beginning of the 
   session and before attempting a (possibly unnecessary) reboot of 
   the system.** 


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


Schedules
=========

.. admonition:: PROBLEM:  

    * **I’ve launched a surely correct schedule, but Nuraghe replies that 
      it contains errors and does not run it.** 

Check for typos, as the system does not acknowledge with a proper error 
message when the commanded schedule is not found – e.g. because you wrote 
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

With Nuraghe 0.5 it is necessary to delete from the schedules all the post-scan 
wait times, as the system now takes automatically care of computing and 
applying proper delays according to the deceleration ramps duration. 
If you specify a wait time in your post-scan procedures, it will add to the 
system-computed delays. 

