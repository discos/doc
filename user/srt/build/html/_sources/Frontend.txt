*******************
Frontend operations
*******************


General rules
=============

To change the frontend Local Oscillator frequency, use the following command:: 	> setLO=[freq1];[freq2];…;[freqN]Notice the semicolon. Ideally, different values could be assigned to different IFs, thus tuning each section to a different sub-band. For the present hardware, though, this is not possible, so a single value must be specified: 
	e.g.  > setLO=5600 Remember that the actually observed band begins at a frequency which is usually different from the LO one (see Initial setup)The L-P band receiver is not provided with a tunable Local Oscillator, and the observed band is fixed. Filters are available in order to set the observed sub-band and select the polarisation (circular or linear), specifying a code with the command::
 		> receiversMode=[code]  see the next section for the details. The temperature of the calibration mark in use is recorded in the logfile whenever a Tsys is measured. It is also stored in the FITS/MBFITS output files. The calibration mark can be manually switched on and off respectively with:: 	> calOn 	> calOffIf the user wants to perform the setup for the frontend only (without affecting the mount, the minor servo or the backend), the command is:: 	> receiversSetup=[code]   (PPP, LLP, PLP, CCB, KKG) 


Specific notes for the L/P receiver
===================================

The L/P receiver is actually seen by Nuraghe as a group of three different receivers, each having its own setup code:   	* **PPP** 	for the usage of the P band only  	* **LLP** 	for the usage of the L band only  	* **PLP** 	for the dual-feed usageThese are the codes to be used in the *setupXXX* command.Then the configuration of the band filter and of the polarisation mode must be performed, by means of the *receiversMode* command. Here follows the list of options. 

PPP
---

Only the P band can be used. The possible configurations are:: 	> receiversMode=C1XX	> receiversMode=C2XX	> receiversMode=C3XX   (default)	> receiversMode=L1XX	> receiversMode=L2XX	> receiversMode=L3XXThe first two characters in the code identify the polarisation mode (C = Circular, L = linear) and the band filter index, where:	1. all band, 305-410 MHz (no filter)	2. 310-350 MHz		3. 305-410 MHz (band-pass filter)The **XX chars are placeholders** for the L-band configuration, which is not allowed in PPP mode. 

LLP
---

Only the L band can be used. The possible configurations are:: 	> receiversMode=XXC1	> receiversMode=XXC2	> receiversMode=XXC3	> receiversMode=XXC4  (default)	> receiversMode=XXC5	> receiversMode=XXL1	> receiversMode=XXL2	> receiversMode=XXL3	> receiversMode=XXL4	> receiversMode=XXL5The last two characters in the code identify the polarisation mode (C = Circular, L = linear) and the band filter index, where:	1. all band, 1300-1800 MHz (no filter)	2. 1320-1780 MHz	3. 1350-1450 MHz (VLBI)	4. 1300-1800 MHz (band-pass)	5. 1625-1715 MHz (VLBI)The **XX chars are placeholders** for the P-band configuration, which is not allowed in LLL mode. 

PLP (dual band)
--------------- 

In this setup, both bands are used and can be configured, according to the following scheme, based on the permutation of all the previously described codes:: 	> receiversMode=C1C1 	> receiversMode=C2C1	> receiversMode=C3C1	> receiversMode=C1C2 	...	> receiversMode=C3C4  (default) 	> receiversMode=C3C5 	...	> receiversMode=L1C1	...	> receiversMode=C1L1	...	> receiversMode=L1L1	...
