**************************
Spectral line observations
**************************

Spectral line observations can either take place exploiting proper schedules 
(see dedicated documents on how the schedules must be written or how to 
produce them with the *schedulecreator* tool) or by means of command-line 
operations. Here this command-line scenario is described.  

Line rest frequency
===================

The spectral line rest frequency must be provided to the system using the 
following command::

    > restFrequency=[value]
    
[value] is given in MHz and is a multiple argument: it can list a 
different value for each section - as long as XARCOS is the backend in use
(not all the backends allow this sub-tuning). 
Specifying a single value assigns the rest frequency to *all* the sections. 

    e.g. ``> restFrequency=22235.8``  
    
used with the 7-feed K-band receiver implies that all the 14 sections are 
meant to observe the same line. 
Instead, providing different values allows to tune the sections on different 
lines (notice the semicolon used as a separator):

    e.g. ``> restFrequency=22235.8;22235.8;22080.0,22080.0,...,``   

notice that all the N values (these being 14 for the K-band MF) must be 
explicitly provided or errors will rise. 

The specified values will hold until different ones are commanded, or
until a new general *setup* command is entered. 


Target velocity parameters
==========================

When spectral line observations are required, targets must be provided with 
proper indications on their radial velocity, i.e.:

    * **Radial velocity** 
    * **Reference frame**
    * **Definition** 
    
in order for the system to compute, at runtime, the frequency drift due to
the line of-sight doppler contribution. 

Once a target has been defined, for example commanding a ``sidereal`` 
positioning, its velocity can be provided by means of a manual command in the 
operatorInput panel, i.e.:: 

    > radialVelocity=[vrad],[vref],[vdef]

Where

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
 
The wildcard code ``*`` can be provided for all the required arguments and 
will be considered as "keep the present values".

The specified velocity parameters are valid until a new target is commanded. 

.. note:: 
   The ``radialVelocity`` command overrides any other velocity value that 
   might have been differently expressed (e.g. if the target was selected 
   from the source catalogue with the ``track`` command). 



Commanding the doppler computation
==================================

Once the above information have been provided to the system, the computation 
of the line observed frequency can take place. 
Use the command:: 

    > fTrack=[dev]
    
It collects all the required data from the antenna, the back-end and the 
front-end, plus the information provided by the user (see the above 
``radialVelocity`` and ``restFrequency`` commands), then it tunes the 
telescope devices in order to centre the line(s) in each section bandwidth. 
The command lets the user select which device [dev] is asked to perform the 
tuning:

  * **LO**: only the front-end local oscillator is moved
  
  * **ALL**: first of all the front-end local oscillator is tuned, then 
    the back-end - if it allows such a sub-tuning - also performs a further 
    frequency adjustment, in order to centre the line(s) in the various 
    sections. 
    This option is useful in case multiple rest frequencies are 
    to be observed, yet a complete success cannot be guaranteed as the 
    dopplered frequencies  might turn out to be incompatible with the section
    bandwidths and the LO ranges. In case at least one line lies outside the RF 
    band of the receiver or the back-end input bandwidth, an error rises.


Acquiring data
==============
See Command-line --> Manual Acquisitions section. 

