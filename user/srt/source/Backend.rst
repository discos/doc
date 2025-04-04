.. _Backend-operations:

******************
Backend operations
******************

The backend to be used can be manually selected as follows:: 

    > chooseBackend=BACKENDS/[bckname]

where *bckname* is the name of the backend. The currently available 
choices are: 
 
	* TotalPower
	* Xarcos      (for the XARCOS spectrometer)
	* Sardara     (for SARDARA, the ROACH-based spectrometer)  


.. _total-power-focus-selector:

Total Power - focus selector
============================

.. warning:: The TotalPower backend works as a **“focus selector”**, sending 
   the signal from the wanted receiver to any other backend. For this reason, 
   it **must** be set up even when acquisitions take place using another 
   backend.  This is accomplished simply using the overall setup commands 
   (such as ``setupCCB``, etc…).

Bandwidth and sampling rate can be changed using:: 

    > setSection=[sect],[startFreq],[bw],[feed],[mode],[sampleRate],[bins]  

where:

	* *[sect]*		is an integer specifying the section number
	* *[startFreq]*	 is the initial frequency for the section (not applicable 
	  for TPB)
	* *[bw]* 		is a double for the bandwidth (MHz)
	* *[feed]* 		is the number of the feed connected to the section 
	  (not applicable for TPB)
	* *[mode]*		is the polarisation mode (not applicable for TPB)	
	* *[sampleRate]*  is also given in MHz
	* *[bins]* 		is the number of frequency bins for the given section 
	  (not applicable for TPB)

To select all sections of the backend, an asterisk can be used instead of
specifying the desired section::

    > setSection=*,*,[bw],*,*,[sampleRate],*

To leave a parameter at its previously set value, or equivalently skip it when 
it is not applicable, use an asterisk. 
For the TPB, in particular, always use::

    > setSection=[sect],*,[bw],*,*,[sampleRate],*

where *bw* can be chosen from a restricted range of options (MHz):

	* 300.0   
	* 730.0   
	* 1250.0   
	* 2000.0 

These values do not correspond to the true observed bandwidth, for the reason 
discussed in Initial Setup. When accumulations of the data “dumps” are required
before integrating them to the output file, it is possible to set the 
integration time as follows::

    > integration=[N] 

where *N* is given in milliseconds. 

Each section is provided with an attenuator, to manage the signal intensity. 
To set the desired attenuation::

    > setAttenuation=[sect],[att] 

where *sect* is the section number and *att* can vary, for the TPB, form 0 dB 
to 15 dB, with a 1 dB step. 

If a backend re-initialization is needed, use::

    > initialize=[code] 
	
(``code`` can be ``CCB``, ``KKG``, etc)

This command resets the backend only, setting it to the default values foreseen
for the specified focus/receiver. 
After the frontend/backend configuration is changed, it is necessary to update 
the value for the beamsize (HPBW), which is computed as a function of the 
actually observed band and is used – during the observations – to evaluate the 
pointing accuracy. This is accomplished using the command::

    > device=[sect]

which uploads to the system the parameters relative to section number [sect] 
(you can generally use 0, which exists for all the receivers, unless you need 
to observe only with a different feed).   


.. _xarcos:

XARCOS
======

This spectrometer is fully integrated in DISCOS, which means that DISCOS can 
command the device, receive data from it and then write these data using a 
standard output (FITS format).

In order to configure the spectrometer, select it with the ``chooseBackend`` 
command and use one of the following commands in the operatorInput: 

.. describe:: > initialize=XK77
 
   This is to use the full K-band MF; each digital sample has a 6-bit 
   representation. Full-Stokes sections are recorded, each having a 62.5 
   MHz bandwidth and 2048(x4) channels 

.. describe:: > initialize=XK03 

   It exploits the K-band feeds 0 and 3. 
   Each feed produces two full-Stokes sections respectively having bandwidths 
   of 62.5 MHz and 4 MHz and 2048(x4) channels. Each digital sample has an 
   8-bit representation.

.. describe:: > initialize=XK06
 
   It enables the K-band feeds 0 and 6. 
   Each feed produces two full-Stokes sections respectively having 
   bandwidths of 62.5 MHz and 4 MHz and 2048(x4) channels. 
   Each digital sample has an 8-bit representation.

.. describe:: > initialize=XK00 

   This configuration is for the usage of the K-band central feed. 
   It produces four full-Stokes sections respectively with bandwidths 
   of 62.5 MHz, 8 MHz, 2 MHz and 0.5 MHz, each having 2048(x4) channels. 
   Each digital sample has an 8-bit representation.

