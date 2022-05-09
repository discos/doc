.. _EN_Appendix-B-Complete-command-list:

**********************************
Appendix B - Complete command list
**********************************

.. note:: **COMMAND TEMPORISATION** All commands can be temporised (i.e. 
   associated to a starting time) adding a proper **suffix**. There are 
   two possibilities:

  * **absolute temporisation** (the operation will be performed at the 
    indicated time): ``@DOY-HH:MM:SS``, where DOY is the Day-Of-Year (1-366) 
    and HH:MM:SS is the UT time; 
  * **iterative temporisation** (the operation is performed now, then 
    periodically according to the indicated time interval): 
    ``@!DAYS-HH:MM:SS``, where DAYS is the number of days and HH:MM:SS is 
    hours, minutes, seconds.

Commands (temporised or not) can be used also in the init/pre-scan/post-scan 
procedures inside schedules. 
*Observers* are in charge of considering *if* and *when* the use of a certain 
command makes sense in their schedule, according to their specific needs and 
goals: this is something that no schedule parser can check!

Here follow all the commands exploitable in ESCS:

.. note:: Spaces within the command line content are **not** allowed!

.. describe:: > antennaPark

   sends the antenna to stow position

.. describe:: > antennaReset

   resets the alarm conditions

.. describe:: > antennaSetup=[code] 
   
   (``code`` can be ``PRIM`` or ``SEC``)
   unstows the antenna, sets it to tracking mode and configures the 
   pointing model according to the specified focus (primary or secondary). 
   It does NOT perform the receiver and backend setup

.. describe:: > antennaStop

   stops the antenna. Activities can start again only commanding a 
   mode change as ``antennaTrack`` (which does not affect the overall setup) or 
   a new setup

.. describe:: > antennaTrack

   sets the antenna to PROGRAMTRACK mode. 
   It does not change the pointing model or any receiver setup
   
.. describe:: > asOff

   disables the AS tracking: actuators go to the fixed position set for
   45° of Elevation
   
.. describe:: > asOn

   enables the AS tracking: actuators move according to the pointed Elevation 
   (with a 0.5° step)
   
.. describe:: > asPark

   sends all the actuators to their lowest position

.. describe:: > azelOffsets=[double]d,[double]d

   sets the Az-El offsets (degrees). They are intended “on sky”, i.e. 
   it is the actual offset run on the sky at the source Elevation. 
   
   Example: ``> azelOffsets=-0.05d,0.05d``
   
.. describe:: > calmux=[code]
   
   (``code`` can be ``TOTALPOWER``, ``DBBC``) 
   configures the calibration diode multiplexer 

.. describe:: > calOn

   switches the calibration mark on

.. describe:: > calOff
 
   switches the calibration mark off

.. describe:: > chooseBackend=[string]  

   selects the backend; *string* can be ``BACKENDS/TotalPower`` 

.. describe:: >  chooseRecorder=[string]
  
   selects the backend; *string* can be ``MANAGEMENT/FitsZilla``, 
   ``MANAGEMENT/CalibrationTool`` or ``MANAGEMENT/Point``

.. describe:: > crossScan=[scanFrame],[span],[duration] 

   performs a cross-scan on the previously selected target (indicated using the
   ``track`` or ``sidereal`` commands), along the *scanFrame* (``EQ``, ``HOR`` 
   or ``GAL``), spanning *span* degrees in *duration* seconds 

.. describe:: > device=[sect]
   
   computes the beamsize, taking into account the present receiver and backend
   configurations relative to section sect

.. describe:: > flush=[N]
  
   deletes the N-th element in the queue of temporised commands

.. describe:: > flushAll  
		
   deletes all the queue of the temporised commands


.. describe:: > fTrack=[dev]

   It collects all the required data from the antenna, the back-end and the 
   front-end, plus the information provided by the user (see the 
   ``radialVelocity`` and ``restFrequency`` commands), then it tunes the 
   telescope devices in order to centre the line(s) in each section bandwidth. 
   The command lets the user select which device [dev] is asked to perform the 
   tuning:

   * **LO**: only the front-end local oscillator is moved
 
   * **ALL**: the back-end performs a sub-tuning in the various sections 

 
.. describe:: > getAttenuations
 
   reads the attenuation values (dB) currently configured for the active 
   sections, and lists them according to increasing section number

