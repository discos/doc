.. _EN_Troubleshooting-and-temporary-procedures:

****************************************
Troubleshooting and temporary procedures
****************************************

The following sections list the solutions to the most common problems 
encountered by users, including indications on how to deal with present bugs 
or inefficiencies in the code. The records are sorted according to the main 
operation areas in which the problems arise. 

.. note:: **Users are advised to read these “hints” at the beginning of the 
   session and before attempting (possibly unnecessary) heavy-handed operations 
   on the system.** 


Setup
=====

.. admonition:: PROBLEM: 

   * **The initial setup fails, but it is difficult to assess what goes 
     wrong.**

Instead of using the overall setup commands, give in the *operatorInput* the 
**individual commands** which deal with the different sub-systems, so that it 
is easier to identify the misbehaving element.

For example, the setupXXP command can be substituted by (the actual 
receiversMode code to be used depends on the desired setup):: 

    > antennaReset
    > antennaSetup=XXP    
    > servoSetup=XXP     
    > receiversSetup=XXP
    > initialize=XXP    
    > device=0
    > calOff

For other receivers, the codes of course vary. 



Schedules
=========

.. admonition:: PROBLEM:  

    * **I've performed cross-scans in order to fine-tune the pointing, but
      the measured offsets are not actually applied to the following 
      acquisitions**
    
System offsets, such as the ones measured with a Point acquisition, sum up to 
the ones indicated inside schedules ONLY if they are expressed in the same 
coordinate frame. This means that, if you perform observations using EQ offsets, 
also the fine-pointing cross-scans must be carried out in the EQ frame. The 
same holds for HOR scans. If there is a frame mismatch, the system offsets are 
automatically rejected (bug under fixing).


.. admonition:: PROBLEM:  

    * **I’ve launched a surely correct schedule, but parts of the system 
      crashed.**

Pay attention to the syntax, you might have inserted unwanted characters like 
an extra “ / ”: the *startSchedule* command must be either given as::

    > startSchedule=[project]/[schedname].scd,[N]

or, if you have already given the project=code command:: 

    > startSchedule=[schedname].scd,[N]


