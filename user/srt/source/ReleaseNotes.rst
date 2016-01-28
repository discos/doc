.. _Release-notes:

*************
Release notes
*************

Authors: 

	* Righini, S. (INAF-IRA)
	* and the DISCOS software group


***************************
Current release: what's new
***************************

Nuraghe 0.6 is the present release. 
Here are the new elements it introduces:

  * **New backend**: SARDARA, ROACH-based spectro-polarimeter. SARDARA can now 
    be configured via Nuraghe (see :ref:`sardara`)

  * **L-band receiver tunable LO**: when exploiting the LLP receiver 
    configuration, it is possible to tune the Local Oscillator
    (see :ref:`Frontend-operations`)
    
  * **Wind Park**: an auto-stow procedure activates in the presence of 
    excessively strong wind (see :ref:`Weather-parameters`.)
    
  * **Updates in the spectral FITS content**: addition of the 'SIGNAL' keyword
    in the primary header. The 'DATE' keyword inside the primary header has 
    been replaced by the 'DATE-OBS' one  (see the external PDF linked in
    the :ref:`Retrieving-the-data` section)
    
  * **Generation of schedules**: schedules must now be generated on nuraghe-obs2,
    where a new tool is available; it is called *basie* and it is an evolved
    version of the previous software. It produces schedules also for the XARCOS 
    and SARDARA backends (for spectro-polarimetry observations). OTF and raster
    mapping schedules are designed in order to optimally exploit the multi-feed 
    receiver, including its derotation 
    (see `basie repository <http://github.com/discos/basie/>`_ )
    
  * **FITS Quick-look**: files produced both by the Total Power Backend and 
    XARCOS are now displayed by the IDL tool *fitslook* (notice the underscore
    was removed from its name). It is as usual available on nuraghe-obs2. 
    It automatically adjusts the display features according to the 
    continuum/spectral content of the FITS files 
    (see :ref:`Data-formats-and-online-quick-look`)
    
  * **mySession command**: when using your terminals on nuraghe-obs2, you can
    have all the info about where your data, schedules and logfiles are located
    with the unified *mySession* command (see :ref:`Retrieving-the-data`)



*******
History 
*******

===========  =========== =====================================================
Issue	     Release     What’s  
             Date        new
===========  =========== =====================================================
12           29/01/16    | **Release of NURAGHE 0.6**
                         | Addition of the SARDARA back-end. 
                         | New instructions for LLP LO setup.
                         | Updates in the Startup, Data retrieval and 
                         | Quick-look sections. 
                         | This release is to be paired to the following
                         | documents
                         | * Nuraghe schedule structure (v. 3)
                         | * FITS and MBFITS output formats in Nuraghe (v. 3)
                         | * basie User Manual (v. 1)
-----------  ----------- -----------------------------------------------------
11           25/05/15    | **Release of NURAGHE 0.5**
                         | Addition of Spectroscopy and Derotator sections.
                         | Changes in goOff command. 
                         | New commands for manual data acquisitions. 
                         | Changes in XARCOS configuration codes. 
                         | This release is to be paired to the following
                         | documents
                         | * Nuraghe schedule structure (v. 2)
                         | * FITS and MBFITS output formats in Nuraghe (v. 2)
-----------  ----------- -----------------------------------------------------
10           02/02/15    | Checklist revision. 
                         | Added Troubleshooting and FaultReport sections. 
                         | Removal of previous Appendix C (Schedule
                         | structure), moved to a separate guide.  
                         | “antennaReset” removed from *setupXXX* 
                         | command internal list of actions.   
-----------  ----------- -----------------------------------------------------
09           11/11/14    | **Release of NURAGHE 0.4**  
                         | Addition of XARCOS commands.
                         | Revision of AS and general commands.
                         | Improved codification of commands. 
                         | Addition of TAB-completion of commands.                        
-----------  ----------- -----------------------------------------------------
08           04/04/14    | **Release of NURAGHE 0.3** 
                         | Added commands for AS, MS, setup/park. 
                         | Addedd focusScan command. 
                         | Updated info on Meteo client.
                         | Added info on BCK schedule file.
                         | Deleted sections on data formats and on “Nuraghe 
                         | from Scratch”, which become independent documents.
                         | Checklist moved to document beginning. 
                         | Updates on the operating machines.
-----------  ----------- -----------------------------------------------------
07           03/12/13    | Addition of info on observing machines.
                         | Updates on receviersMode command.
                         | Addition of minor servo commands. 
                         | Addition of “Start Nuraghe from Scratch”
                         | appendix. Addition of clients: “Meteo”,
                         | “Scheduler”, “CalibrationTool”.
-----------  ----------- -----------------------------------------------------
06           10/06/13    | Corrections on receiversMode description.
-----------  ----------- -----------------------------------------------------
05           31/05/13    | Added details on the L/P receiver configurations. 
-----------  ----------- -----------------------------------------------------
04           23/05/13    | Details on login and data access temporarily removed
                         | Correction to the setSection command description. 
                         | Correction and more info on data quick-look
-----------  ----------- -----------------------------------------------------
03           20/05/13    | Added info on user login. 
                         | Added info on quick-look.
                         | Added info on data-retrieval.
                         | Description of OTFC scanning option.
                         | Addition of system calibrator catalogue.  
-----------  ----------- -----------------------------------------------------
02           30/04/13    | Updated info on commands. New formatting.
-----------  ----------- -----------------------------------------------------
01           20/02/13    | Issue 01
===========  =========== =====================================================