.. describe:: > getTpi 

   reads the signal intensity (raw counts) for the active sections, and lists 
   them according to increasing section number

.. describe:: > goOff=[frame],[beams] 
		
   slews the antenna to an offset position, wrt a previously commanded target,
   along the longitude axis of the indicated coordinate frame (``EQ``, ``HOR`` 
   or ``GAL``). The user provides the offset value expressed in beamsizes. 
   If the frame is HOR and target lies beyond the Elevation cutoff limits, the 
   offset is applied in Elevation. 

.. describe:: > goTo=[double]d,[double]d

   sends the antenna, while in TRACKING mode, to the specified Az-El position.
   
   Example: ``goTo=180d,45d``
   
   Arguments are always rounded in the range 0-360 and 0-90 for azimuth and 
   elevation respectively (in any case the ranges are limited to mechanical 
   contraints). The jolly character is valid and is considered as: keep the 
   present value. 
   The differences from the ``preset`` command are:

			* once the antenna reaches the destination, the 
			  system will acknowledge the “on source” status;
			* the pointing corrections (pointing model and refraction) 
			  are applied. In case they are not required they must be turned 
			  off explicitly.

.. describe:: > haltSchedule
 
   completes the current scan and then stops the schedule

.. describe:: > ifdist=[int]input,[int]pol,[double]att
 
   set/get the configuration for IF Distributor
	
	``input`` can be:
		* ``1`` to select output on A
		* ``2`` to select output on B
	
	``pol`` can be:
		* ``-1`` to get the current value of pol for selected input
		* ``0`` no input selected
		* ``1`` vertex Right Pol (A input) or ricevitore in vertex Left Pol (B input)
		* ``2`` L Right Pol (A input) L Left Pol (B input)
		* ``3`` X Right Pol (A input) ricevitore X Left Pol (B input)
		* ``4`` S Right Pol (A input) ricevitore S Left Pol (B input)
		* ``5`` spare (A input) S Right Pol (for geo obs.) (B input)
		* ``6`` spare (A input) spare (B input)
		
	``att`` can be:
		* ``-1`` to get the current value of att for selected input
		* a value in the range ``0 - 63``, each step is 0.5 dB
		
.. describe:: > initialize=[code]
   
   (``code`` can be ``CCC``, ``MMC``, ``KKC``, ``QQC``, …) 
   configures the backend using the default parameters relative to the selected
   receiver. It does *not* act on the receiver, pointing model or antenna mount
   mode. 

.. describe:: > integration=[double]

   sets the backend integration time (ms)

.. describe:: > log=[filename]  

   defines a custom name for the logfile (do not specify the extension)

.. describe:: > lonlatOffsets=[double]d,[double]d

   sets the Galactic b-l offsets (degrees). They are intended “on sky”, i.e. 
   it is the actual offset run on the sky at the source latitude.
    
   Example: ``> lonlatOffsets=2.0d,-1.0d``

.. describe:: > moon
 
   points the antenna to the present coordinates of the center of the Moon

.. describe:: > preset=[double]d,[double]d
 
   sends the antenna, if in PRESET mode, to the specified Az-El position, 
   without applying any pointing correction. This is useful when needing to 
   point to a position next to the zenith. Beware: the antenna will reach the 
   destination but no “on source” flag will be raised.
   
   Example: ``> preset=180d,45d``

.. describe:: > project=[code]

   lets the system know which project is observing (the code/name must 
   correspond to the one provided by the TAC). This code/name is then 
   considered as default when launching schedules: the system will search for 
   them in a folder named “project/schedules”. This code/name also forms part 
   of the output FITS filename. Notice that the PROJECT keyword indicated 
   inside the schedule, which is then written in the “Project Name” keyword in 
   the FITS main header, is a free string and might differ from the project 
   official name. 

.. describe:: > radecOffsets=[double]d,[double]d

   sets the RA-Dec offsets (degrees). They are intended “on sky”, i.e. it is 
   the actual offset run on the sky at the source Declination.  
   
   Example: ``> radecOffsets=1.0d,0.0d``

