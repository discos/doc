.. _E_Checklist-for-spectral-observations_SARDARA: 

******************************************************
Checklist for schedule-based observations with SARDARA
******************************************************

Notice that actions take place in three different “locations”:

  * **(1)** = action to be performed in a terminal on the observing machine (the one with the DISCOS system interface)
  * **(2)** = action to be performed in a terminal on the project/schedule/data machine
  * **(op)** = command to be given in the *operatorInput* panel of DISCOS


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
 
	> chooseBackend=Sardara 
	> initialize=[code]      (e.g. SCC00, SCC00S, SK00, SK00S)

**If non-default parameters are needed, configure the sections** (op)::

	> setSection=[sect],[startFreq],[bw],[feed],[mode],[sampleRate],[bins]

Remember: for full-Stokes setups, only section 0 is to be configured. 
For spectral-only setups, both sections 0 and 1 must be configured. 

**Measure RMS in order to verify the signal level** (op)::

	> getRms

Values should be included in the 20-22 range. If they are not, adjust the attenuation
levels as follows and repeat the RMS measurement.

**If needed, set the attenuators** (op):: 

        > setAttenuation=[sect],[att]   

Each attenuator can be set from 0 dB to 15 dB, with a 1-dB step.

**If needed, create a schedule** (2):: 

	Use schedulecreator (see its own guide): 
	$ basie –c [configfile] [out_directory] 

**Parse the schedule** (2):: 

	$ scheduleChecker [schedulename].scd 
	—> Move the schedule files to the observing machine 

**Launch the schedule** (op):: 
		
	> startSchedule=[schedulename].scd,[N]

.. admonition:: WARNING:  

    * **The project ID written inside the .scd schedule file MUST coincide
      with the one invoked during the observations (and thus with the project-specific 
      path it is stored into).**

 
**Data quick-look** 

 Use the online quick-look provided on the second desktop of the remote machine.  

**Weather conditions and webcam (in a web browser)**

	Weather: www.med.ira.inaf.it/escs/meteo
	Webcam: www.med.ira.inaf.it/webcam.html 
	
**Stop the schedule** (op)::

	> haltSchedule

**Copy the data** (2) 
	—> Get the latest subfolders written in the main data folder 

**Stow the antenna and restore default user** (op)::
 
	> antennaPark
	> project=staff
         


 


