# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Sun Apr 18 22:17:12 2010

import os
import re
from abc import ABCMeta, abstractmethod

import wx

from core.controller import Controller
from gui.BaseTextPanel import BaseTextPanel
import core.system
from gui.htmlview import HtmlView
from gui.HtmlTextEditor import HtmlTextEditor
import core.commands
from core.htmlimprover import HtmlImprover

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade


class ToolsInfo (object):
	def __init__ (self, id, alwaysEnabled):
		"""
		id - идентификатор
		alwaysEnabled - кнопка всегда активна?
		"""
		self.id = id
		self.alwaysEnabled = alwaysEnabled


class HtmlPanel(BaseTextPanel):
	__metaclass__ = ABCMeta
	
	def __init__(self, *args, **kwds):
		BaseTextPanel.__init__ (self, *args, **kwds)
		self._htmlFile = "__content.html"
		self.currentHtmlFile = None

		# Номера страниц-вкладок
		self.codePageIndex = 0
		self.resultPageIndex = 1

		self.imagesDir = core.system.getImagesDir()

		# begin wxGlade: HtmlPanel.__init__
		kwds["style"] = wx.TAB_TRAVERSAL
		wx.Panel.__init__(self, *args, **kwds)
		self.notebook = wx.Notebook(self, -1, style=wx.NB_BOTTOM)
		self.previewPane = wx.Panel(self.notebook, -1)
		self.htmlPane = wx.Panel(self.notebook, -1)
		self.codeWindow = self.GetTextEditor()
		self.htmlWindow = HtmlView(self.previewPane, -1)

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.onTabChanged, self.notebook)
		# end wxGlade

		self.HCount = 6
		self.toolsId = {}


	def GetTextEditor(self):
		return HtmlTextEditor (self.htmlPane)

	
	def onEditorConfigChange (self):
		self.codeWindow.setDefaultSettings()

	
	def onClose (self, event):
		BaseTextPanel.Close (self)


	def onAttachmentPaste (self, fnames):
		text = self._getAttachString (fnames)
		self.codeWindow.textCtrl.AddText (text)
		self.codeWindow.textCtrl.SetFocus()

	
	def UpdateView (self, page):
		self.htmlWindow.page = self._currentpage
		self.codeWindow.textCtrl.SetText (self._currentpage.content)
		self.codeWindow.textCtrl.EmptyUndoBuffer()
		self.codeWindow.textCtrl.SetReadOnly (page.readonly)


	def GetContentFromGui(self):
		return self.codeWindow.textCtrl.GetText()
	
	
	def __set_properties(self):
		# begin wxGlade: HtmlPanel.__set_properties
		pass
		# end wxGlade


	def __do_layout(self):
		# begin wxGlade: HtmlPanel.__do_layout
		grid_sizer_7 = wx.FlexGridSizer(1, 1, 0, 0)
		grid_sizer_9 = wx.FlexGridSizer(1, 1, 0, 0)
		grid_sizer_8 = wx.FlexGridSizer(1, 1, 0, 0)
		grid_sizer_8.Add(self.codeWindow, 1, wx.TOP|wx.BOTTOM|wx.EXPAND, 2)
		self.htmlPane.SetSizer(grid_sizer_8)
		grid_sizer_8.AddGrowableRow(0)
		grid_sizer_8.AddGrowableCol(0)
		grid_sizer_9.Add(self.htmlWindow, 1, wx.EXPAND, 0)
		self.previewPane.SetSizer(grid_sizer_9)
		grid_sizer_9.AddGrowableRow(0)
		grid_sizer_9.AddGrowableCol(0)
		self.notebook.AddPage(self.htmlPane, _("HTML"))
		self.notebook.AddPage(self.previewPane, _("Preview"))
		grid_sizer_7.Add(self.notebook, 1, wx.EXPAND, 0)
		self.SetSizer(grid_sizer_7)
		grid_sizer_7.Fit(self)
		grid_sizer_7.AddGrowableRow(0)
		grid_sizer_7.AddGrowableCol(0)
		# end wxGlade

		self.Bind (wx.EVT_CLOSE, self.onClose)


	@abstractmethod
	def generateHtml (self, page, path):
		pass


	def getHtmlPath (self, path):
		"""
		Получить путь до результирующего файла HTML
		"""
		path = os.path.join (self._currentpage.path, self._htmlFile)
		return path


	def removeHtml (self):
		"""
		Удалить сгенерированный HTML-файл
		"""
		if self.currentHtmlFile != None:
			try:
				os.remove (self.currentHtmlFile)
			except OSError:
				pass
	

	def _openDefaultPage(self):
		assert self._currentpage != None

		if len (self._currentpage.content) > 0 or len (self._currentpage.attachment) > 0:
			self.notebook.SetSelection (self.resultPageIndex)
		else:
			self.notebook.SetSelection (self.codePageIndex)
			self.codeWindow.textCtrl.SetFocus()


	def onTabChanged(self, event): # wxGlade: HtmlPanel.<event_handler>
		if self._currentpage == None:
			return

		if event.GetSelection() == self.resultPageIndex:
			self._onSwitchToPreview()
		else:
			self._onSwitchToCode()
	

	def _onSwitchToCode (self):
		"""
		Обработка события при переключении на код страницы
		"""
		self._enableTools (self.pageToolsMenu, True)
		self.codeWindow.textCtrl.SetFocus()

	
	def _onSwitchToPreview (self):
		"""
		Обработка события при переключении на просмотр страницы
		"""
		self.Save()
		self._enableTools (self.pageToolsMenu, False)
		self.htmlWindow.SetFocus()
		self.htmlWindow.Update()
		self.__showHtml()
	

	def __showHtml (self):
		"""
		Подготовить и показать HTML текущей страницы
		"""
		assert self._currentpage != None

		core.commands.setStatusText (_(u"Page rendered. Please wait...") )
		Controller.instance().onHtmlRenderingBegin (self._currentpage, self.htmlWindow)

		path = self.getHtmlPath (self._currentpage)
		self.currentHtmlFile = path
		try:
			self.generateHtml (self._currentpage, path)
		except IOError:
			wx.MessageBox (_(u"Can't save HTML-file"), _(u"Error"), wx.ICON_ERROR | wx.OK)

		self.htmlWindow.LoadPage (path)

		core.commands.setStatusText (u"")
		Controller.instance().onHtmlRenderingEnd (self._currentpage, self.htmlWindow)
	

	def _enableTools (self, menu, enable):
		for key in self.toolsId:
			if not self.toolsId[key].alwaysEnabled:
				if self.mainWindow.mainToolbar.FindById (self.toolsId[key].id) != None:
					self.mainWindow.mainToolbar.EnableTool (self.toolsId[key].id, enable)
				menu.Enable (self.toolsId[key].id, enable)
	

	def GetSearchPanel (self):
		if self.notebook.GetSelection() == self.codePageIndex:
			return self.codeWindow.searchPanel

		return None


	def _removeTool (self, id):
		if self.mainWindow.mainToolbar.FindById (id) != None:
			self.mainWindow.mainToolbar.DeleteTool (id)
		self.mainWindow.Unbind(wx.EVT_MENU, id=id)


	def _addRenderTools (self):
		self._addTool (self.pageToolsMenu, 
				"ID_RENDER", 
				self.__switchView, 
				_(u"Code / Preview\tF5"), 
				_(u"Code / Preview"), 
				os.path.join (self.imagesDir, "render.png"),
				True)

		self.pageToolsMenu.AppendSeparator()


	def __switchView (self, event):
		if self._currentpage == None:
			return

		if self.notebook.GetSelection() == self.codePageIndex:
			self.notebook.SetSelection (self.resultPageIndex)
		else:
			self.notebook.SetSelection (self.codePageIndex)


	def _addTool (self, menu, idstring, func, menuText, buttonText, image, alwaysEnabled = False):
		"""
		Добавить пункт меню и кнопку на панель
		menu -- меню для добавления элемента
		id -- идентификатор меню и кнопки
		func -- обработчик
		menuText -- название пунта меню
		buttonText -- подсказка для кнопки
		image -- имя файла с картинкой
		disableOnView -- дизаблить кнопку при переключении на просмотр результата
		"""
		id = wx.NewId()
		self.toolsId[idstring] = ToolsInfo (id, alwaysEnabled)

		menu.Append (id, menuText, "", wx.ITEM_NORMAL)
		self.mainWindow.Bind(wx.EVT_MENU, func, id = id)

		if image != None and len (image) != 0:
			self.mainWindow.mainToolbar.AddLabelTool(id, 
					buttonText, 
					wx.Bitmap(image, wx.BITMAP_TYPE_ANY), 
					wx.NullBitmap, 
					wx.ITEM_NORMAL, 
					buttonText, 
					"")
	

	def removeGui (self):
		BaseTextPanel.removeGui (self)

		for key in self.toolsId.keys ():
			self._removeTool (self.toolsId[key].id)


	def _turnText (self, lefttext, righttext):
		selText = self.codeWindow.textCtrl.GetSelectedText()
		newtext = lefttext + selText + righttext
		self.codeWindow.textCtrl.ReplaceSelection (newtext)

		if len (selText) == 0:
			"""
			Если не оборачиваем текст, а делаем пустой тег, то поместим каретку до закрывающегося тега
			"""
			currPos = self.codeWindow.textCtrl.GetSelectionEnd()
			len_bytes = self.codeWindow.calcByteLen (righttext)

			newPos = currPos - len_bytes

			self.codeWindow.textCtrl.SetSelection (newPos, newPos)
	

	def _turnList (self, start, end, itemStart, itemEnd):
		"""
		Создать список
		"""
		selText = self.codeWindow.textCtrl.GetSelectedText()
		items = filter (lambda item: len (item.strip()) > 0, selText.split ("\n") )

		# Собираем все элементы
		if len (items) > 0:
			itemsList = reduce (lambda result, item: result + itemStart + item.strip() + itemEnd + "\n", items, u"")
		else:
			itemsList = itemStart + itemEnd + "\n"

		result = start + itemsList + end

		if len (end) == 0:
			# Если нет завершающего тега (как в викинотации), 
			# то не нужен перевод строки у последнего элемента
			result = result[: -1]

		self.codeWindow.textCtrl.ReplaceSelection (result)

		if len (items) == 0:
			endText = u"%s\n%s" % (itemEnd, end)
			len_bytes = self.codeWindow.calcByteLen (endText)

			currPos = self.codeWindow.textCtrl.GetSelectionEnd()
			newPos = currPos - len_bytes
			self.codeWindow.textCtrl.SetSelection (newPos, newPos)


	def _replaceText (self, text):
		self.codeWindow.textCtrl.ReplaceSelection (text)


