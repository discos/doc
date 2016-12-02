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

    > setupSXP     for the SX-band receiver
    > setupCCC     for the C-band receiver 
    > setupMMC     for the M-band receiver
    > setupKKC     for the K-band receiver
    > setupQQC     for the Q-band receiver

.. admonition:: WARNING:  

    * It is necessary to manually select the observing focus using the hardware 
      IF switch located in the control room. The figure below illustrates this
      rack.  

.. figure:: images/Focus_switch.jpg
   :scale: 80%
   :alt: Hardware switch in charge of selecting the IF lines to be used, i.e. 
   selecting the observing focus. 
   :align: center

The general setup command sets the antenna mount, the minor servos, the selected 
receiver and the default backend (TotalPower) according to **default 
parameters**. The antenna mode is set to **ProgramTrack** (allowing tracking 
and the execution of schedules), while the Local Oscillator frequency and the 
bandwidth are set as illustrated in the following table.


.. tabularcolumns:: |c|c|c|c|c|

========  ==========  ============  ==========  ==========  =================
Receiver  |LO freq    |Frontend     |Backend    |Observed   |Observed
          |           |RF band      |IF band    |bandwidth  |band
--------  ----------  ------------  ----------  ----------  -----------------
code      \(MHz\)     \(MHz\)       \(MHz\)     \(MHz\)     \(MHz\)
========  ==========  ============  ==========  ==========  ================= 
SXP       |2020       |2200-2360    |50-730     |160        |2200-2360
          |8080       |8180-8580    |50-730     |400        |8180-8580
--------  ----------  ------------  ----------  ----------  -----------------
CCC       4600        4620-5020     50-730      400         4650-5020
--------  ----------  ------------  ----------  ----------  -----------------
MMC (1)   6956        5100-7250     50-730      500         6356-6856 
--------  ----------  ------------  ----------  ----------  -----------------
KKC       21869       21500-23000   50-730      400         21969-22369        
--------  ----------  ------------  ----------  ----------  -----------------
QQC       42850       39000-43500   50-730      400         42950-43350
========  ==========  ============  ==========  ==========  =================

Notice that the true observed band depends on the **intersection between the 
frontend IF band and the chosen backend filter**. The actual observed 
bandwidth and the band starting frequency are recorded in the output files 
(see :ref:`EN_Appendix-C-Output-files`).

(1) For this setup, the FITS file will **NOT** report the actual values 
relative to frequency and bandwidth, as the present ESCS release does not take 
into account the different conversion taking place for this receiver. 
  

Logfile
=======

The default logfile is named **station.log**. 
If the user wants to change it::

    > log=[logfilename]  (without extension)

Logfiles are stored in a dedicated folder (see Retrieving the data).
**When schedules are run, a new logfile is automatically started**, and it is 
named after the schedule: [schedulename].log.
   
 
