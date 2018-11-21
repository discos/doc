#####################
GitHub based workflow
#####################

.. contents::

================================================
Remarks on working with DISCOS GitHub repository 
================================================

All the submissions, including submissions by project members, require a review by a member of the core team.
We use GitHub pull requests for this purpose. 
Any feature, enhancement or bug must be submitted to GitHub tracking system before starting any further elaboration.
All subsequent changes are done on dedicated branches that clearly reference the issue number. 
DISCOS settle on two persistent branches, the *master* branch dedicated to development and the *stable* branch
in which the releases are maintained. 

==================
Hot-Fixes workflow
==================

* Check out into master branch: *git checkout master*
* Fetch all remote updates: *git remote update*
* Update local master branch with remote copy: *git pull origin master*
* Check out into stable branch: *git checkout stable*
* Update local stable branch with remote copy: *git pull origin stable*
* Create a hotfix branch related to the issue xxx: *git checkout -b fix-issue-xxx*
* Do some fixes and commit to them
* Push the hotfix branch to remote repository: *git push origin fix-issue-xxx*
* Open a "Pull request" in GitHub, in order to merge the hotfix branch onto the stable branch, and reqeust a review from the team
* Once the team approves the pull request, the branch can be merged using the "Squash and merge" strategy, be sure to not delete the hotfix branch
* Open a second "Pull request" in GitHub, in order to merge the hotfix branch onto the master branch
* Once again, once the team approves the pull request, the branch can be merged using the "Squash and merge" strategy, this time the branch can be deleted
* If some conflict between the master and the hotfix branch arises, don't worry, they can be fixed right away when merging online. Resolve the conflict by porting the new lines from the hotfix branch into the master branch version of the file.
* Finally, delete the hotfix branch from the local repository: *git branch -D fix-issue-xxx*
* Now that the hotfix is on the online repository, a new tag can be created onto the stable branch. In order to do this, go to the releases page of the repository, and select "Draft a new release". Fill the "Tag version" and "Release title" fields according to the previous releases. Also, be sure to select the stable branch as target and to check "This is a pre-release" if you are not sure if your release is ready to be deployed on production line.

===============================
Feature implementation workflow
===============================

* Check out into master branch: *git checkout master*
* Fetch all remote updates: *git remote update*
* Update local master branch with remote copy: *git pull origin master*
* Create a branch related to the issue xxx: *git checkout -b fix-issue-xxx*
* Do some coding and commit to it: *git commit -m "Fix #xxx:…"*
* Push feature branch to remote repository: *git push origin fix-issue-xxx*
* Open a "Pull request" in GitHub for team to verify the feature
* Once the team approves the pull request, the branch can be merged using the "Squash and merge" strategy, and it can be deleted from the online repository
* Finally, delete the feature branch from the local repository: *git branch -D fix-issue-xxx*