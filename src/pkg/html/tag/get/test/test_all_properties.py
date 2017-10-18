#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Test case for get all properties inside of the HTML tag."""

import unittest

from src.pkg.html.tag.get.all_properties import all_properties


class TestPkgHtmlTagGetAllProperties(unittest.TestCase):
    """Tests for extract properties from the tags"""

    def test_when_tag_is_not_send_return_none(self):
        """Returns nil if we don't send the tag"""
        expected_property = all_properties()

        self.assertIsNone(expected_property)

    def test_extract_all_properties_with_one_simple_tag(self):
        """Extract properties for a simple html tag"""
        properties = all_properties(tag='div', text='''<div id="a" class='b'>Hello</div>''')
        first_tag = properties[0]

        self.assertEqual(first_tag[0][0], 'id')
        self.assertEqual(first_tag[0][1], 'a')

        self.assertEqual(first_tag[1][0], 'class')
        self.assertEqual(first_tag[1][1], 'b')

    def test_if_the_property_start_with_double_quotes_it_accept_single_quotes_and_inversely(self):
        """Extract properties for a simple html tag"""
        properties = all_properties(tag='div', text='''<div title="You're" data-type='She said "ok"'>Hello</div>''')
        first_tag = properties[0]

        self.assertEqual(first_tag[0][0], 'title')
        self.assertEqual(first_tag[0][1], "You're")

        self.assertEqual(first_tag[1][0], 'data-type')
        self.assertEqual(first_tag[1][1], 'She said "ok"')

    def test_if_the_properties_contains_the_greater_or_less_than_symbols(self):
        """Extract properties for a simple html tag"""
        properties = all_properties(tag='div', text='''<div title="a>b=c<d" data-type='a>b=c<d'>Hello</div>''')
        first_tag = properties[0]

        self.assertEqual(first_tag[0][0], 'title')
        self.assertEqual(first_tag[0][1], 'a>b=c<d')

        self.assertEqual(first_tag[1][0], 'data-type')
        self.assertEqual(first_tag[1][1], 'a>b=c<d')

    def test_extract_all_properties_with_one_simple_tag_spaces_between(self):
        """Extract properties for a simple html tag"""
        properties = all_properties(tag='div', text='''<div  	 data-type=" c  " title = "d">Hello</div>''')
        first_tag = properties[0]

        self.assertEqual(first_tag[0][0], 'data-type')
        self.assertEqual(first_tag[0][1], 'c')

        self.assertEqual(first_tag[1][0], 'title')
        self.assertEqual(first_tag[1][1], 'd')

    def test_extract_all_properties_with_one_simple_tag_but_not_trim_the_spaces(self):
        """Extract properties for a simple html tag"""
        properties = all_properties(tag='div', text='''<div class="    e     ">Hello</div>''', trim=False)
        first_tag = properties[0]

        self.assertEqual(first_tag[0][0], 'class')
        self.assertEqual(first_tag[0][1], '    e     ')

    def test_extract_all_properties_with_one_simple_tag_with_special_characters(self):
        """Extract properties for a simple html tag"""
        expected_string = '''!#$%&()*+,-./:;?<=>@[\]^_`{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑ'''
        expected_string += '''ÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚě'''
        expected_string += '''ĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤť'''
        expected_string += '''ŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſƀƁƂƃƄƅƆƇƈƉƊƋƌƍƎƏƐƑƒƓƔƕƖƗƘƙƚƛƜƝƞƟƠơƢƣƤƥƦƧƨƩƪƫƬƭƮƯ'''
        expected_string += '''ưƱƲƳƴƵƶƷƸƹƺƻƼƽƾƿǀǁǂǃǄǅǆǇǈǉǊǋǌǍǎǏǐǑǒǓǔǕǖǗǘǙǚǛǜǝǞǟǠǡǢǣǤǥǦǧǨǩǪǫǬǭǮǯǰǱǲǳǴǵǶǷǸǹ'''
        expected_string += '''ǺǻǼǽǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘșȚțȜȝȞȟȠȡȢȣȤȥȦȧȨȩȪȫȬȭȮȯȰȱȲȳȴȵȶȷȸȹȺȻȼȽȾȿɀɁɂɃɄ'''
        expected_string += '''ɅɆɇɈɉɊɋɌɍɎ'''

        properties = all_properties(tag='div', text='''<div data-type="''' + expected_string + '''">Hello</div>''')
        first_tag = properties[0]

        self.assertEqual(first_tag[0][0], 'data-type')
        self.assertEqual(first_tag[0][1], expected_string)

    def test_extract_all_properties_with_two_simple_tag(self):
        properties = all_properties(tag='div', text='''<div id="a" class='b'>H</div><div id='1' class="2">W</div>''')
        first_tag = properties[0]
        second_tag = properties[1]

        self.assertEqual(first_tag[0][0], 'id')
        self.assertEqual(first_tag[0][1], 'a')

        self.assertEqual(first_tag[1][0], 'class')
        self.assertEqual(first_tag[1][1], 'b')

        self.assertEqual(second_tag[0][0], 'id')
        self.assertEqual(second_tag[0][1], '1')

        self.assertEqual(second_tag[1][0], 'class')
        self.assertEqual(second_tag[1][1], '2')
