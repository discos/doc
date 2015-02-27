****************
How to fix a bug
****************
Once we have confirmed the existence of a bug, we do not never start 
fixing it until we have reproduced that bug in a unit test. 
So, if we want to fix a bug, we have to:

    * work in the nuraghe-x-dev environment
    * write a small, simple and fast test that reproduces the bug
    * ensure the test breaks
    * fix the code
    * run the test to confirm it now passes
    * run all the regression tests to confirm that the changes does not
      brake something else
    * leave the test in the *test* directory (forever) in order
      to ensure that the bag does not reoccur
    * commit the changes
    * update the changes in production
    * run all the tests in production

This is the only way to ensure the DISCOS stability and 
robustness, and you will soon realize the TDD is not at all 
a lose of time.

