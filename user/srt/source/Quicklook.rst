**********************************
Data formats and online quick-look
**********************************

Waiting for a comprehensive GUI which is going to include also a real-time preview of the data under acquisition, users are provided with two different tools in order to inspect the data produced by the TPB. 

If writer is MANAGEMENT/FitsZilla
=================================
When acquiring FITS files through a schedule, there is an IDL tool available for the semi-realtime quick-look of the saved data.
 
Open a terminal on *nuraghe-obs2*. Launch IDL::	$ idl	At the IDL prompt, compile and run the program fits_look.pro:: 	IDL> .r fits_look	IDL> fits_lookThe last available FITS file will be plotted. Full usage::	IDL> fits_look [,pin=] [,x=] [,y=] [,/help]where: 	* **pin** = full path to data storage folder (the one containing the scan subfolders) 	* **x** = letter indicating the choice for the x-axis label, default is 's' 	* **y** = choice of the data stream, default is 'raw', displaying raw counts, 
          while using 'atemp' the antenna temperature - *if available* - is shown.The procedure iteratively lists all the folders in the given path (pin) and displays on screen the Feed0L and Feed0R data of the last surely complete FITS file recorded in the last written folder. If pin is not provided, the path to the data is **by default** to the folder where data is currently being written. The x-axis can be represented as: 
|	sample number (if x='s'), |	elapsed time from the acquisition start (if x='t'), |	scanning axis (if x='x'),|	azimuth degrees (if x='a'), |	elevation degrees (if x='e'), |	declination degrees (if x='d'), |	right ascension hh.hhh (if x='r').Default is SAMPLE NUMBER.In order to display all the sections of a **multi-feed receiver**, use the specific procedure:: 	IDL> .r fits_look_mf	IDL> fits_look_mfPlease report any problem/request about these tools, as they are very basic and still under development... note:: The antenna temperature data streams are available only if a Tsys has been correctly acquired prior to the execution of the scan. See the FITS-related document for details.


If writer is MANAGEMENT/Point or MANAGEMENT/CalibrationTool
===========================================================

When data are acquired – both manually or through a schedule – using the Point or CalibrationTool writers, the quick-look must be performed using the CalibrationToolClient. Open a terminal on nuraghe-obs1 and use the command:: $ calibrationtoolclient [componentName]where componentName is either MANAGEMENT/Point or MANAGEMENT/CalibrationTool. A graphic window will appear. Its content is given in the following figure. 

.. figure:: images/CalToolClient.png
   :scale: 80%
   :alt: calibrationtoolclient 
   :align: center

.. note:: In this client, the subscan currently being acquired is shown *in real-time* (upper plot), even if in a low-res version. Under this display, the last completed subscan - in its full sampling - is shown. 