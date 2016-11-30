.. _E_Checklist-for-schedule-based-observations: 

*****************************************
Checklist for schedule-based observations
*****************************************

Notice that actions take place in three different “locations”:

  * **(1)** = action to be performed in a terminal on escsRemote
  * **(2)** = action to be performed in a terminal on escsConsole
  * **(op)** = command to be given in the *operatorInput* panel of ESCS


**Login on both (1) and (2)** 
*Locally*: login on (2) using your projectName, then Using the VNC icon on the 
Desktop, connect to (1) as “observer”.
*Remotely*: connect via VNC to (1) as "observer", then use ssh to access (2). 


**Launch the monitors, if necessary** (1):: 

	$ escsConsole 

**Initial setup** (op)::

	> antennaReset  (if resuming after the emergency stop button is released)  

	> setupCCC      (or other receiver code) 

**Tune the local oscillator, if any** (op)::

	> setLO=[freq] 
	—> e.g. setLO=4900 - start frequency of the observed band will depend on the backend


**Point the antenna to a reference position** (op)::

	> goTo=[Az]d,[El]d 
	—> e.g. goTo=180d,45d


**Always explicitly choose the Total Power backend (XARCOS might have been left active)** (op)::
	
	> chooseBackend=BACKENDS/TotalPower    


**Measure the cold sky signal level** (op)::

	> getTpi 
	> setAttenuation=[sect],[att] 
	—> iteratively adjust attenuations until the level is about 850 counts 


**Get a Tsys** (op)::

	> tsys

**Pointing and focusing optimisation** (op):: 

	> track=name                    (choose a proper calibrator from source catalogue) 
	> chooseRecorder=MANAGEMENT/Point 
	—> the following command on (1): 
		$ calibrationtoolclient MANAGEMENT/Point            (to display the plots) 
	> crossScan=HOR,0.5d,00:00:20   (set proper parameters according to your beamsize) 
	> azelOffsets=0d,0d             (only if wanting to reject the measured offsets!)	
	> focusScan=60,00:01:00 
	> clearServoOffsets             (only if wanting to reject the updated focus position!)
	
.. admonition:: WARNING:  

    * **System offsets, such as the ones measured with a Point acquisition, sum 
      up to the ones indicated inside schedules ONLY if they are expressed in 
      the same coordinate frame.**

This means that, if you perform observations using EQ offsets, also the 
fine-pointing cross-scans must be carried out in the EQ frame. The same
holds for HOR scans. If there is a frame mismatch, the system offsets are
automatically rejected (bug under fixing).

**If needed, choose and set the spectrometer** (op)::
 
	> chooseBackend=BACKENDS/XBackends 
	> initialize=[code]

**Create a schedule** (2):: 

	Use schedulecreator (see its own guide): 
	$ basie –c [configfile] [out_directory] 

**Parse the schedule** (2):: 

	$ scheduleChecker [schedulename].scd 
	—> Move the schedule files to the observing machine 

**Launch the schedule** (op):: 
		
	> startSchedule=[project/][schedulename].scd,[N]
 
**Data quick-look (continuum only)**

	* *Case A\:* when using MANAGEMENT/Fitszilla, launch the quick-look (2)::
 
		$ idl 
		IDL> .r fitslook    
		IDL> fitslook

	* *Case B\:* when using MANAGEMENT/Point, launch the quick-look (2)::
 
		$ calibrationtoolclient MANAGEMENT/Point

	* *Case C\:* when using MANAGEMENT/CalibrationTool, launch the quick-look (1):: 

		$ calibrationtoolclient MANAGEMENT/CalibrationTool
	
**Stop the schedule** (op)::

	> haltSchedule

**Copy the data** (2) 
	—> Get the latest subfolders written in the main data folder 

**Stow the antenna** (op)::
 
	> antennaPark

**Close the monitors, if necessary** (1)::

	$ escsConsole —-stop   (individual panels are closed typing “exit” in their command lines)
 


