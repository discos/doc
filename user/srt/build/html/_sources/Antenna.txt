******************
Antenna operations
******************

Besides the overall telescope setup previously described, individual commands are available to change the antenna mount status and manage its steering/pointing:    	**> antennaReset** 
		resets the antenna status after a failure, for example after the emergency stop button is released	**> antennaUnstow**     		it only performs the unstow procedure   	**> antennaSetup=[code]**    (available codes: LP - for both L and P bands -, CCB, KKG)      		it unstows the antenna (if it is stowed) then it sets the pointing model and 
		the minor servo system according to the selected receiver. Mount is 
		set to ProgramTrack mode   	**> servoSetup=[code]** (available codes: LLP, PLP, PPP, CCB, KKG)     		it sets the minor servo system only, without affecting other systems	**> antennaTrack**
		it sets the mount to ProgramTrack mode, allowing the execution of sidereal 
		tracking, on-off, OTF scans, etc…Even beam-parking acquisitions (i.e. on a 
		fixed Az-El position) can be now performed in ProgramTrack mode by means 
		of the goTo command	**> goTo=[Az]d,[El]d**     		it points the antenna to fixed Az-El positions, yet the mount remains in
		ProgramTrack mode
       			e.g. > goTo=180d,45d	**> track=[sourcename]**		if the antenna is in ProgramTrack mode and the sourcename is known 
		within the station catalogue (which includes the most commonly observed 
		calibrators), it directly points to the source and tracks it			e.g.  > track=3c286	**> sidereal=[sourcename],[RA],[Dec],[epoch],[sector]**		if the antenna mode is ProgramTrack, it points to the supplied RA-Dec 
		position and temporarily assigns the sourcename label to it. Epoch can 
		be ‘1950’, ‘2000’ or ‘-1’, the last one meaning that the provided 
		coordinates are precessed to the observing epoch. The sector keyword 
		forces the cable wrap sector, if needed: its value can be ‘cw’, ‘ccw’ 
		or ‘neutral’. The last option means the system will automatically choose the optimal alternative			e.g.   > sidereal=src12,319.256d,70.864d,2000,neutral

.. note:: **COORDINATE FORMATS** 
   Whenever celestial coordinates (Equatorial, Horizontal or Galactic) are specified, the allowed formats are:   
   *  **decimal degrees**, using a ‘d’ suffix, for any coordinate →  e.g.   30.00d      *  **sexagesimal degrees**, with no suffix, for any coordinate → 30:00:00       *  **hh:mm:ss**, with a ‘h’ suffix, for longitudes only → 02:00:00h  (not accepted for offsets)


Back to the commands:
	**> goOff=[frame],[offset]d**   		it slews the antenna to an offset position, in the indicated coordinate 
		frame (‘eq’, ‘hor’ or ‘gal’). The user provides the offset value (degrees only), 
		but the system automatically chooses on which axis to perform the slewing, 
		taking into account the present position of the antenna			e.g.   > goOff=eq,1.0d     	**> azelOffsets=[azoff]d,[eloff]d** 		it sets user-defined offsets in the Horizontal frame (degrees only).
		The following example sets an azimuth offset to 0.5 degrees and the elevation offset to 0.3 degrees		  	e.g.  > azelOffsets=0.5d,0.3d 
		  		**> radecOffsets=[raoff]d,[decoff]d** 		it sets user-defined offsets in the Equatorial frame (degrees only).
		The following example sets the right ascension offset to 0.3 degrees and the elevation offset to 0.0 degrees			e.g.  > radecOffsets=0.3d,0.0d  					**> lonlatOffsets=[lonoff]d,[latoff]d** 		it sets user-defined offsets in the Galactic frame (degrees only).
		The following example sets the galactic longitude offset to 0.1 degrees and the galactic latitude offset to 0.5 degrees			e.g.  > lonlatOffsets=0.1d,0.5d  .. note:: **OFFSETS**: the above user-defined offsets are the overall antenna offsets 
   and they are mutually exclusive! If the user commands the offsets several times in a row 
   (in one or different frames) only the last one will be effective. **Offsets specified within schedules, 
   at subscan level, sum up to these user-defined offsets.**
			
On with the list:

	**> setServoOffset=[axis_code],[value]**       (→ for technical activities)		The [axis_code] argument must be one of the following codes:			
			* SRP_TX 	# SRP translation along the X axis (mm)			* SRP_TY 	# SRP translation along the Y axis (mm)			* SRP_TZ 	# SRP translation along the Z axis (mm)			* SRP_RX 	# SRP rotation around the X axis (arcsec)			* SRP_RY 	# SRP rotation around the Y axis (arcsec)			* SRP_RZ 	# SRP rotation around the Z axis (arcsec)			* PFP_RY 	# PFP rotation around the Y axis (arcsec)			* PFP_TX 	# PFP translation along the X axis (mm)			* PFP_TZ 	# PFP translation along the Z axis (mm)			* GFR_RZ 	# GFR rotation (mm)			* M3R_RZ 	# M3R rotation (degrees)		
		The [value] argument is a mm value that is assigned to the offset. For instance, in order to set a 5mm offset to the subreflector Z axis:     
			> setServoOffset=SRP_TZ,5	**> antennaStop**		it stops the antenna motion, if any, and changes the mount mode to Stop	**> antennaPark**		it stows the antenna	**> asPark**		it parks the active surface in the reference position for El=45°		**> servoPark**		it stows the minor servo system (notice: after antennaPark, always give this command)	**> telescopePark** 		it parks all the elements: mount (sending the antenna to stow position), minor servo and active surface 