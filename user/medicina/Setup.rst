.. _E_Initial-setup:

*************
Initial setup
*************

.. _E_overall_setup:

Antenna overall setup
=====================

When opening an ESCS observing session, it is necessary to perform a setup 
which includes the antenna unstow, the mount configuration in tracking mode, 
the minor servo setup. This is done by means of a unique command, which is 
specific for the wanted receiver, to be written in the **operatorInput**. 
The currently available choices are::

    > setupCCCL  for the C-band receiver (narrow bandwidth)
    > setupCCC   for the C-band receiver (wide bandwidth)
    > setupXXP   for the X-band receiver
    > setupKKC   for the K-band receiver 


.. note:: Spaces within the command line content are **not** allowed!

The above setup command sets the antenna mount, the minor servos, the selected 
receiver and the default backend (TotalPower) according to **default 
parameters**. The antenna mode is set to **ProgramTrack** (allowing tracking 
and the execution of schedules), while the Local Oscillator frequency and the 
bandwidth are set as illustrated in the following table.


.. tabularcolumns:: |c|c|c|c|c|

========  ==========  ==========  ==============  ==========  =================
Receiver  LO freq     Frontend    Backend         Observed    Observed
                      IF band     IF band         bandwidth   band
--------  ----------  ----------  --------------  ----------  -----------------
code      \(MHz\)     \(MHz\)     \(MHz\)         \(MHz\)     \(MHz\)
========  ==========  ==========  ==============  ==========  ================= 
CCCL      4600        100-250     50-250           150        4700-4850
CCC       4600        100-900     50-780           680        4700-5380
XXP       8080        100-900     50-780           680        8180-8860 
KKC       21964       100-2100    50-2400          2000       22064-24064
========  ==========  ==========  ==============  ==========  =================

Notice that, depending on the devices in use, the sky frequency at the 
observed band starting point is given by the LO frequency plus an offset. For 
the present combinations of the frontends *with the total power backend*, 
which the above table refers to, this offset is 100 MHz. 
In general, the true observed band depends on the **intersection between the 
frontend IF band and the chosen backend filter**. The actual observed 
bandwidth and the band starting frequency are recorded in the output files 
(see :ref:`E_Appendix-C-Output-files`).



Logfile and project code
========================

The default logfile is named **station.log**. 
If the user wants to change it::

    > log=[logfilename]  (without extension)

Logfiles are stored in a dedicated folder (see Retrieving the data).
**When schedules are run, a new logfile is automatically started**, and it is 
named after the schedule: [schedulename].log.

It is possible, and advisable, to insert the project code/name (a string 
assigned to the project by the TAC) using the command::

    > project=[projectcode]   (e.g. project=scicom)      

This will make the user save time in later stages, as it will not be necessary 
to specify the project name in schedule-launching commands. The project 
code/name must correspond to an existing user, already known to the system. 
This means that, if its spelling does not match with the recorded name, an 
error rises.
 
