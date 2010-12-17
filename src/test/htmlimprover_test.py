#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest

from core.htmlimprover import HtmlImprover

class HtmlImproverTest (unittest.TestCase):
	def test1 (self):
		src = ur"""<H2>Attach links</H2><P>Attach:file.odt<BR><A HREF="__attach/file.odt">file.odt</A><BR><A HREF="__attach/file.odt">alternative text</A><BR><A HREF="__attach/file with spaces.pdf">file with spaces.pdf</A><P><H2>Images</H2>"""

		expectedResult = ur"""<HTML>
<HEAD>
<META HTTP-EQUIV='CONTENT-TYPE' CONTENT='TEXT/HTML; CHARSET=UTF-8'/>
</HEAD>
<BODY>
<P><H2>Attach links</H2></P>

<P>Attach:file.odt
<BR><A HREF="__attach/file.odt">file.odt</A>
<BR><A HREF="__attach/file.odt">alternative text</A>
<BR><A HREF="__attach/file with spaces.pdf">file with spaces.pdf</A></P>

<P><H2>Images</H2></P>
</BODY>
</HTML>"""

		result = HtmlImprover.run (src)
		self.assertEqual (expectedResult, result, result)
	

	def test2 (self):
		src = ur"""<UL><LI>Несортированный список. Элемент 1</LI><LI>Несортированный список. Элемент 2</LI><LI>Несортированный список. Элемент 3</LI><OL><LI>Вложенный сортированный список. Элемент 1</LI><LI>Вложенный сортированный список. Элемент 2</LI><LI>Вложенный сортированный список. Элемент 3</LI><LI>Вложенный сортированный список. Элемент 4</LI><UL><LI>Совсем вложенный сортированный список. Элемент 1</LI><LI>Совсем вложенный сортированный список. Элемент 2</LI></UL><LI>Вложенный сортированный список. Элемент 5</LI></OL><UL><LI>Вложенный несортированный список. Элемент 1</LI></UL></UL>"""

		expectedResult = ur"""<HTML>
<HEAD>
<META HTTP-EQUIV='CONTENT-TYPE' CONTENT='TEXT/HTML; CHARSET=UTF-8'/>
</HEAD>
<BODY>
<P>
<UL>
<LI>Несортированный список. Элемент 1</LI>
<LI>Несортированный список. Элемент 2</LI>
<LI>Несортированный список. Элемент 3</LI>
<OL>
<LI>Вложенный сортированный список. Элемент 1</LI>
<LI>Вложенный сортированный список. Элемент 2</LI>
<LI>Вложенный сортированный список. Элемент 3</LI>
<LI>Вложенный сортированный список. Элемент 4</LI>
<UL>
<LI>Совсем вложенный сортированный список. Элемент 1</LI>
<LI>Совсем вложенный сортированный список. Элемент 2</LI>
</UL>
<LI>Вложенный сортированный список. Элемент 5</LI>
</OL>
<UL>
<LI>Вложенный несортированный список. Элемент 1</LI>
</UL>
</UL></P>
</BODY>
</HTML>"""

		result = HtmlImprover.run (src)
		self.assertEqual (expectedResult, result, result)
	

	def test3 (self):
		src = ur"""qweqweqw qweqwe<BR>qwewqeqwe wqe<P>qweqweqw qwe qweqwe<PRE>
аап ываыв ываываыываы ыва ыва
ываыва выа выа

ываыв фывфв фывфывыф ыфв
вапвапввап вапвапвап

вапвапвап вапваапва</PRE><P>sdfsdf sdfsdf<BR>sdfsdf<BR>sdf sdfsdf sdf"""

		expectedResult = ur"""<HTML>
<HEAD>
<META HTTP-EQUIV='CONTENT-TYPE' CONTENT='TEXT/HTML; CHARSET=UTF-8'/>
</HEAD>
<BODY>
<P>qweqweqw qweqwe
<BR>qwewqeqwe wqe</P>

<P>qweqweqw qwe qweqwe
<PRE>
аап ываыв ываываыываы ыва ыва
ываыва выа выа

ываыв фывфв фывфывыф ыфв
вапвапввап вапвапвап

вапвапвап вапваапва</PRE></P>

<P>sdfsdf sdfsdf
<BR>sdfsdf
<BR>sdf sdfsdf sdf</P>
</BODY>
</HTML>"""

		result = HtmlImprover.run (src)
		self.assertEqual (expectedResult, result, result)
