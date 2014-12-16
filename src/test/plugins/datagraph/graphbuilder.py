# -*- coding: UTF-8 -*-

import unittest

from outwiker.core.pluginsloader import PluginsLoader
from outwiker.core.application import Application


class GraphBuilderTest (unittest.TestCase):
    def setUp(self):
        dirlist = [u"../plugins/datagraph"]

        self.loader = PluginsLoader(Application)
        self.loader.load (dirlist)
        self.GraphBuilder = self.loader[u'DataGraph'].GraphBuilder

        self._defaultWidth = 700
        self._defaultHeight = 400


    def tearDown (self):
        self.loader.clear()


    def testEmpty (self):
        params = {}
        content = u''
        page = None

        builder = self.GraphBuilder(params, content, page)
        graph = builder.graph

        self.assertEqual (graph.getProperty (u'width', 0), self._defaultWidth)
        self.assertEqual (graph.getProperty (u'height', 0), self._defaultHeight)

        self.assertEqual (graph.getProperty (u'Width', 0), self._defaultWidth)
        self.assertEqual (graph.getProperty (u'HEIGHT', 0), self._defaultHeight)

        self.assertIsNotNone (graph.getObject (u'pane'))
        self.assertIsNotNone (graph.getObject (u'PANE'))
        self.assertIsNotNone (graph.getObject (u'pane1'))
        self.assertIsNotNone (graph.getObject (u'PANE1'))

        self.assertIsNone (graph.getObject (u'curve'))
        self.assertIsNone (graph.getObject (u'curve1'))


    def testGraphProperties (self):
        params = {
            u'width': 100,
            u'height': 150,

            u'pane.title': u'Заголовок графика',

            # invalid values
            u'pane': u'Бла-бла-бла',
            u'abyrvalg': u'Абырвалг',
            u'Абырвалг': u'Главрыба',
            u'qwerty.qw': 42,
            u'qwerty.qw.sss': 42,
        }
        content = u''
        page = None

        builder = self.GraphBuilder (params, content, page)
        graph = builder.graph
        pane = graph.getObject (u'pane')

        self.assertIsNotNone (pane)
        self.assertIsNotNone (graph.getObject(u'pane1'))

        self.assertEqual (graph.getProperty (u'width', 0), 100)
        self.assertEqual (graph.getProperty (u'height', 0), 150)

        self.assertEqual (pane.getProperty (u'title', None), u'Заголовок графика')

        self.assertEqual (graph.getProperty (u'abyrvalg', None), u'Абырвалг')
        self.assertEqual (graph.getProperty (u'Абырвалг', None), u'Главрыба')


    def testCurvesCount_01 (self):
        params = {
            'curve': u'Абырвалг',
            'curve1': u'Абырвалг',
            'curve23sdf': u''
        }
        content = u''
        page = None

        builder = self.GraphBuilder (params, content, page)
        graph = builder.graph

        self.assertIsNone (graph.getObject (u'curve'))
        self.assertIsNone (graph.getObject (u'curve1'))
        self.assertIsNone (graph.getObject (u'curve23sdf'))


    def testCurvesCount_02 (self):
        params = {
            'curve.property': u'Абырвалг',
        }
        content = u''
        page = None

        builder = self.GraphBuilder (params, content, page)
        graph = builder.graph

        self.assertIsNotNone (graph.getObject (u'curve'))
        self.assertIsNotNone (graph.getObject (u'curve1'))


    def testCurvesCount_03 (self):
        params = {
            'curve1.property': u'Абырвалг',
        }
        content = u''
        page = None

        builder = self.GraphBuilder (params, content, page)
        graph = builder.graph

        self.assertIsNotNone (graph.getObject (u'curve'))
        self.assertIsNotNone (graph.getObject (u'curve1'))


    def testCurvesCount_04 (self):
        params = {
            'curve2.property': u'Абырвалг',
        }
        content = u''
        page = None

        builder = self.GraphBuilder (params, content, page)
        graph = builder.graph

        self.assertIsNone (graph.getObject (u'curve'))
        self.assertIsNone (graph.getObject (u'curve1'))
        self.assertIsNotNone (graph.getObject (u'curve2'))


    def testCurveProperties_01 (self):
        params = {
            'curve.property': u'Абырвалг',
        }
        content = u''
        page = None

        builder = self.GraphBuilder (params, content, page)
        graph = builder.graph
        curve = graph.getObject (u'curve')
        curve1 = graph.getObject (u'curve1')

        self.assertEqual (curve.getProperty (u'property', None), u'Абырвалг')
        self.assertEqual (curve1.getProperty (u'property', None), u'Абырвалг')
