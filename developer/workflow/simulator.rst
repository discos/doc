**************************
Write a hardware simulator
**************************
Hardware Simulator and related tests. The same tests must pass both
for the hardware and the simulator. An important goal is
to test the hardware interface `robustness
<http://en.wikipedia.org/wiki/Robustness_(computer_science)>`_, in order
to simplify the diagnosis of component malfunctions and the DISCOS
maintenance. In that way, if we have to upgrade an hardware firmware or 
an interface, we just have to run the tests to be sure the upgrade does 
not break the system.
