SunRain free diazo theme for Plone 4.1.

Features
--------

**Different views**

 In SunRain Theme you can change view from: 'Rain' - defined as a default view:

 .. figure:: http://quintagroup.com/services/plone-development/skins/images/rain.png/

 to 'Sun':

 .. figure:: http://quintagroup.com/services/plone-development/skins/images/sun.png/

 To change between 'Sun' and 'Rain' views - go to 'Site Setup' -> 'Diazo theme' settings, open 'Advanced settings' tab.
 In 'Parameter expressions' textarea change ``theme = string:rain`` parameter for ``theme = string:sun`` or vice versa.

**Responsive Web Design**

 Among the most interesting features integrated into SunRain Theme you can find responsive web design that allows for easy viewing on mobile devices and tablets. If the device screen size is smaller than 5 inches the website will start to automatically resize and reposition the content to accommodate for the changes. 

**Top image**
 
 SunRain diazo theme has replaceable header image for front and inner site pages. To replace default image, upload image with ``topimage`` shortname into site root or any site section. Recommended image size: 1000*104px.

**Editable Slogan**

 SunRain Theme uses customizable slogan. To change it, go to 'Site Setup' -> 'Diazo theme' settings, open 'Advanced settings' tab.
 
 In 'Parameter expressions' field change 'Type your slogan here' slogan in ``slogan = context/slogan | string:Type your slogan here`` line.

 If you need your slogan to be displayed in non-ASCII characters, go to 'Site Setup' -> 'Diazo theme' settings, open 'Advanced settings' tab.  In 'Parameter expressions' change the following field  
 
 ``slogan = string:Type your slogan here`` 

 to 

 ``slogan = python:path('context/slogan|string:').decode('utf-8', 'ignore')``
 
 and in 'Site Setup' -> 'Zope Management Interface' settings -> 'Properties' tab add a new property 'slogan', type 'string', value 'your slogan' and save.

**Customizable Logo**

 SunRain diazo Theme comes with default Plone logo.  You can replace it with your own as you would do it in default Plone: in ZMI customize  portal_skins -> sunburst_images -> logo.png.

**Search Box**

 New approach to site search display is implemented in this theme: searchSection is hidden during common page view. Simply hover the cursor to the search box area and the searchSection appears.

**Improved thumbnail display view**

 To see the changes go to Display drop-down menu and click on Thumbnail view. 

**Editable footer** 

 Customize: portal_view_customizations -> plone.footer

**Theme Extensions**

  Additional features can be activated:

* ``Products.Carousel``
   Adds rotating Carousel banner feature.

* ``Products.ContentWellPortlets``
   Allows adding portlets in the header, footer and content area.

* ``Products.PloneFormGen``
   Adds TTW Form Generator feature.

* ``quintagroup.dropdownmenu``
   Adds adjusted stylings to dropdown menu.

* ``Products.LinguaPlone``
   Adds multilingual functionality. Adjusted stylings for language selectors.

* ``quintagroup.sunrain.policy``
   Adds four actions for subscription: 'Share on Twitter', 'Share on Facebook', 'Send this' and 'Subscribe to RSS'.
   Their links can be edited via ZMI portal_actions -> subscribe. 

   Icons can be edited via file system at '/src/quintagroup.theme.sunrain/quintagroup/theme/sunrain/static/images' folder:  replace twitter.png, facebook.png, rss.png and email.png icons with the new ones. Restart instance.

    Note, if you only downloaded ``sunrain.zip``, you will not be able to edit links. To do this, go to sunrain folder and open index.html with any editor to make the changes.

* ``quintagroup.portlet.static``
   When activated, SunRain theme will have specially-styled text  portlets: 'Green Item' and 'Grey Item'. To add them, select 'Static Stylish Portlet' from 'Add portlet...' dropdown  menu. Provide portlet text into Text area, enable 'Omit portlet border' option, and select 'Green Item' or 'Grey Item' style from 'Portlet style' menu.

   Static Stylish portlets include special styling for links (e.g. 'More...' link). To enable it, select a piece of text and set 'Link Item' style for it (Styles dropdown menu on TinyMCE toolbar).

    Note, if you only downloaded ``sunrain.zip``, you will not be able to apply 'Green Item' or 'Grey Item' style from 'Portlet style'  to your portlets. To do this, you should go to 'Site Setup' -> 'Add-on Configuration' -> Static Stylish portlet. Click on 'Add Dropdown select', enter title 'Green Item' or 'Grey Item', value 'portletGreyItem' or 'portletGreenItem' accordingly and save.

    To apply special styling for links, you should go to 'Site Setup' -> 'TinyMCE Visual Editor'. In 'Styles' textarea add 'Link Item|a|portletLinkItem' and save. 

* ``Products.Quills or blog.star``
   Blogging support.

* ``quintagroup.portlet.cumulus``
   Adds animated Tag Cloud Feature.

Dependencies
============

* plone.app.theming
* plone.app.themingplugins

Recommended
===========

Theme was tested with:

* Plone 4.1
* plone.app.theming 1.0b9
* plone.app.themingplugins 1.0b1
* Products.Carousel 2.1
* Products.ContentWellPortlets 4.1.0
* Products.PloneFormGen 1.7.0
* quintagroup.dropdownmenu 1.2.5
* Products.LinguaPlone 4.1.1
* quintagroup.sunrain.policy 1.0
* quintagroup.portlet.static 0.5
* Products.Quills 1.8a
* blog.star 1.0
* quintagroup.portlet.cumulus 1.1.0

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