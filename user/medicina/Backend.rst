.. _E_Backend-operations:

******************
Backend operations
******************

The backend to be used can be manually selected as follows:: 

    > chooseBackend=[bckname]

where *bckname* is the name of the backend. At present, the available 
choices are: 
 
	* TotalPower
	* Sardara
	* XArcos   



.. _E_total-power-focus-selector:

Total Power - focus selector
============================

.. warning:: The TotalPower backend works as a **“focus selector”**, sending 
   the signal from the wanted receiver to any other backend. For this reason, 
   it **must** be set up even when acquisitions take place using another 
   backend.  This is accomplished simply using the overall setup commands 
   (such as ``setupKKC``, etc…).

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

To leave a parameter at its previously set value, or equivalently skip it when 
it is not applicable, use an asterisk. 
For the TPB, in particular, always use::

    > setSection=[sect],*,[bw],*,*,[sampleRate],*

where *bw* can be chosen from a restricted range of options (MHz):

	* 300.0   
	* 730.0   
	* 1250.0   
	* 2000.0 

Notice: not all the receivers have RF bands large enough to employ the wide-band
filters. In particular, only the KKC receiver can be used with the 1250 and 2000 MHz 
filters. 

The nominal *bw* values do not correspond to the true observed bandwidth, for the reason 
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
	
(``code`` can be ``CCC``, ``XXP``, etc)

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



SARDARA
=======

This is a spectroscopic-polarimeter, at present offered in SHARED RISK. 
In order to configure it, select it with the ``chooseBackend`` 
command 

    > chooseBackend=Sardara

and use one of the following commands in operatorInput: 


.. describe:: > initialize=SCC00 

   This configuration is for the usage of the Clow-band receiver, 
   in spectral mode only (LCP and RCP spectra). 

.. describe:: > initialize=SCC00S 

   This configuration is for the usage of the Clow-band receiver, 
   in full-Stokes mode (LCP and RCP spectra and Stokes parameters). 

.. describe:: > initialize=SCH00 

   This configuration is for the usage of the Chigh-band receiver, 
   in spectral mode only (total intensity spectra). 

.. describe:: > initialize=SCH00S 

   This configuration is for the usage of the Chigh-band receiver, 
   in full-Stokes mode (LCP and RCP spectraand Stokes parameters). 

.. describe:: > initialize=SK00 

   This configuration is for the usage of the K-band reference feed, 
   in spectral mode only (total intensity spectra). 

.. describe:: > initialize=SK00S 

   This configuration is for the usage of the K-band reference feed, 
   in full-Stokes mode (LCP and RCP spectra and Stokes parameters). 


Ideally, configuration details can be changed using the ``setSection`` command:: 

    > setSection=[sect],[startFreq],[bw],[feed],[mode],[sampleRate],[bins]

where:

	* *[sect]*		is an integer specifying the section number
	* *[startFreq]*		is the initial frequency for the section 
	* *[bw]* 		is a double for the bandwidth 
	* *[feed]*	 	is the number of the feed connected to the section 
	* *[mode]*		is the polarisation mode	
	* *[sampleRate]*  	is also given in MHz 
	* *[bins]* 		is the number of frequency bins for the given section

However, the present implementation allows the user to change only part of 
these parameters, in particular: 

	* *[bw]* – bandwidth must be chosen from the following values 
	  (all are expressed in MHz): 420 or 1500.  

	* *[sampleRate]* – it must amount to twice the bandwidth (i.e. 840 or 3000). 

	* *[bins]* – its value can be either 1024 or 16384.

.. warning:: When using a full-Stokes setup, only section 0 is to be configured. 
   Instead, when using spectral-only setups, both Sections 0 and 1 must be configured. 

Valid examples of setup and ``setSection`` usage, then, are::

    > chooseBackend=Sardara
    > initialize=SK00   
    > setSection=0,*,1500,*,*,3000,16384
    > setSection=1,*,1500,*,*,3000,16384

    > chooseBackend=Sardara
    > initialize=SK00S   
    > setSection=0,*,420,*,*,840,1024

where asterisks indicate which parameters are to be set according to default 
values. 

.. warning:: Observations with this back-end still pose issues with the 
   activation of the calibration mark. System temperature measurements might not be
   carried out correctly, so it is best to avoid them in schedules. 



XARCOS
======

This spectrometer is fully integrated in DISCOS, which means that DISCOS can 
command the device, receive data from it and then write these data using a 
standard output (FITS format).

In order to configure the spectrometer, select it with the ``chooseBackend`` 
command and use one of the following commands in operatorInput: 

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

Ideally, configuration details can be changed using the ``setSection`` command:: 

    > setSection=[sect],[startFreq],[bw],[feed],[mode],[sampleRate],[bins]

where:

	* *[sect]*		is an integer specifying the section number
	* *[startFreq]*		is the initial frequency for the section 
	* *[bw]* 		is a double for the bandwidth 
	* *[feed]*	 	is the number of the feed connected to the section 
	* *[mode]*		is the polarisation mode	
	* *[sampleRate]*  	is also given in MHz 
	* *[bins]* 		is the number of frequency bins for the given section

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

A valid example of setup and ``setSection`` usage, then, is::

    > chooseBackend=XArcos
    > initialize=XC00   
    > setSection=0,155.0,31.25,*,*,62.5,*

where asterisks indicate which parameters are to be set according to default 
values. 

.. warning:: Integration time is equal to **10 seconds**. 
   Data transfer requires about **2 seconds** for each integration, thus take 
   this overhead into consideration when estimating how long your schedules 
   are going to last. 



