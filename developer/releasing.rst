*******************
Releasing procedure
*******************
Nuraghe uses a *major.minor.patch* nomenclature, so Nuraghe-1.5.2
has a *major version* of 1, a minor version of 5, and a *patch version* of 2.
The *major version* zero (0.y.z) is for initial development, when anything 
may change at any time, so the public API, the *operator input* commands
and the schedule *grammar* should not be considered stable. 

.. _final:

Production-ready releases
=========================
This section describes the semantic used to assign the
version number to the production-ready releases, that is 
the releases the astronomers use during their normal
observations.

New major versions
------------------
New *major versions* are exceptional, because
they only come when strongly incompatible changes are 
deemed necessary, and are planned very long in advance.

That means if an astronomer *schedule* can be executed
using *Nuraghe-1.x.y*, then it will also be executed using any of the
next releases of Nuraghe with major version of 1.


New minor versions
------------------
New *minor versions* are feature releases, so they add
functionality in a backwards-compatible manner.

New patch versions
------------------
New *patch versions* are bugfix releases that
make backwards-compatible bug fixes

In-development versions
=======================
We also have *non*-production ready versions which get an additional qualifier:
*beta* and *release candidate* (RC).  The beta versions
are aimed at testing by advanced users, not production use, while the RC is
aimed at testing by a group of astronomers, as described in section :ref:`rc`.

.. _beta:

Beta
----
In this stage no more features are accepted. Only
bug fixes can now be committed. This is when core developers should concentrate
on the task of fixing regressions and other new issues. 
The new user's manual must be released before the end of this stage.

.. _rc:

Release Candidate
-----------------
A *release candidate* (RC) must be tested by a group of astronomers, called
RC testers. They should interact whit the core developers in order to report 
the malfunctions.

.. todo:: We must indicate how to report the malfunctions.

This release can only have bugfixes applied that have
been reviewed by other core developers, and can become a final-release
only after the RC testers give their approval.

After the final-release is published, the full
*development cycle* starts again for the next minor version.
Only the :ref:`project-manager` can approve new changes to the 
final releases.


