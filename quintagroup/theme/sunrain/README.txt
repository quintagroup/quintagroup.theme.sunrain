SunRain free diazo theme for Plone 4.
    
Features
--------

* SunRain Theme can be presented in two different views: 'Rain' - defined as a default view:

 .. figure:: http://quintagroup.com/services/plone-development/skins/images/rain.png/

 and 'Sun':

 .. figure:: http://quintagroup.com/services/plone-development/skins/images/sun.png/

 To change between 'Sun' and 'Rain' views - go to 'Site Setup' -> 'Diazo theme' settings, open 'Advanced settings' tab.
 In 'Parameter expressions' field change ``theme = string:rain`` for ``theme = string:sun`` or vice versa.

* SunRain theme has 'subscribe' viewlet integrated, that adds 4 actions 'Share on Twitter', 'Share on Facebook', 'Send this'
  and 'Subscribe to RSS'. Their links can be edited via ZMI portal_actions -> subscribe. 
  
  Icons can be edited via file system at /src/quintagroup.theme.sunrain/quintagroup/theme/sunrain/static/images folder: 
  replace twitter.png, facebook.png, rss.png and email.png icons with new ones. Restart instance.

* Slogan. SunRain Theme uses customizable slogan. To change portal slogan go to ZMI, open 'Properties' tab and type in
  your new slogan into 'description' field.

* Logo. SunRain diazo Theme uses default Plone 4 logo. To replace it - in ZMI customize portal_skins -> sunburst_images -> logo.png image.

* Search Box. New approach to site search display is implemented in this theme: searchSection is hidden during common page 
  view. Simply hover the cursor to the search box area and the searchSection appears.

* Improved thumbnail display view (switch to Thumbnail view)

**Additional Features**

Features, that require additional packages installation:

* quintagroup.portlet.static. When activated, SunRain theme will have specially-styled text  portlets: 'Green Item' and 
  'Grey Item'. To add them - select 'Static Stylish Portlet' from 'Add portlet...' drop down  menu. Provide portlet text 
  into Text area, enable 'Omit portlet border' option, and select 'Green Item' or 'Grey Item' style from 'Portlet style' menu.
  
  Static Stylish portlets include special styling for links (e.g. 'More...' link). To enable it - select a piece of text 
  and set 'Link Item' style for it (Styles drop-down menu on TinyMCE toolbar).

* blogging support require either Products.Quills or blog.star product installation.

Dependencies
============

* plone.app.theming
* plone.app.themingplugins

Recommended
===========

SuinRain diazo theme was tested with:

* Plone 4.1
* plone.app.theming 1.0b8 
* plone.app.themingplugins 1.0b1
* Products.Carousel 2.1
* Products.ContentWellPortlets 4.0

Besides, special styles were added to the theme for correct theme display with the following products activated:

* quintagroup.dropdownmenu 1.2.5
* Products.LinguaPlone 4.0.4
* quintagroup.portlet.cumulus 1.1.0
* quintagroup.portlet.static 0.5
* Products.Quills 1.8a
* blog.star 1.0

Home Directory
==============

http://skins.quintagroup.com/sunrain

Authors
=======

* Volodymyr Rudnytskyy
* Borys Olekhnovych
* Yuriy Hvozdovych
* Taras Peretiatko

Quintagroup: http://quintagroup.com, 2006-2011
