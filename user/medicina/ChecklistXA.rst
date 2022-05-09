.. _E_Checklist-for-spectral-observations: 

**************************************************
Checklist for spectral schedule-based observations
**************************************************

Notice that actions take place in three different “locations”:

  * **(1)** = action to be performed in a terminal on the observing machine (the one with the DISCOS system interface)
  * **(2)** = action to be performed in a terminal on the project/schedule/data machine
  * **(op)** = command to be given in the *operatorInput* panel of ESCS


**Login on both (1) and (2)** 
Connect via VNC to (1) as "observer", from there use ssh to access (2) with your project-specific account. 


**Launch the monitors, if necessary** (1):: 

	$ discosConsole 

**Set the project name** (op)::

	> project=[projectID]  

**Initial setup** (op):: 

	> setupKKC      (or other receiver code: CCC, XXP) 

**Tune the local oscillator, if any** (op)::

	> setLO=[freq] 
	—> e.g. setLO=22000 - start frequency of the observed band will depend on the backend


**Point the antenna to a reference position** (op)::

	> goTo=[Az]d,[El]d 
	—> e.g. goTo=180d,45d


**Always explicitly choose the Total Power backend (XARCOS might have been left active)** (op)::
	
	> chooseBackend=TotalPower    


**Measure the cold sky signal level** (op)::

	> getTpi 
	> setAttenuation=[sect],[att]  (values range from 0 dB to 15 dB, 1-dB step)
	—> iteratively adjust attenuations until the level is about 700-900 counts 


**Get a Tsys** (op)::

	> tsys

**Pointing check** (op):: 

	> track=name                    (choose a proper calibrator from source catalogue) 
	> chooseRecorder=MANAGEMENT/CalibrationTool 
	—> the following command on (1): 
		$ calibrationtoolclient  (to display the plots) 
	> crossScan=HOR,0.2d,00:00:15    (set proper parameters according to your beamsize) 
	> azelOffsets=0d,0d              (only if wanting to reject the measured offsets!)	
		
.. admonition:: WARNING:  

    * **System offsets, such as the ones measured with a Point acquisition, sum 
      up to the ones indicated inside schedules ONLY if they are expressed in 
      the same coordinate frame.**

This means that, if you perform observations using EQ offsets, also the 
fine-pointing cross-scans must be carried out in the EQ frame. The same
holds for HOR scans. If there is a frame mismatch, the system offsets are
automatically rejected (bug under fixing).

**Choose and set the spectrometer** (op)::
 
	> chooseBackend=XArcos 
	> initialize=[code]      (either XC00 or XK00)

**If needed, set the spectrometer attenuators** 
        > setAttenuation=[sect],[att]     
          (values around 19-21 dB have proven to be OK to avoid saturation, but it depends on the signal level)

**If needed, create a schedule** (2):: 

	Use schedulecreator (see its own guide): 
	$ basie –c [configfile] [out_directory] 

**Parse the schedule** (2):: 

	$ scheduleChecker [schedulename].scd 
	—> Move the schedule files to the observing machine 

**Launch the schedule** (op):: 
		
	> startSchedule=[schedulename].scd,[N]

If you haven't previously specified the project ID using the ``project`` command,
you need to insert it in the schedule path:: 

	> startSchedule=[projectID]/[schedulename].scd,[N]

.. admonition:: WARNING:  

    * **The project ID written inside the .scd schedule file MUST coincide
      with the one invoked during the observations (and thus with the project-specific 
      path it is stored into).**

 
**Data quick-look**

	* *Case A\:* when using MANAGEMENT/Fitszilla, launch the raw-FITS quick-look (2)::
 
		$ idl 
		IDL> .r fitslook    
		IDL> fitslook
		
		or (to inspect complete (ON-OFF)/OFF spectral acquisitions)
		
		$ idl 
		IDL> .r onoff    
		IDL> onoff, dutyc='N_on:N_off:N_cal'   
		(where N_on, N_off, N_cal are integer numbers - may assume zero value) 


	* *Case B\:* when using MANAGEMENT/CalibrationTool, launch the quick-look (1):: 

		$ calibrationtoolclient MANAGEMENT/CalibrationTool
                  (—> it opens only if the CalibrationTool writer is currently selected!)

**Weather conditions and webcam (in a web browser)**

	Weather: www.med.ira.inaf.it/escs/meteo
        Webcam: www.med.ira.inaf.it/webcam.html 
	
**Stop the schedule** (op)::

	> haltSchedule

**Copy the data** (2) 
	—> Get the latest subfolders written in the main data folder 

**Stow the antenna** (op)::
 
	> antennaPark


 


