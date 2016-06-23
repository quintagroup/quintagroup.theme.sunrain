Installation
------------

Here are detailed instructions on installation of the quintagroup.theme.sunrain package.

Versions
========

Note that there are differences in installation of Sunrain responsive theme for Plone 4 and 5. You will need to use specific theme versions for different Plone releases: 

* 6.x - for Plone 4
* 7.x - for Plone 5

For 6.x version details see https://github.com/quintagroup/quintagroup.theme.sunrain/releases and *docs/HISTORY.txt*.

Installation via buildout
=========================

In the buildout.cfg file of your instance:

* Add ``quintagroup.theme.sunrain`` to the list of eggs to install, e.g.::

    [buildout]
    ...
    eggs =
       ...
       quintagroup.theme.sunrain

* The newest releases are suitable for **Plone 5**. If you want to use Sunrain theme with **Plone 4**, please pin theme’s version - **6.x** (according to the latest release before 7.0 - e.g. 6.8.1)::

    [versions]
    quintagroup.theme.sunrain = 6.8.1
       
* Re-run buildout::

    $ ./bin/buildout

* Restart the Zope server::

    $ ./bin/instance restart

Then activate 'Sunrain Theme' in Plone (Site Setup -> Add-ons).      
       

Installation: development mode
==============================

If you want to customize Sunrain theme please use the following installation instructions: 

* download ``quintagroup.theme.sunrain-version.zip`` archive from http://pypi.python.org/pypi/quintagroup.theme.sunrain
* extract theme archive to get ``quintagroup.theme.sunrain-version`` folder. Remove version from 
  folder name to have ``quintagroup.theme.sunrain`` folder
* put ``quintagroup.theme.sunrain`` folder into ``src`` directory of your buildout
* in buildout.cfg file of your buildout add ``quintagroup.theme.sunrain`` to the list of eggs you are developing and  to the list of eggs to install::

       [buildout]
       ...
       develop = src/quintagroup.theme.sunrain
       ...
       eggs =
           ...
           quintagroup.theme.sunrain
   
* Re-run buildout::

    $ ./bin/buildout

* Start instance in development mode::

    $ ./bin/instance fg

* Install ``Sunrain Theme`` in Plone (Site Setup -> Add-ons).

Now you can customize Sunrain Theme by modifying ``quintagroup.theme.sunrain`` package in ``src`` directory of your buildout.
