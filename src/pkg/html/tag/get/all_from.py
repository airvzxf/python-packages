#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

from src.pkg.html.tag.regex.get_open import get_open as get_opened_tag
from src.pkg.html.tag.regex.get_close import get_close as get_closed_tag


def all_from(tag=None, text="", ignore_case=True, get_only_content_inside=False):
    if tag is None:
        return

    return __search_html_tags(tag, text, ignore_case, get_only_content_inside)


def __search_html_tags(tag=None, text="", ignore_case=True, get_content_inside=False):
    if tag is None:
        return

    flags = re.RegexFlag.DOTALL

    if ignore_case:
        flags = flags | re.RegexFlag.IGNORECASE

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
            if get_content_inside:
                text_star_at = tag.get('end_at')
            else:
                text_star_at = tag.get('start_at')
            is_a_new_tag = False

        tags_opened += tag.get('value')

        if tags_opened == 0:
            if get_content_inside:
                tags_found.append(text[text_star_at: tag.get('start_at')].rstrip())
            else:
                tags_found.append(text[text_star_at: tag.get('end_at')])
            is_a_new_tag = True

    return tags_found
