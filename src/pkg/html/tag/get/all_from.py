#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Search all HTML content inside of specific tag.

Cases:
- If exists tags inside of the main tag it only return the principal tag.
Example: all_from(tag=div, text=html_code)
    HTML code: <div id ="id_1"><span>bla1</span><div id="id_2">bla2</div><hr/><div>
    Returns: ['<span>bla1</span><div id="id_2">bla2</div><hr/>']
- Otherwise if exist more than one outside tag it return all the next tags too.
Example: all_from(tag=div, text=html_code)
    HTML code: <div id ="id_1"><span>bla1</span></div><div id="id_2">bla2<hr/><div>
    Returns: ['<span>bla1</span>', 'bla2<hr/>']
"""

import re

from pkg.html.tag.get.helper_tag_validation import helper_tag_validation
from pkg.html.tag.regex.get_close import get_close as get_closed_tag
from pkg.html.tag.regex.get_open import get_open as get_opened_tag


def all_from(tag=None, text="", ignore_case=True, get_only_content_inside=False):
    """
    Search a specific tag in all HTML code and return a list of occurrences.

    :param tag: HTML tag like div, article, body, etc., looks like <div, <body.
    :param text: The HTML source code.
    :param ignore_case: If is true it should be search in lowercase and uppercase.
    :param get_only_content_inside: If is true return only the string after <div...> and before </div>
    otherwise return all included the tag and its properties.
    :return: List with the matched tags.
    """
    if tag is None:
        return

    flags = helper_tag_validation(ignore_case=ignore_case)

    regex_start_tag = re.compile(get_opened_tag(tag), flags)
    regex_end_tag = re.compile(get_closed_tag(tag), flags)

    tag_matrix = {}

    for o in re.finditer(regex_start_tag, text):
        tag_matrix[o.start()] = {'value': 1, 'start_at': o.start(), 'end_at': o.end()}

    for c in re.finditer(regex_end_tag, text):
        tag_matrix[c.start()] = {'value': -1, 'start_at': c.start(), 'end_at': c.end()}

    tag_matrix = sorted(tag_matrix.items())

    tags_found = []
    text_star_at = 0
    tags_opened = 0
    is_a_new_tag = True

    for _, tag in tag_matrix:
        if tags_opened == 0 and is_a_new_tag:
            if get_only_content_inside:
                text_star_at = tag.get('end_at')
            else:
                text_star_at = tag.get('start_at')
            is_a_new_tag = False

        tags_opened += tag.get('value')

        if tags_opened == 0:
            if get_only_content_inside:
                tags_found.append(text[text_star_at: tag.get('start_at')].rstrip())
            else:
                tags_found.append(text[text_star_at: tag.get('end_at')])
            is_a_new_tag = True

    return tags_found
