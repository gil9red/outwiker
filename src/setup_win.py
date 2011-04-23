#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from cx_Freeze import setup, Executable
import os

import core.system

def getCurrentVersion ():
	"""
	Получить текущую версию для файла
	"""
	fname = "version.txt"
	path = os.path.join (core.system.getCurrentDir(), fname)

	with open (path) as fp:
		lines = fp.readlines()

	version_str = "%s.%s" % (lines[0].strip(), lines[1].strip())

	return version_str

includefiles = ['images', 'msvcr90.dll', 'Microsoft.VC90.CRT.manifest', 'help', 'locale', 'version.txt', 'tools']
includes = []
excludes = []
packages = []


setup(
	name = "OutWiker",
	version = getCurrentVersion(),
	description = "Wiki + Outliner",
	options = {'build_exe': {'excludes':excludes, 'packages':packages, 'include_files':includefiles}},
	executables = [Executable("outwiker.py", base = 'Win32GUI', icon = "images/icon.ico")])
