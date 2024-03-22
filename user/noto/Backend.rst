.. _EN_Backend-operations:

******************
Backend operations
******************

The backend to be used can be manually selected as follows:: 

    > chooseBackend=BACKENDS/[bckname]

where *bckname* is the name of the backend. At present, the only available 
choice is: 
 
	* TotalPower



.. _EN_total-power-focus-selector:

Total Power - focus selector
============================

.. warning:: The TotalPower backend works as a **“focus selector”**, sending 
   the signal from the wanted receiver to any other backend. For this reason, 
   it **must** be set up even when acquisitions take place using another 
   backend.  This is accomplished simply using the overall setup commands 
   (such as ``setupCCC``, etc…).

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

where *bw* can be chosen between two options (MHz):

	* 300.0   
	* 730.0 

Larger bandwidths (1250, 2000) are technically possible, but make no sense as 
long as the receivers' IF bandwidth is restricted to 500 MHz.   

Consider that the above-listed bandwidths do not correspond to the true 
observed ones, for the reason discussed in Initial Setup. When accumulations 
of the data “dumps” are required before integrating them to the output file, it 
is possible to set the integration time as follows::

    > integration=[N] 

where *N* is given in milliseconds. 

Each section is provided with an attenuator, to manage the signal intensity. 
To set the desired attenuation::

    > setAttenuation=[sect],[att] 

where *sect* is the section number and *att* can vary, for the TPB, form 0 dB 
to 15 dB, with a 1 dB step. 

If a backend re-initialization is needed, use::

    > initialize=[code] 
	
(``code`` can be ``CCC``, ``MMC``, ``KKC``, ``QQC``)

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


.. _EN_calmux-focus-selector:

Calmux - calibration diode multiplexer
======================================

The Calmux is a multiplexer that allows to choose which backend is entitled to control the
calibration diode on the frontend. This device is required when more than one backend has the
capability to exploit the fast switching. This is the case for DBBC (VLBI) and TotalPower
backends in Noto. When observing with DISCOS, the proper calmux configuration is set
transparently during the setup phase. In case a specific configuration is required, use::

    > calmux=[code] 
	
(``code`` can be ``TOTALPOWER``, ``DBBC``)

.. admonition:: WARNING:  

	* Since then calmux control port is single-client, it is mandatory for DISCOS to properly configure it to make sure that no other clients are connected at the time of the telescope setup.
 
 
 .. _EN_ifdist-if-distributor:

Ifdist - IF Distributor
======================================

The IF Distributors system allows to change the patch of IF, to set attenuation and to retrieve the values of current configuratoion. 
When observing with DISCOS, you can use::

    > ifdist=[input],[pol],[att] 

	
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


