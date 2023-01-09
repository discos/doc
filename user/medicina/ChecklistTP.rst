.. _E_Checklist-for-total_power-observations: 

*****************************************************
Checklist for Total Power schedule-based observations
*****************************************************

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
	—> e.g. setLO=23400 - start frequency of the observed band will depend on the backend


**Point the antenna to a reference position** (op)::

	> goTo=[Az]d,[El]d 
	—> e.g. goTo=180d,45d


**Always explicitly choose the Total Power backend (XARCOS might have been left active)** (op)::
	
	> chooseBackend=TotalPower    


**Measure the cold sky signal level** (op)::

	> getTpi 
	> setAttenuation=[sect],[att] 
	—> iteratively adjust attenuations until the level is about 800-1000 counts 


**Get a Tsys** (op)::

	> tsys 


**Pointing check and optimisation, if needed** (op):: 

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
automatically rejected.

**If needed, create a schedule** (2):: 

	Use schedulecreator (see its own guide): 
	$ basie –c [configfile] [out_directory] 

**Parse the schedule** (2):: 

	$ scheduleChecker [schedulename].scd 
	—> Move the schedule files to the observing machine 

**For solar observations ONLY** (op):: 

        > dmed=sun 

This command sets the DIMED attenuators to the high values
that are specific for solar observations. When returning to non-solar
acquisitions, use ``dmed=default``

**Launch the schedule** (op):: 
		
	> startSchedule=[schedulename].scd,[N]

.. admonition:: WARNING:  

    * **The project ID written inside the .scd schedule file MUST coincide
      with the one invoked during the observations (and thus with the project-specific 
      path it is stored into).**

	 
**Data quick-look**
Use the online quick-look provided on the second desktop pf the remote machine. 
	
Notice: if also using MANAGEMENT/CalibrationTool, launch the quick-look (1):: 

	$ calibrationtoolclient MANAGEMENT/CalibrationTool   
          (—> it opens only if the CalibrationTool writer is currently selected!)

**Weather conditions and webcam (in a web browser)**

	Weather: www.med.ira.inaf.it/escs/meteo
	Webcam: www.med.ira.inaf.it/webcam.html 
	
**Stop the schedule** (op)::

	> stopSchedule

**Copy the data** (2) 
	—> Get the latest subfolders written in the main data folder 

**Stow the antenna and restore the default user** (op)::
 
	> antennaPark
	> project=staff


 


