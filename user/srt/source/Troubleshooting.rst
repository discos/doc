.. _Troubleshooting-and-temporary-procedures:

****************************************
Troubleshooting and temporary procedures
****************************************

The following sections list the solutions to the most common problems 
encountered by users, including indications on how to deal with present bugs 
or inefficiencies in the code. The records are sorted according to the main 
operation areas in which the problems arise. 


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

   * **I am using correct commands, but they are not recognized or I am told 
     that arguments are missing**

Are you inserting blank spaces in your command line? Remember that they are not 
allowed. 



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

