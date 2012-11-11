#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Thu Nov 18 21:58:50 2010

import os.path

import wx

from outwiker.core.system import getImagesDir

# begin wxGlade: extracode
# end wxGlade


class AboutDialog(wx.Dialog):
    def __init__(self, currversion, *args, **kwds):
        self.imagesDir = getImagesDir()

        # begin wxGlade: AboutDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.THICK_FRAME
        wx.Dialog.__init__(self, *args, **kwds)
        self.titleLabel = wx.StaticText(self, -1, _("OutWiker"))
        self.versionTitleLabel = wx.StaticText(self, -1, _("Version:"))
        self.versionLabel = wx.StaticText(self, -1, "")
        self.notebook = wx.Notebook(self, -1, style=0)
        self.aboutPane = wx.Panel(self.notebook, -1)
        self.logo = wx.StaticBitmap(self.aboutPane, -1, wx.Bitmap(os.path.join (self.imagesDir, "outwiker_64x64.png"), wx.BITMAP_TYPE_ANY))
        # self.description = wx.TextCtrl(self.aboutPane, -1, _("OutWiker is personal wiki system and tree notes outliner."), style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_LINEWRAP | wx.NO_BORDER)
        self.description = wx.StaticText (self.aboutPane, -1, _("OutWiker is personal wiki system and tree notes outliner."))
        self.license = wx.StaticText(self.aboutPane, -1, _("License: GPL 3"))
        self.siteLabel = wx.StaticText(self.aboutPane, -1, _("OutWiker's page:"))
        self.outwikerUrl = wx.HyperlinkCtrl(self.aboutPane, -1, label=_("http://jenyay.net/Outwiker/English"), url=_("http://jenyay.net/Outwiker/English"))
        self.contactsPane = wx.Panel(self.notebook, -1)
        self.email = wx.HyperlinkCtrl(self.contactsPane, -1, label=_(u"jenyay.ilin@gmail.com"), url=_(u"mailto:jenyay.ilin@gmail.com"))
        self.googleplus = wx.HyperlinkCtrl(self.contactsPane, -1, label=_(u"Google+ page"), url=_(u"https://plus.google.com/u/0/b/113404982971748285098/113404982971748285098/posts"))
        self.facebook = wx.HyperlinkCtrl(self.contactsPane, -1, label=_(u"Facebook page"), url=_(u"http://www.facebook.com/outwiker"))
        self.livejournal = wx.HyperlinkCtrl(self.contactsPane, -1, label=_(u"Livejournal community"), url=_(u"http://ru-outwiker.livejournal.com/?style=mine"))
        self.twitter = wx.HyperlinkCtrl(self.contactsPane, -1, label=_(u"Twitter"), url=_(u"https://twitter.com/OutWiker"))
        self.vkontakte = wx.HyperlinkCtrl(self.contactsPane, -1, label=_(u"Vkontakte group"), url=_(u"http://vk.com/outwiker"))
        self.okButton = wx.Button(self, wx.ID_OK, "")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

        self.currversion = currversion
        self.versionLabel.SetLabel (str (self.currversion))


    def __set_properties(self):
        # begin wxGlade: AboutDialog.__set_properties
        self.SetTitle(_("About"))
        self.SetSize((500, 350))
        self.titleLabel.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.description.SetMinSize((-1, 50))
        self.okButton.SetFocus()
        self.okButton.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AboutDialog.__do_layout
        main_sizer = wx.FlexGridSizer(4, 1, 0, 0)
        grid_sizer_4 = wx.FlexGridSizer(1, 1, 0, 0)
        grid_sizer_2 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_3 = wx.FlexGridSizer(1, 1, 0, 0)
        sizeSizer = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_1 = wx.FlexGridSizer(1, 2, 0, 0)
        main_sizer.Add(self.titleLabel, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 2)
        grid_sizer_1.Add(self.versionTitleLabel, 0, wx.ALL | wx.ALIGN_RIGHT, 2)
        grid_sizer_1.Add(self.versionLabel, 0, wx.ALL, 2)
        grid_sizer_1.AddGrowableRow(0)
        grid_sizer_1.AddGrowableCol(0)
        grid_sizer_1.AddGrowableCol(1)
        main_sizer.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.logo, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 2)
        grid_sizer_3.Add(self.description, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, border=4)
        author = wx.StaticText(self.aboutPane, -1, _("Author: Ilin Eugeniy (aka Jenyay)"))
        grid_sizer_3.Add(author, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 2)
        grid_sizer_3.Add(self.license, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 2)
        sizeSizer.Add(self.siteLabel, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 2)
        sizeSizer.Add(self.outwikerUrl, 1, wx.ALL | wx.EXPAND | wx.ALIGN_RIGHT, 2)
        sizeSizer.AddGrowableCol(1)
        grid_sizer_3.Add(sizeSizer, 1, wx.EXPAND, 0)
        grid_sizer_3.AddGrowableCol(0)
        grid_sizer_2.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        self.aboutPane.SetSizer(grid_sizer_2)
        grid_sizer_2.AddGrowableRow(0)
        grid_sizer_2.AddGrowableCol(1)
        grid_sizer_4.Add(self.email, 1, wx.ALL | wx.EXPAND | wx.ALIGN_RIGHT, 2)
        grid_sizer_4.Add(self.googleplus, 1, wx.ALL | wx.EXPAND | wx.ALIGN_RIGHT, 2)
        grid_sizer_4.Add(self.facebook, 1, wx.ALL | wx.EXPAND | wx.ALIGN_RIGHT, 2)
        grid_sizer_4.Add(self.livejournal, 1, wx.ALL | wx.EXPAND | wx.ALIGN_RIGHT, 2)
        grid_sizer_4.Add(self.twitter, 1, wx.ALL | wx.EXPAND | wx.ALIGN_RIGHT, 2)
        grid_sizer_4.Add(self.vkontakte, 1, wx.ALL | wx.EXPAND | wx.ALIGN_RIGHT, 2)
        self.contactsPane.SetSizer(grid_sizer_4)
        grid_sizer_4.AddGrowableCol(0)
        self.notebook.AddPage(self.aboutPane, _("About"))
        self.notebook.AddPage(self.contactsPane, _("Contacts"))
        main_sizer.Add(self.notebook, 1, wx.ALL | wx.EXPAND, 2)
        main_sizer.Add(self.okButton, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 4)
        self.SetSizer(main_sizer)
        main_sizer.AddGrowableRow(2)
        main_sizer.AddGrowableCol(0)
        self.Layout()
        self.Centre()
        # end wxGlade

# end of class AboutDialog


