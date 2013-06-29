#!/usr/bin/python
# -*- coding: UTF-8 -*-

from outwiker.core.commands import getCurrentVersion
from outwiker.core.version import Version

from .versionlist import VersionList
from .updatedialog import UpdateDialog


class UpdateDialogController (object):
    """
    Контроллер для управления UpdateDialog.
    Сюда вынесена вся логика.
    """
    def __init__ (self, application):
        self._application = application
        self._updateDialog = UpdateDialog (self._application.mainWindow)


    def _updateVersions (self):
        verList = VersionList (self._application.plugins)
        verList.updateVersions()

        currentVersion = getCurrentVersion()
        stableVersion = verList.getStableVersion()
        unstableVersion = verList.getUnstableVersion()

        self._updateDialog.setCurrentOutWikerVersion (currentVersion)
        self._updateDialog.setLatestStableOutwikerVersion (stableVersion, currentVersion < stableVersion)
        self._updateDialog.setLatestUnstableOutwikerVersion (unstableVersion, currentVersion < unstableVersion)

        for plugin in self._application.plugins:
            pluginVersion = verList.getPluginVersion (plugin.name)
            if (pluginVersion != None and
                    pluginVersion > Version.parse (plugin.version)):
                try:
                    self._updateDialog.addPluginInfo (plugin, 
                            pluginVersion,
                            verList.getPluginUrl (plugin.name))
                except KeyError:
                    pass
        

    def ShowModal (self):
        self._updateVersions()
        return self._updateDialog.ShowModal()
