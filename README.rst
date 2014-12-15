SunRain free responsive diazo theme for Plone.

Screenshot
------------

.. image:: https://raw.github.com/quintagroup/quintagroup.theme.sunrain/master/quintagroup/theme/sunrain/static/images/preview.png
   :alt: SunRain Plone Theme Screenshot
   :align: center

Features
--------

**Different views**

 In SunRain Theme you can change view from: *Rain* - defined as a default view:

 .. figure:: http://quintagroup.com/services/plone-development/skins/images/rain.png/

 to *Sun*:

 .. figure:: http://quintagroup.com/services/plone-development/skins/images/sun.png/

 To change between *Sun* and *Rain* views - go to '*Site Setup -> Theming*, open *Advanced settings* tab.  In *Parameter expressions* textarea change ``theme = string:rain`` parameter for ``theme = string:sun`` or vice versa.

**Responsive Web Design**

 SunRain is a fully responsive theme that allows for easy viewing on mobile devices and tablets. The website will start to automatically resize and reposition the content to accommodate the different device screen sizes. 

**Top image**
 
 SunRain diazo theme has replaceable header image for front and inner site pages. To replace default image, upload image with ``topimage`` shortname into site root or any site section. Recommended image size: 1000*104px.

**Editable Slogan**

 SunRain Theme uses customizable slogan. To change it, go to *Site Setup -> Theming*, open *Advanced settings* tab.  In *Parameter expressions* change *Type your slogan here* slogan in *slogan* line.

 If you need your slogan to be displayed in non-ASCII characters, go to *Site Setup -> Theming*, open *Advanced settings* tab.  In *Parameter expressions* change the following field  
 
 ``slogan = string:Type your slogan here`` 

 to 

 ``slogan = python:path('context/slogan|string:').decode('utf-8', 'ignore')``
 
 and in *Site Setup -> Zope Management Interface settings -> Properties* tab add a new property *slogan*, type ``string``, value ``your slogan`` and save.

**Customizable Logo**

 SunRain diazo Theme comes with default Plone logo.  You can replace it with your own as you would do it in default Plone: in ZMI customize  *portal_skins -> sunburst_images -> logo.png*.

**Search Box**

 Search box is hidden while browsing. Simply hover the cursor to the search box area for it to appear.

**Improved thumbnail display view**

 To see the changes go to *Display* drop-down menu and click on ``Thumbnail`` view. 

**Editable footer** 

 Customize: *portal_view_customizations -> plone.footer*.

**Theme Extensions**

  Additional features can be activated:

* ``Products.Carousel``
   Adds rotating Carousel banner feature.

* ``Products.ContentWellPortlets``
   Allows adding portlets in the header, footer and content area.

* ``Products.PloneFormGen``
   Adds TTW Form Generator feature.

* ``quintagroup.dropdownmenu``
   Adds adjusted styling to drop-down menu.

* ``Products.LinguaPlone``
   Adds multilingual functionality with adjusted styling for language selectors.

* ``quintagroup.sunrain.policy``
   Adds four actions for subscription: *Share on Twitter, Share on Facebook, Send this and Subscribe to RSS*.
   Their links can be edited via ZMI *portal_actions -> subscribe*. 

   Icons can be edited via file system at */src/quintagroup.theme.sunrain/quintagroup/theme/sunrain/static/images* folder:  replace ``twitter.png``, ``facebook.png``, ``rss.png`` and ``email.png`` icons with the new ones. Restart instance.

   Note, if you only downloaded ``sunrain.zip``, you will not be able to edit links. To do this, go to sunrain folder and open *index.html* with any editor to make the changes.

* ``quintagroup.portlet.static``
   When activated, SunRain theme will have specially-styled text  portlets: *Green Item* and *Grey Item*. To add them, select *Static Stylish Portlet* from *Add portlet...* drop-down  menu. Provide portlet text into text area, enable *Omit portlet border* option, and select ``Green Item/Grey Item`` style from *Portlet style* menu.

   Static Stylish portlets include special styling for links (e.g. 'More...' link). To enable it, select a piece of text and set ``Link Item`` style for it (Styles drop-down menu on TinyMCE toolbar).

    Note, if you only downloaded ``sunrain.zip``, you will not be able to apply *Green Item* and *Grey Item* style to your portlets. To do this, you should go to *Site Setup -> Add-on Configuration -> Static Stylish portlet*. Click on *Add Dropdown select*, enter title ``Green Item`` or ``Grey Item``, value ``portletGreyItem`` or ``portletGreenItem`` accordingly and save.

    To apply special styling for links, you should go to *Site Setup -> TinyMCE Visual Editor*. In *Styles* textarea add ``Link Item|a|portletLinkItem`` and save. 

* ``Products.Quills or blog.star``
    Blogging support.

* ``quintagroup.portlet.cumulus``
    Adds animated Tag Cloud Feature.

* ``quintagroup.slidertemplates``
    Enhanced Responsive Views for NG Collection Portlet (Carousel, Shelf, Tabs)

* ``quintagroup.megamenu``  
    Clean and professional fully responsive Mega Menu solution for Plone. This product allows Plone website to display panel added to portal top as drop-down menu for navigation tabs.

Dependencies
============

* plone.app.theming
* plone.app.themingplugins

Recommended
===========

Theme was tested with:

* Plone 4.3rc1
* plone.app.theming 1.1b2
* plone.app.themingplugins 1.0b1
* Products.Carousel 2.2.1
* Products.ContentWellPortlets 4.2.1
* Products.PloneFormGen 1.7.6
* quintagroup.dropdownmenu 1.2.11
* Products.LinguaPlone 4.1.3
* quintagroup.sunrain.policy 1.0
* quintagroup.portlet.static 0.7
* Products.Quills 1.8a1
* blog.star 1.1
* quintagroup.portlet.cumulus 1.1.0
* quintagroup.megamenu 1.3
* quintagroup.slidertemplates 1.0

Home Directory
==============

http://themes.quintagroup.com/product/sunrain

Authors
=======

* Taras Peretiatko
* Volodymyr Rudnytskyy
* Borys Olekhnovych
* Yuriy Hvozdovych

Quintagroup: http://quintagroup.com, 2013