.. describe:: > initialize=XC00
 
   This configuration is C-band usage. 
   It produces four full-Stokes sections respectively with bandwidths 
   of 62.5 MHz, 8 MHz, 2 MHz and 0.5 MHz, each having 2048(x4) channels. 
   Each digital sample has an 8-bit representation.

Ideally, configuration details can be changed using the setSection command:: 

    > setSection=[sect],[startFreq],[bw],[feed],[mode],[sampleRate],[bins]

where:

	* *[sect]*		is an integer specifying the section number
	* *[startFreq]*		is the initial frequency for the section 
	* *[bw]* 		is a double for the bandwidth 
	* *[feed]*	 	is the number of the feed connected to the section 
	* *[mode]*		is the polarisation mode	
	* *[sampleRate]*  	is also given in MHz 
	* *[bins]* 		is the number of frequency bins for the given section

To select all sections of the backend, an asterisk can be used instead of
specifying the desired section::

    > setSection=*,[startFreq],[bw],[feed],[mode],[sampleRate],[bins]

However, the present implementation allows the user to change only part of 
these parameters, in particular: 

	* *[startFreq]* – initial frequency, it must be in the 125-250 MHz range. 
	  This value, added to the LO frequency, gives the lowest sky frequency 
	  observed by the section. Different sections can have different start 
	  frequencies (contrarily to what happens for the TPB); 

	* *[bw]* – bandwidth must be chosen from the following values 
	  (all are expressed in MHz): 125.0, 62.5, 31.25, 15.625, 7.8125, 3.90625, 
	  1.953125, 0.9765625, 0.48828125; 

	* *[sampleRate]* – its value (MHz) must be twice the bandwidth.

Users must not change the feed, mode and bins parameters, which are fixed as 
described in the configuration defaults. 

A valid example of setup and setSection usage, then, is::

    > chooseBackend=BACKENDS/Xarcos
    > initialize=XC00   
    > setSection=0,155.0,31.25,*,*,62.5,*

where asterisks indicate which parameters are to be set according to default 
values. 

.. warning:: At present, integration time is equal to **10 seconds**. 
   Shorter integrations might be available in the future. Data transfer 
   requires about **2 seconds** for each integration; take this overhead into
   consideration when estimating how long your schedules are going to last. 


.. _sardara:

SARDARA
=======
This is a ROACH-based spectrometer, now fully integrated in DISCOS. 
In order to configure it, select it with the chooseBackend command as described
above and use one of the following commands in the operatorInput: 

.. describe:: > initialize=SP00 
   
   This is to use P-band receiver in L/R mode

.. describe:: > initialize=SP00S 
   
   This is to use P-band receiver in full Stokes mode
   
.. describe:: > initialize=SL00 
   
   This is to use L-band receiver in L/R mode

.. describe:: > initialize=SL00S 
   
   This is to use L-band receiver in full Stokes mode

.. describe:: > initialize=SC00 
   
   This is to use C-band receiver in L/R 

.. describe:: > initialize=SC00S 
   
   This is to use C-band receiver in full Stokes mode
   
.. describe:: > initialize=SK00 
   
   This is to use K-band receiver (central feed only) in L/R 

.. describe:: > initialize=SK00S 
   
   This is to use K-band receiver (central feed only) in full Stokes mode

.. describe:: > initialize=SK03 
   
   This is to use K-band receiver (feeds number 0 and 3) in L/R 

.. describe:: > initialize=SK03S 
   
   This is to use K-band receiver (feeds number 0 and 3) in full Stokes mode

.. describe:: > initialize=SK06 
   
   This is to use K-band receiver (feeds number 0 and 6) in L/R 

.. describe:: > initialize=SK06S
   
   This is to use K-band receiver (feeds number 0 and 6) in full Stokes mode

.. describe:: > initialize=SK77 
   
   This is to use K-band receiver (all the 7 feeds) in L/R 

.. describe:: > initialize=SK77S 
   
   This is to use K-band receiver (all the 7 feeds) in full Stokes mode
   
By default, the spectral bin number is set to 1024 and the filter bandwidth 
to 1500 MHz (except for the RP00 configuration, which uses a 500 MHz bandwidth).
The actually observed bandwidth and frequency range are reported in the FITS
files (see the dedicated documentation). 

Users can change the frequency bin number to 16384, using:: 

    > setSection=[sect],*,*,*,*,*,16384

Where *sect* is the section number. 
To select all sections of the backend, an asterisk can be used instead of
specifying the desired section::

    > setSection=*,*,*,*,*,*,16384

Users can also change the integration time::

    > integration=[N] 

where *N* is given in milliseconds.
Attenuations can be handled with the command:: 

    > setAttenuation=[sect],[att] 

where *att* can vary form 0 dB to 15 dB, with a 1 dB step. This attenuation 
is actually applied at the focus selector level. 







 
 

