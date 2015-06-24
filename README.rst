SunRain free responsive diazo theme for Plone 5.

Screenshot
------------

.. image:: http://quintagroup.com/services/plone-development/skins/images/sunrain-theme.png/
   :alt: SunRain Plone Theme Screenshot
   :align: center

Installation
------------

Starting from the 7.0 release this theme is adopted for **Plone 5**. If you want to use it with **Plone 4**, please pin theme’s version - **6.x** (according to the latest release before 7.0 - e.g. 6.6)::

  [versions]
  quintagroup.theme.sunrain = 6.6
  
For 6.x version details see https://github.com/quintagroup/quintagroup.theme.sunrain/releases.

Features
--------

**Different views**

In SunRain Theme you can change view from: *Rain* - defined as a default view:

.. figure:: http://quintagroup.com/services/plone-development/skins/images/rain-sunrain.png/

 to *Sun*:

.. figure:: http://quintagroup.com/services/plone-development/skins/images/sun-sunrain.png/

To change between *Sun* and *Rain* views - go to *ploneadmin* menu in the side toolbar, then choose *Site Setup -> Theming*, open *Advanced settings* tab.  In *Parameter expressions* textarea change ``theme = string:rain`` parameter for ``theme = string:sun`` or vice versa.

**Responsive Web Design**

SunRain is a fully responsive theme that allows for easy viewing on mobile devices and tablets. The website will start to automatically resize and reposition the content to accommodate the different device screen sizes. 

**Top image**

SunRain diazo theme has replaceable header image for front and inner site pages. To replace default image, upload image with ``topimage`` shortname into site root or any site section. Recommended image size: 1920*104px.

**Editable Slogan**

SunRain Theme uses customizable slogan. To change it, go to *ploneadmin* menu in the side toolbar, then choose *Site Setup -> Theming*, open *Advanced settings* tab.  In *Parameter expressions* change *Type your slogan here* slogan in *slogan* line.

If you need your slogan to be displayed in non-ASCII characters, go to *Site Setup -> Theming*, open *Advanced settings* tab.  In *Parameter expressions* change the following field  
 
``slogan = string:Type your slogan here`` 

to 

``slogan = python:path('context/slogan|string:').decode('utf-8', 'ignore')``
 
and in *Site Setup -> Zope Management Interface settings -> Properties* tab add a new property *slogan*, type ``string``, value ``your slogan`` and save.

**Customizable Logo**

SunRain diazo Theme comes with default Plone logo.  You can replace it with your own as you would do it in default Plone: go to *ploneadmin* menu in the side toolbar, then choose *Site Setup -> Site -> Site logo*. Upload your image there.

**Social media icons**

Social media icons can be inserted into any place on the page using portlets. Choose Static Text portlet from the “Add portlet..” drop-down menu. Add portlet title, e.g. Find Us On. Change *text/html* editing format to *text/x-web-textile* and add the following code::

  <ul class="social-icons">
   <li class="btn-social"><a class="fa fa-facebook btn-social btn-facebook" href="#"></a></li>
   <li class="btn-social"><a class="fa fa-twitter btn-twitter" href="#"></a></li>
   <li class="btn-social"><a class="fa fa-linkedin btn-linkedin" href="#"></a></li>
   <li class="btn-social"><a class="fa fa-google-plus btn-google-plus" href="#"></a></li>
   <li class="btn-social"><a class="fa fa-pinterest btn-pinterest" href="#"></a></li>
   <li class="btn-social"><a class="fa fa-reddit btn-reddit" href="#"></a></li>
   <li class="btn-social"><a class="fa fa-dropbox btn-dropbox" href="#"></a></li>
   <li class="btn-social"><a class="fa fa-youtube btn-youtube" href="#"></a></li>
  </ul>

Insert your preferred URLs into *href*. Add only those social media icons you need, in any order. You can use ready-made icons from Bootstrap. Go to http://lipis.github.io/bootstrap-social and copy classes of social icons you want to see. 
 
**Editable footer** 

Customize template: *ZMI -> portal_skins -> plone_templates -> footer*. To change colophon "Powered by Plone & Python": go to *ZMI -> portal_skins -> plone_templates -> colophon*. Or you can delete either of them via *More options -> Plone Footerportlets -> footer/colophon*.

Recommended
===========

Theme was tested with:

* Plone 5.0b1

Home Directory
==============

http://themes.quintagroup.com/product/sunrain

Authors
=======

* Roman Ischiv
* Taras Peretiatko
* Volodymyr Rudnytskyy
* Borys Olekhnovych
* Yuriy Hvozdovych

Quintagroup: http://quintagroup.com, 2015.
