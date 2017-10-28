#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Test case for get all properties inside of the HTML tag.
"""

from unittest import TestCase

from pkg.html.tag.get.all_properties import all_properties


class TestPkgHtmlTagGetAllProperties(TestCase):
    """
    Tests for extract properties from the tags.
    """

    def test_when_tag_is_none_return_empty(self):
        """
        Returns an emtpy list if we don't send the tag.
        """
        properties = all_properties()

        self.assertEqual([], properties)

    def test_extract_all_properties_with_one_simple_tag(self):
        """
        Extract properties for a simple html tag.
        """
        properties = all_properties(tag='div', text='''<div id="a" class='b'>Hello</div>''')

        compare_the_properties_from_the_html(self, first_tag=properties[0])

    def test_extract_all_properties_with_one_simple_tag_and_ignore_case(self):
        """
        Extract properties for a simple html tag.
        """
        properties = all_properties(tag='dIv', text='''<div id="a" class='b'>Hello</div>''', ignore_case=True)

        compare_the_properties_from_the_html(self, first_tag=properties[0])

    def test_extract_all_properties_with_one_simple_tag_and_not_ignore_case(self):
        """
        Return empty because the ignore case is false and the div tag have different case.
        """
        properties = all_properties(tag='dIv', text='''<div id="a" class='b'>Hello</div>''', ignore_case=False)

        self.assertEqual([], properties)

    def test_if_the_property_start_with_double_quotes_it_accept_single_quotes_and_inversely(self):
        """
        Extract properties for a simple html tag.
        """
        properties = all_properties(tag='div', text='''<div title="You're" data-type='She said "ok"'>Hello</div>''')
        first_tag = properties[0]

        expected_results = [('title', "You're"), ('data-type', 'She said "ok"')]

        self.assertEqual(expected_results, first_tag)

    def test_if_the_properties_contains_the_greater_or_less_than_symbols(self):
        """
        Extract properties for a simple html tag.
        """
        properties = all_properties(tag='div', text='''<div title="a>b=c<d" data-type='a>b=c<d'>Hello</div>''')
        first_tag = properties[0]

        expected_results = [('title', 'a>b=c<d'), ('data-type', 'a>b=c<d')]

        self.assertEqual(expected_results, first_tag)

    def test_extract_all_properties_with_one_simple_tag_spaces_between(self):
        """
        Extract properties for a simple html tag.
        """
        properties = all_properties(tag='div', text='''<div  	 id=" a  " class = "b">Hello</div>''')

        compare_the_properties_from_the_html(self, first_tag=properties[0])

    def test_extract_all_properties_with_one_simple_tag_but_not_trim_the_spaces(self):
        """
        Extract properties for a simple html tag.
        """
        properties = all_properties(tag='div', text='''<div class="    e     ">Hello</div>''', trim=False)
        first_tag = properties[0]

        expected_results = [('class', '    e     ')]

        self.assertEqual(expected_results, first_tag)

    def test_extract_all_properties_with_one_simple_tag_with_special_characters(self):
        """
        Extract properties for a simple html tag.
        """
        expected_string = '''!#$%&()*+,-./:;?<=>@[\]^_`{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑ'''
        expected_string += '''ÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚě'''
        expected_string += '''ĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤť'''
        expected_string += '''ŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſƀƁƂƃƄƅƆƇƈƉƊƋƌƍƎƏƐƑƒƓƔƕƖƗƘƙƚƛƜƝƞƟƠơƢƣƤƥƦƧƨƩƪƫƬƭƮƯ'''
        expected_string += '''ưƱƲƳƴƵƶƷƸƹƺƻƼƽƾƿǀǁǂǃǄǅǆǇǈǉǊǋǌǍǎǏǐǑǒǓǔǕǖǗǘǙǚǛǜǝǞǟǠǡǢǣǤǥǦǧǨǩǪǫǬǭǮǯǰǱǲǳǴǵǶǷǸǹ'''
        expected_string += '''ǺǻǼǽǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘșȚțȜȝȞȟȠȡȢȣȤȥȦȧȨȩȪȫȬȭȮȯȰȱȲȳȴȵȶȷȸȹȺȻȼȽȾȿɀɁɂɃɄ'''
        expected_string += '''ɅɆɇɈɉɊɋɌɍɎ'''

        properties = all_properties(tag='div', text='''<div data-type="''' + expected_string + '''">Hello</div>''')
        first_tag = properties[0]

        expected_results = [('data-type', expected_string)]

        self.assertEqual(expected_results, first_tag)

    def test_extract_all_properties_with_two_simple_tag(self):
        """
        Extract properties for two html tag.
        """
        properties = all_properties(tag='div', text='''<div id="a" class='b'>H</div><div id='1' class="2">W</div>''')

        compare_the_properties_from_the_html(self, first_tag=properties[0], second_tag=properties[1])


def compare_the_properties_from_the_html(self, first_tag=None, second_tag=None):
    """
    Compare the id and class properties from specific HTML.
    <div id="a" class='b'>Hello</div>
    or from
    <div id="a" class='b'>H</div><div id='1' class="2">W</div>

    :param self: The test actor
    :param first_tag: Get the properties form the first tag
    :param second_tag: Get the properties form the second tag
    """
    if first_tag:
        self.assertEqual([('id', 'a'), ('class', 'b')], first_tag)

    if second_tag:
        self.assertEqual([('id', '1'), ('class', '2')], second_tag)
