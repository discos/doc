###############################
Contributing to the development
###############################

====================================
Making a change on the master branch
====================================

The **master** branch is our main development branch, we should do our best to keep
it stable and clean but we should never assume that master is a production-stable branch. 
Consider this as the old svn trunk.

Working on the master branch is simple, the only difference with svn is that now 
you work on a local copy of the project, and commits are done on your workstation 
rather than on the server. Once you feel confident of your changes you can push them
on the remote repository stored on github.com so that others can access your changes. 

----------------------------------------
Making a commit in your local repository
----------------------------------------

First we verify that our repository is up-to-date with the remote reposiroty, 
then we edit a file and note how git is aware of the new change.

.. code-block:: bash
  
  $ git status
  On branch master
  Your branch is up-to-date with 'origin/master'.
  nothing to commit, working tree clean
  $ git branch
  * master
  $ echo "DISCOS is in use at three italian radio telescopes" >> README.md
  $ git status
  On branch master
  Your branch is up-to-date with 'origin/master'.
  Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git checkout -- <file>..." to discard changes in working directory)

      modified:   README.md

  no changes added to commit (use "git add" and/or "git commit -a")

Just as SVN, git offers a **diff** command that shows you what changes: 

.. code-block:: bash

   $ git diff
   diff --git a/README.md b/README.md
   index 041992e..f1d6f53 100644
   --- a/README.md
   +++ b/README.md
   @@ -1,3 +1,4 @@
    # DISCOS
     
     Discos is the Development of Italian Single-dish COntrol System
     +DISCOS is in use at three italian radio telescopes

We now add the changes to the next commit operation and create a new commit object
with an associated message: 

.. code-block:: bash 

   $ git add README.md
   $ git status
   On branch master
   Your branch is up-to-date with 'origin/master'.
   Changes to be committed:
     (use "git reset HEAD <file>..." to unstage)

        modified:   README.md

   $ git commit -m "updated README.md for the doc example" 
   [master 4ba4caa] updated README.md for the doc example
    1 file changed, 1 insertion(+)

We can see how git has just created a new *commit* on our local repository. The commit
is uniquely identified by the hashtag starting with *4ba4caa* and is on the branch 
*master*. The commit also has associated a messaged that we specified on the command line.
We could achieve the same result in one single step adding every changeset to the 
commit automatically using the *-a* option, without explicitly adding the files:

.. code-block:: bash
 
   $ git commit -am "updated README.md for the doc example" 

If we look now at the status and the commit tree of our local repo we can see:

.. code-block:: bash

   $ git status
   On branch master
   Your branch is ahead of 'origin/master' by 1 commit.
     (use "git push" to publish your local commits)
   nothing to commit, working tree clean
   $ gittree
   * 4ba4caa (HEAD -> master) updated README.md for the doc example
   * 04fc562 (origin/srt-0.1, origin/noto-0.1, origin/medicina-0.1, origin/master, origin/HEAD) added gitignore and readme

We can see how our newly created commit object is automatically labelled **HEAD** and is positioned one step forward with respect to the remote repository identified by **origin/HEAD** 

-----------------------------------------
Pushing a commit to the remote repository
-----------------------------------------

If we want the remote repo to do this same step we need to *push* the commit object into the remote repository: 

.. code-block:: bash

   $ git push
   Counting objects: 3, done.
   Delta compression using up to 4 threads.
   Compressing objects: 100% (3/3), done.
   Writing objects: 100% (3/3), 385 bytes | 0 bytes/s, done.
   Total 3 (delta 1), reused 0 (delta 0)
   remote: Resolving deltas: 100% (1/1), completed with 1 local object.
   To github.com:discos/discos.git
      04fc562..4ba4caa  master -> master
   $ git status
   On branch master
   Your branch is up-to-date with 'origin/master'.
   nothing to commit, working tree clean
   $ gittree
   * 4ba4caa (HEAD -> master, origin/master, origin/HEAD) updated README.md for the doc example
   ... 

We can see how **HEAD** and **origin/HEAD** are now positioned on the same
commit object. If we look at the repository stored on github.com we would see this same
commit has appeared. 









