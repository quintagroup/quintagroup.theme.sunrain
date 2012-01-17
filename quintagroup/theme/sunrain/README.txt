SunRain free diazo theme for Plone 4.1.
    
Features
--------

* SunRain Theme can be presented in two different views: 'Rain' - defined as a default view:

 .. figure:: http://quintagroup.com/services/plone-development/skins/images/rain.png/

 and 'Sun':

 .. figure:: http://quintagroup.com/services/plone-development/skins/images/sun.png/

 To change between 'Sun' and 'Rain' views - go to 'Site Setup' -> 'Diazo theme' settings, open 'Advanced settings' tab.
 In 'Parameter expressions' field change ``theme = string:rain`` for ``theme = string:sun`` or vice versa.

* Top image. SunRain diazo theme has replaceable header image for front and inner site pages. To replace default image - upload image with
  ``topimage`` shortname into site root or any site section. Recommended image size: 1000*104px.

* SunRain theme has 'subscribe' viewlet integrated, that adds 4 actions 'Share on Twitter', 'Share on Facebook', 'Send this'
  and 'Subscribe to RSS'. Their links can be edited via ZMI portal_actions -> subscribe. 
  
  Icons can be edited via file system at /src/quintagroup.theme.sunrain/quintagroup/theme/sunrain/static/images folder: 
  replace twitter.png, facebook.png, rss.png and email.png icons with new ones. Restart instance.

* Slogan. SunRain Theme uses customizable slogan. To change it, go to 'Site Setup' -> 'Diazo theme' settings, open 'Advanced settings' tab.
  In 'Parameter expressions' field change 'Type your slogan here' slogan in ``slogan = context/slogan | string: Type your slogan here`` line.

* Logo. SunRain diazo Theme uses default Plone 4 logo. To replace it - in ZMI customize portal_skins -> sunburst_images -> logo.png image.

* Search Box. New approach to site search display is implemented in this theme: searchSection is hidden during common page 
  view. Simply hover the cursor to the search box area and the searchSection appears.

* Improved thumbnail display view (switch to Thumbnail view)

* Editable footer. Customize: portal_view_customizations -> plone.footer

**Additional Features**

Features, that are supported and can be activated by additional packages installation:

* quintagroup.dropdownmenu. Adds custom-style dropdown menu

* Products.Carousel. Adds rotating Carousel banner feature

* Products.LinguaPlone. Adds multilingual functionality. Custom-style language selectors.

* Products.PloneFormGen. Adds TTW Form Generator feature.

* Products.ContentWellPortlets. Allows adding portlets in the header, footer and content area

* quintagroup.portlet.static. When activated, SunRain theme will have specially-styled text  portlets: 'Green Item' and 
  'Grey Item'. To add them - select 'Static Stylish Portlet' from 'Add portlet...' drop down  menu. Provide portlet text 
  into Text area, enable 'Omit portlet border' option, and select 'Green Item' or 'Grey Item' style from 'Portlet style' menu.
  
  Static Stylish portlets include special styling for links (e.g. 'More...' link). To enable it - select a piece of text 
  and set 'Link Item' style for it (Styles drop-down menu on TinyMCE toolbar).

* Products.Quills or blog.star. Blogging support

* quintagroup.portlet.cumulus. Adds animated Tag Cloud Feature


Recommended
===========

Theme was tested with:

* Plone 4.1
* plone.app.theming 1.0b9
* plone.app.themingplugins 1.0b1
* quintagroup.portlet.cumulus 1.1.0
* quintagroup.portlet.static 0.5
* Products.Quills 1.8a
* blog.star 1.0
* Products.Carousel 2.1
* quintagroup.dropdownmenu 1.2.5
* Products.LinguaPlone 4.1.1
* Products.PloneFormGen 1.7.0
* Products.ContentWellPortlets 4.1.0

Dependencies
============

* plone.app.theming
* plone.app.themingplugins

Home Directory
==============

http://skins.quintagroup.com/sunrain

Authors
=======

* Taras Peretiatko
* Volodymyr Rudnytskyy
* Borys Olekhnovych
* Yuriy Hvozdovych

Quintagroup: http://quintagroup.com, 2006-2012
