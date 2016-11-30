.. _EN_Appendix-C-output-files: 

*************************
Appendix C - Output files
*************************

The system at present allows the user to write the output data, coming from the 
integrated backends, in two different formats: FITS and MBFITS. 
The former is a substantially **standard FITS**, carrying the data and a load 
of ancillary information inside several extensions. A FITS is produced for 
every subscan composing the observation.

**MBFITS** is a more complex format, not yet fully implemented and whose 
writer component is still under testing. Each MBFITS contains the 
whole scan, and subscans are hierarchically organized inside its structure.

**Details on both formats are provided in this separate manual** 
:download:`pdf <attachments/MED-MAN-FITS-02.pdf>` 
