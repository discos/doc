.. _Checklist-for-schedule-based-observations: 

*****************************************
Checklist for schedule-based observations
*****************************************

Notice that actions take place in three different “locations”:

  * **(dc)** = action to be performed in a terminal on the observing machine 
    (viewer02), within the VNC connection to *discos-console*
  * **(op)** = command to be given in the *operatorInput* panel of DISCOS


**Login on (dc)** 

**Launch the monitors, if necessary** (dc):: 

	$ discosConsole 

**Initial setup** (op)::

	> antennaReset  (if resuming after the emergency stop button is released)  

	> setupCCB      (or other receiver code) 

	> asSetup=S     (or other AS code)
	
**Project declaration** (op)::

	> project=[projectID]    (to correctly store all your data and more easily retrieve schedules)

**Tune the local oscillator, if any** (op)::

	> setLO=[freq] 
	—> e.g. setLO=6600 - start frequency of the observed band will depend on the backend


**Point the antenna to a reference position** (op)::

	> goTo=[Az]d,[El]d 
	—> e.g. goTo=180d,45d


**Always explicitly choose the Total Power backend (a spectrometer might have been left active)** (op)::
	
	> chooseBackend=BACKENDS/TotalPower    


**Measure the cold sky signal level** (op)::

	> getTpi 
	> setAttenuation=[sect],[att] 
	—> iteratively adjust attenuations until the level is in the 800-1000 count range 


**Get a Tsys** (op)::

	> tsys

**Pointing and focusing optimisation** (op):: 

	> track=name                    (choose a proper calibrator from source catalogue) 
	> chooseRecorder=MANAGEMENT/Point 
	—> the following command on (1): 
		$ calibrationtoolclient MANAGEMENT/Point            (to display the plots) 
	> crossScan=HOR,0.5d,00:00:20   (set proper parameters according to your beamsize) 
	> azelOffsets=0d,0d             (if wanting to reject the measured offsets)	
	> focusScan=60,00:01:00 
	> clearServoOffsets             (if wanting to reject the updated focus position)

.. admonition:: WARNING:  

    * **System offsets, such as the ones measured with a Point acquisition, sum 
      up to the ones indicated inside schedules ONLY if they are expressed in 
      the same coordinate frame.**

This means that, if you perform observations using EQ offsets, also the 
fine-pointing cross-scans must be carried out in the EQ frame. The same
holds for HOR scans. If there is a frame mismatch, the system offsets are
automatically rejected (bug under fixing).

**If needed, choose and set the spectrometer** (op)::
 
	> chooseBackend=XARCOS  (or SARDARA)
	> initialize=[code]

**Create a schedule** (dc):: 

	Use the *basie* schedule creator (read its guide for details): 
	$ basie –c [configfile] [out_directory] 

**Copy all the schedule files** (dc):: 

    Copy the schedule to the destination folder on discos-console.

    
**Parse the schedule** (dc):: 

	$ scheduleChecker [schedulename].scd 


**Launch the schedule** (op):: 
		
	> startSchedule=[project/][schedulename].scd,[N]

**Data quick-look** (dc)::

        Launch the real-time quick-look of the data under acquisition
        by double-clicking on the quicklook.html icon on the desktop 
		
**Stop the schedule** (op)::

	> stopSchedule

**Copy the data** (dc) 
	—> Get the latest subfolders written in the main data folder 

**Stow the antenna** (op)::
 
	> telescopePark
 


