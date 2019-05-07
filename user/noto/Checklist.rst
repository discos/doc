.. _EN_Checklist-for-schedule-based-observations: 

*****************************************
Checklist for schedule-based observations
*****************************************

Notice that actions can take place either locally or remotely.

**Login control system(1)** 
*Locally*: login on discos-manager using the discos credentials. 
*Remotely*: connect via VNC to discos-manager with the proper credentials and instructions
provided by local staff. 
**login your user or poject home(2)** you can ssh into discos-manager with proper credentials.


.. note:: Remember that spaces within the command line content are **not** 
   allowed!

**Launch the monitors, if necessary**:: 

	$ discosConsole

**Initial setup** (op)::

	> antennaReset  (if resuming after the emergency stop button is released)  
	> setupCCC      (or other setup code) 

**Tune the local oscillator, if any** (op)::

	> setLO=[freq] 
	—> e.g. setLO=4900 - start frequency of the observed band will depend on the backend


**Point the antenna to a reference position** (op)::

	> goTo=[Az]d,[El]d 
	—> e.g. goTo=180d,45d


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
      the same coordinate frame.** This means that, if you perform observations 
      using EQ offsets, also the fine-pointing cross-scans must be carried out 
      in the EQ frame. The same holds for HOR scans. If there is a frame 
      mismatch, the system offsets are automatically rejected (bug under fixing).

**Create a schedule** (2):: 

	Use basie, the schedule creator (see its own guide): 
	$ basie –c [configfile] [out_directory] 
	—> Move the schedule files to the proper folder

**Parse the schedule** (2):: 

	$ scheduleChecker [schedulename].scd 

**Launch the schedule** (op):: 
		
	> startSchedule=[schedulename].scd,[N]
 
**Data quick-look**

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
	
**Stow the and active surface and minor servo** (op)::

    > asPark
    > servoPark

**Close the monitors, if necessary** (1)::

	$ discosConsole —-stop   (individual panels are closed typing “exit” in their command lines)
 


