.. _EN_Initial-setup:

*************
Initial setup
*************

.. _EN_overall_setup:

Antenna overall setup
=====================

When opening an ESCS observing session, it is necessary to perform a setup 
which includes the antenna unstow, the mount configuration in tracking mode, 
the minor servo setup. This is done by means of a unique command, which is 
specific for the wanted receiver, to be written in the **operatorInput**. 
The currently available choices are::

    > setupCCC     for the C-band receiver 

.. note:: Spaces within the command line content are **not** allowed!

The above setup command sets the antenna mount, the minor servos, the selected 
receiver and the default backend (TotalPower) according to **default 
parameters**. The antenna mode is set to **ProgramTrack** (allowing tracking 
and the execution of schedules), while the Local Oscillator frequency and the 
bandwidth are set as illustrated in the following table.


.. tabularcolumns:: |c|c|c|c|c|

========  ==========  ==========  ==============  ==========  =================
Receiver  LO freq     Frontend    Backend         Observed    Observed
                      RF band     IF band         bandwidth   band
--------  ----------  ----------  --------------  ----------  -----------------
code      \(MHz\)     \(MHz\)     \(MHz\)         \(MHz\)     \(MHz\)
========  ==========  ==========  ==============  ==========  ================= 
CCC       4600        4620-5020   50-730          400         4620-5020
========  ==========  ==========  ==============  ==========  =================

Notice that the true observed band depends on the **intersection between the 
frontend IF band and the chosen backend filter**. The actual observed 
bandwidth and the band starting frequency are recorded in the output files 
(see :ref:`EN_Appendix-C-Output-files`).



Logfile and project code
========================

The default logfile is named **station.log**. 
If the user wants to change it::

    > log=[logfilename]  (without extension)

Logfiles are stored in a dedicated folder (see Retrieving the data).
**When schedules are run, a new logfile is automatically started**, and it is 
named after the schedule: [schedulename].log.
   
 