.. describe:: > radialVelocity=[vrad],[vref],[vdef]

    * [vrad] (radial velocity) is in km/sec if vdef is *not* Z
    
    * [vref] (reference frame) can be one of the following:
    
       * **BARY**: Solar System BARYCENTRE
       * **LSRK**: Kinematic Local Standard of Rest
       * **LSRD**: Dynamical Local Standard of Rest
       * **LGRP**: Local Group
       * **GALCEN**: Galactic Centre
       * **TOPOCEN**: TOPOCENTRIC (observer's frame)
       
    * [vdef] (velocity definition) can either be:
    
        * **RD**: Radio Definition
        * **OP**: Optical Definition
        * **Z**: stands for Redshift
 
    The specified velocity parameters are valid until a new target is 
    commanded. The ``radialVelocity`` command overrides any other velocity 
    value that might have been differently expressed 

.. describe:: > receiversMode=[code]
		
   configures the working mode of the receiver, according to its peculiar 
   characteristics

.. describe:: > receiversSetup=[code] 
 
   (``code`` can be ``CCC``, ``MMC``, ``KKC``, ``QQC``, …) 		
   configures the receiver using the default parameters. 
   It does *not* act on the backend, pointing model or antenna mount mode
   
   
.. describe:: > restFrequency=[freq1];...;[freqN]
     
   [freq] is given in MHz and is a multiple argument: it can list a 
   different value for each of the N sections - as long as XARCOS is the 
   backend in use(not all the backends allow this sub-tuning). 
   Specifying a single value assigns the rest frequency to *all* the sections. 
   The specified values will hold until different ones are commanded, or 
   until a new general *setup* command is entered. 
   

.. describe:: > setAttenuation=[sect],[att] 
		
   sets to *att* (dB) the attenuator of section *sect*

.. describe:: > setLO=[freq]

   Local Oscillator frequency, in MHz (one per IF, separated by “;”, 
   usually the values are identical) This LO frequency corresponds to: 
   SkyFreq(@band start) – 100 MHz when using the TPB

.. describe:: > setSection=[sect],[startFreq],[bw],[feed],[mode],[sampleRate],[bins]

   configures the backend section sect.
   
.. describe:: > setupCCC (setupKKC, etc…) 

   unstows the antenna, sets it to tracking mode, selects the pointing model, 
   and configures the receiver and the backend using default parameters. 
   In practice, it is a shortcut corresponding to this sequence:: 

			> antennaSetup=[code]
			> receiversSetup=[receiverCode]
			> initialize=[receiverCode] 
			> device=0 
			> calOff 


.. describe:: > sidereal=[sourcename],[RA],[Dec],[epoch],[sector]
 
   points to the supplied RA-Dec position and temporarily assigns the 
   sourcename label to it. Epoch can be ``1950``, ``2000`` or ``-1``, the last 
   one meaning that the provided coordinates are precessed to the observing 
   epoch. 
   The sector keyword forces the cable wrap sector, if needed: its value can be
   ``CW``, ``CCW`` or ``NEUTRAL``. 
   The last option means the system will automatically choose the optimal 
   alternative.
   
   Example:  ``> sidereal=src12,319.256d,70.864d,2000,neutral``

.. describe:: > skydip=[El1]d,[El2]d,[duration]
 
   performs an OTF acquisition at the current azimuth position, spanning in 
   elevation from *El1* to *El2* (both expressed in degrees, with ‘d’ suffix), 
   in *duration* time, expressed in hh:mm:ss. 
   A recorder must have previously been enabled in order to save the data, and a
   reference position must have been selected via a ``sidereal``, ``track`` or
   ``goTo`` command. 

.. describe:: > startSchedule=[project/][schedulename].scd,[N]
 
   runs schedule *schedulename*.scd (project is the ID of the observing 
   project, it is optional if it has already been input through the 
   ``projectCode`` command), reading it from line *N*  

.. describe:: > stopSchedule 

   immediately stops the running schedule, truncating the acquisition

.. describe:: > ti
  
   lists all the active temporised commands

.. describe:: > track=[sourcename]
 
   points the antenna, in sidereal tracking, to the specified source, which 
   must be present in the local catalogue 

.. describe:: > tsys
 
   measures the system temperature (K) in the position the antenna is pointing 
   to. It returns a list of values, one for each section in use. Intermediate 
   steps and calculations are stored in the active logfile

.. describe:: > wait=[double]
 
   sets a delay (in seconds) which is applied before the system reads/executes 
   the next command
   

.. describe:: > wx  

   returns the current weather parameters: ground temperature (°C), 
   relative humidity (%), atmospheric pressure (hPa), wind speed (km/h).
