SunRain Plone Theme
===================

Free Theme for Plone 4 and Plone 3.
    
Features
--------

* SunRain Theme can be presented in two different views: 'Rain' - defined as a default view:

.. figure:: http://quintagroup.com/services/plone-development/skins/images/rain.png/

and 'Sun':

.. figure:: http://quintagroup.com/services/plone-development/skins/images/sun.png/

 To change between 'Sun' and 'Rain' views - go to ZMI -> portal_skins, open 'Properties' tab. In 'Default skin' area 
 change qThemeRain for qThemeSun or vice versa.

 There are 2 directories in portal_skins (ZMI): theme_rain and theme_sun that include logotypes and header images for 
 these views.

* Static Stylish portlet. SunRain theme includes static stylish portlet product that allows to add specially-styled text
  portlets: 'Green Item' and 'Grey Item'. To add them - select 'Static Stylish Portlet' from 'Add portlet...' drop down 
  menu. Provide portlet text into Text area, enable 'Omit portlet border' option, and select 'Green Item' or 'Grey Item' 
  style from 'Portlet style' menu.
  
  Static Stylish portlets include special styling for links (e.g. 'More...' link). To enable it - select a piece of text 
  and set 'Link Item' style for it (Styles drop-down menu on TinyMCE toolbar).

* SunRain theme has 'subscribe' viewlet integrated, that adds two actions 'Send this' and 'RSS'.

* Slogan. SunRain Theme uses customizable slogan. To change portal slogan go to ZMI, open 'Properties' tab and type in
  your new slogan into 'description' field. Save changes.

* Logo. Default logotype dimensions - 188px width and 78px height. There are different logotypes for Sun and Rain theme views.
  In case your new logo height is bigger than the default one - portal-header area will be extended according to your logo 
  height. So, to make theme header look appropriately - customize 'bg-header.jpg' image, i.e. replace it with an image of the
  same height as your logo. If your logo is smaller than the default one - it will be placed in the middle of logotype area.

* Search Box. New approach to site search display is implemented in this theme. In particular, searchSection is hidden during
  common page view. Simply hover the cursor to the search box area and the searchSection appears.

* SunRain Plone Theme changes default Plone look using tableless layout.

* Theme is compatible with Products.LinguaPlone.

SunRain Plone Theme is available at http://pypi.python.org/pypi/quintagroup.theme.sunrain

Supported Plone version
-----------------------
 
This version of SunRain Theme was developed and tested on Plone-4.0 (Python-2.6.4, Zope-2.12.10).

Dependency
----------

* quintagroup.portlet.static

Other products
--------------

The following products were added to previous theme versions. Current version of SunRain Theme does not have these dependencies 
any more. But you can install them to your Plone site (see /docs/INSTALL.txt for insructions):

* quintagroup.portlet.cumulus - adds tag cloud portlet
* Products.Quills or collective.blog.star - add blogs support

Home Directory
--------------

http://skins.quintagroup.com/sunrain

Authors
-------

* Volodymyr Rudnytskyi
* Borys Olekhnovych
* Yuriy Hvozdovych
* Taras Peretiatko

&copy; "Quintagroup": http://quintagroup.com, 2006-2011