# end of class HtmlPanel

class HtmlPagePanel (HtmlPanel):
	def __init__ (self, *args, **kwds):
		HtmlPanel.__init__ (self, *args, **kwds)


	def __addFontTools (self):
		"""
		Добавить инструменты, связанные со шрифтами
		"""
		self._addTool (self.pageToolsMenu, 
				"ID_BOLD", 
				lambda event: self._turnText (u"<b>", u"</b>"), 
				_(u"Bold\tCtrl+B"), 
				_(u"Bold (<b>...</b>)"), 
				os.path.join (self.imagesDir, "text_bold.png"))

		self._addTool (self.pageToolsMenu, 
				"ID_ITALIC", 
				lambda event: self._turnText (u"<i>", u"</i>"), 
				_(u"Italic\tCtrl+I"), 
				_(u"Italic (<i>...</i>)"), 
				os.path.join (self.imagesDir, "text_italic.png"))

		self._addTool (self.pageToolsMenu, 
				"ID_UNDERLINE", 
				lambda event: self._turnText (u"<u>", u"</u>"), 
				_(u"Underline\tCtrl+U"), 
				_(u"Underline (<u>...</u>)"), 
				os.path.join (self.imagesDir, "text_underline.png"))

		self._addTool (self.pageToolsMenu, 
				"ID_SUBSCRIPT", 
				lambda event: self._turnText (u"<SUB>", u"</SUB>"), 
				_(u"Subscript\tCtrl+="), 
				_(u"Subscript (<sub> ... </sub>)"), 
				os.path.join (self.imagesDir, "text_subscript.png"))

		self._addTool (self.pageToolsMenu, 
				"ID_SUPERSCRIPT", 
				lambda event: self._turnText (u"<SUP>", u"</SUP>"), 
				_(u"Superscript\tCtrl++"), 
				_(u"Superscript (<sup> ... </sup>)"), 
				os.path.join (self.imagesDir, "text_superscript.png"))

	
	def __addAlignTools (self):
		self._addTool (self.pageToolsMenu, 
				"ID_ALIGN_CENTER", 
				lambda event: self._turnText (u'<DIV ALIGN="CENTER">', u'</DIV>'), 
				_(u"Center align\tCtrl+Shift+C"), 
				_(u"Center align"), 
				os.path.join (self.imagesDir, "text_align_center.png"))

		self._addTool (self.pageToolsMenu, 
				"ID_ALIGN_RIGHT", 
				lambda event: self._turnText (u'<DIV ALIGN="RIGHT">', u'</DIV>'), 
				_(u"Right align"), 
				_(u"Right align"), 
				os.path.join (self.imagesDir, "text_align_right.png"))
	

	def __addTableTools (self):
		"""
		Добавить инструменты, связанные с таблицами
		"""
		self._addTool (self.pageToolsMenu, 
				"ID_TABLE", 
				lambda event: self._turnText (u'<table>', u'</table>'), 
				_(u"Table\tCtrl+Q"), 
				_(u"Table (<table>...</table>)"), 
				os.path.join (self.imagesDir, "table.png"))

		self._addTool (self.pageToolsMenu, 
				"ID_TABLE_TR", 
				lambda event: self._turnText (u'<tr>',u'</tr>'), 
				_(u"Table row\tCtrl+W"), 
				_(u"Table row (<tr>...</tr>)"), 
				os.path.join (self.imagesDir, "table_insert_row.png"))


		self._addTool (self.pageToolsMenu, 
				"ID_TABLE_TD", 
				lambda event: self._turnText (u'<td>', u'</td>'), 
				_(u"Table cell\tCtrl+Y"), 
				_(u"Table cell (<td>...</td>)"), 
				os.path.join (self.imagesDir, "table_insert_cell.png"))

	
	def __addListTools (self):
		"""
		Добавить инструменты, связанные со списками
		"""
		self._addTool (self.pageToolsMenu, 
				"ID_MARK_LIST", 
				lambda event: self._turnList (u'<ul>\n', u'</ul>', u'<li>', u'</li>'), 
				_(u"Bullets list\tCtrl+G"), 
				_(u"Bullets list (<ul>...</ul>)"), 
				os.path.join (self.imagesDir, "text_list_bullets.png"))

		self._addTool (self.pageToolsMenu, 
				"ID_NUMBER_LIST", 
				lambda event: self._turnList (u'<ol>\n', u'</ol>', u'<li>', u'</li>'), 
				_(u"Numbers list\tCtrl+J"), 
				_(u"Numbers list (<ul>...</ul>)"), 
				os.path.join (self.imagesDir, "text_list_numbers.png"))
	

	def __addHTools (self):
		"""
		Добавить инструменты для заголовочных тегов <H>
		"""
		self._addTool (self.pageToolsMenu, 
				"ID_H1", 
				lambda event: self._turnText (u"<h1>", u"</h1>"), 
				_(u"H1\tCtrl+1"), 
				_(u"H1 (<h1>...</h1>)"), 
				os.path.join (self.imagesDir, "text_heading_1.png"))

		self._addTool (self.pageToolsMenu, 
				"ID_H2", 
				lambda event: self._turnText (u"<h2>", u"</h2>"), 
				_(u"H2\tCtrl+2"), 
				_(u"H2 (<h2>...</h2>)"), 
				os.path.join (self.imagesDir, "text_heading_2.png"))
		
		self._addTool (self.pageToolsMenu, 
				"ID_H3", 
				lambda event: self._turnText (u"<h3>", u"</h3>"), 
				_(u"H3\tCtrl+3"), 
				_(u"H3 (<h3>...</h3>)"), 
				os.path.join (self.imagesDir, "text_heading_3.png"))

		self._addTool (self.pageToolsMenu, 
				"ID_H4", 
				lambda event: self._turnText (u"<h4>", u"</h4>"), 
				_(u"H4\tCtrl+4"), 
				_(u"H4 (<h4>...</h4>)"), 
				os.path.join (self.imagesDir, "text_heading_4.png"))

		self._addTool (self.pageToolsMenu, 
				"ID_H5", 
				lambda event: self._turnText (u"<h5>", u"</h5>"), 
				_(u"H5\tCtrl+5"), 
				_(u"H5 (<h5>...</h5>)"), 
				os.path.join (self.imagesDir, "text_heading_5.png"))

		self._addTool (self.pageToolsMenu, 
				"ID_H6", 
				lambda event: self._turnText (u"<h6>", u"</h6>"), 
				_(u"H6\tCtrl+6"), 
				_(u"H6 (<h6>...</h6>)"), 
				os.path.join (self.imagesDir, "text_heading_6.png"))
	

	def __addOtherTools (self):
		"""
		Добавить остальные инструменты
		"""
		self._addTool (self.pageToolsMenu, 
				"ID_IMAGE", 
				lambda event: self._turnText (u'<img src="', u'"/>'), 
				u'Image\tCtrl+M', 
				u'Image (<img src="..."/>', 
				os.path.join (self.imagesDir, "image.png"))

		self._addTool (self.pageToolsMenu, 
				"ID_LINK", 
				lambda event: self._turnText (u'<a href="">', u'</a>'), 
				_(u"Link\tCtrl+L"), 
				u'Link (<a href="...">...</a>)', 
				os.path.join (self.imagesDir, "link.png"))

		self._addTool (self.pageToolsMenu, 
				"ID_HORLINE", 
				lambda event: self._replaceText (u'<hr>'), 
				_(u"Horizontal line\tCtrl+H"), 
				_(u"Horizontal line (<hr>)"), 
				os.path.join (self.imagesDir, "text_horizontalrule.png"))


	def initGui (self, mainWindow):
		BaseTextPanel.initGui (self, mainWindow)

		self.pageToolsMenu = wx.Menu()
		
		self._addRenderTools()
		self.__addFontTools()
		self.__addAlignTools()
		self.__addHTools()
		self.__addTableTools()
		self.__addListTools()
		self.__addOtherTools()

		mainWindow.mainMenu.Insert (mainWindow.mainMenu.GetMenuCount() - 1, self.pageToolsMenu, _(u"H&tml"))
		mainWindow.mainToolbar.Realize()

		self._openDefaultPage()


	def generateHtml (self, page, path):
		if page.readonly and os.path.exists (path):
			# Если страница открыта только для чтения и html-файл уже существует, то покажем его
			return path

		text = HtmlImprover.run (page.content)
		text = re.sub ("\n<BR>\n(<li>)|(<LI>)", "\n<LI>", text)

		with open (path, "wb") as fp:
			fp.write (text.encode ("utf-8"))

		return path


	def removeGui (self):
		HtmlPanel.removeGui (self)
		self.mainWindow.mainMenu.Remove (self.mainWindow.mainMenu.GetMenuCount() - 2)
