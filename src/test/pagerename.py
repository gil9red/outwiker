#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os.path
import unittest
import stat

from core.tree import RootWikiPage, WikiDocument

from pages.text.textpage import TextPageFactory, TextWikiPage
from core.attachment import Attachment

from test.utils import removeWiki
import core.exceptions


class RenameTest (unittest.TestCase):
	def setUp (self):
		self.path = u"../test/testwiki"
		removeWiki (self.path)

		self.rootwiki = WikiDocument.create (self.path)

		TextPageFactory.create (self.rootwiki, u"Страница 1", [])
		TextPageFactory.create (self.rootwiki, u"Страница 2", [])
		TextPageFactory.create (self.rootwiki[u"Страница 2"], u"Страница 3", [])
		TextPageFactory.create (self.rootwiki[u"Страница 2/Страница 3"], u"Страница 4", [])
		TextPageFactory.create (self.rootwiki[u"Страница 1"], u"Страница 5", [])
		TextPageFactory.create (self.rootwiki, u"Страница 6", [])

		self.treeUpdateCount = 0

	
	def testRename1 (self):
		page = self.rootwiki[u"Страница 1"]
		page.title = u"Страница 1 new"

		self.assertEqual (page.title, u"Страница 1 new")
		self.assertEqual (self.rootwiki[u"Страница 1 new"], page)
		self.assertEqual (page.subpath, u"Страница 1 new")
		self.assertEqual (self.rootwiki[u"Страница 1"], None)
		self.assertTrue (os.path.exists (self.rootwiki[u"Страница 1 new"].path))

	
	def testInvalidRename (self):
		def rename (page, newtitle):
			page.title = newtitle

		self.assertRaises (core.exceptions.DublicateTitle, rename, 
				self.rootwiki[u"Страница 1"], u"СтраНица 6")
	

	def testRename2 (self):
		page = self.rootwiki[u"Страница 2/Страница 3"]
		page.title = u"Страница 3 new"

		self.assertEqual (page.title, u"Страница 3 new")
		self.assertEqual (self.rootwiki[u"Страница 2/Страница 3 new"], page)
		self.assertEqual (page.subpath, u"Страница 2/Страница 3 new")
		self.assertEqual (self.rootwiki[u"Страница 2/Страница 3"], None)
	

	def testRename3 (self):
		page3 = self.rootwiki[u"Страница 2/Страница 3"]
		page4 = page3[u"Страница 4"]

		page3.title = u"Страница 3 new"

		self.assertEqual (page3[u"Страница 4"], page4)
		self.assertEqual (self.rootwiki[u"Страница 2/Страница 3 new/Страница 4"], page4)
	

	def testRename4 (self):
		page = self.rootwiki[u"Страница 1"]
		page.title = u"СтрАницА 1"

		self.assertEqual (page.title, u"СтрАницА 1")
		self.assertEqual (self.rootwiki[u"СтрАницА 1"], page)
		self.assertEqual (page.subpath, u"СтрАницА 1")

	
	def testLoad (self):
		page = self.rootwiki[u"Страница 1"]
		page.title = u"Страница 1 new"

		wiki = WikiDocument.load (self.path)
		self.assertNotEqual (wiki[u"Страница 1 new"], None)
		self.assertEqual (wiki[u"Страница 1"], None)
	

	def testBookmarks1 (self):
		page = self.rootwiki[u"Страница 6"]
		self.rootwiki.bookmarks.add (page)
		page.title = u"Страница 6 new"

		self.assertTrue (self.rootwiki.bookmarks.pageMarked (page))
	

	def testBookmarks2 (self):
		page2 = self.rootwiki[u"Страница 2"]
		page3 = self.rootwiki[u"Страница 2/Страница 3"]
		page4 = self.rootwiki[u"Страница 2/Страница 3/Страница 4"]

		self.rootwiki.bookmarks.add (page2)
		self.rootwiki.bookmarks.add (page3)
		self.rootwiki.bookmarks.add (page4)

		page2.title = u"Страница 2 new"

		self.assertTrue (self.rootwiki.bookmarks.pageMarked (page2))
		self.assertTrue (self.rootwiki.bookmarks.pageMarked (page3))
		self.assertTrue (self.rootwiki.bookmarks.pageMarked (page4))
	

	def testPath (self):
		page2 = self.rootwiki[u"Страница 2"]
		page3 = self.rootwiki[u"Страница 2/Страница 3"]
		page4 = self.rootwiki[u"Страница 2/Страница 3/Страница 4"]

		page2.title = u"Страница 2 new"

		self.assertEqual (page2.path, os.path.join (self.path, u"Страница 2 new"))
		self.assertEqual (page3.path, os.path.join (self.path, u"Страница 2 new", u"Страница 3"))
		self.assertEqual (page4.path, os.path.join (self.path, u"Страница 2 new", u"Страница 3", u"Страница 4"))
	

	def testConfig (self):
		page2 = self.rootwiki[u"Страница 2"]
		page3 = self.rootwiki[u"Страница 2/Страница 3"]
		page4 = self.rootwiki[u"Страница 2/Страница 3/Страница 4"]

		page2.title = u"Страница 2 new"

		page2.tags = [u"тег 1"]
		page3.tags = [u"тег 2"]
		page4.tags = [u"тег 3"]

		self.assertEqual (page2.tags[0], u"тег 1")
		self.assertEqual (page3.tags[0], u"тег 2")
		self.assertEqual (page4.tags[0], u"тег 3")


	def testRenameError (self):
		page = self.rootwiki[u"Страница 2"]
		attach = Attachment (page)

		with open (attach.getFullPath ("111.txt", True), "w") as fp:
			try:
				page.title = u"Новое имя"
			except OSError:
				pass
			else:
				self.assertTrue (os.path.exists (self.rootwiki[u"Новое имя"].path))
				self.assertEqual (self.rootwiki[u"Страница 2"], None)
