#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re


def all_from(tag=None, text="", ignore_case=True, get_only_content_inside=False):
    if tag is None:
        return

    return __search_html_tags(tag, text, ignore_case, get_only_content_inside)


def __search_html_tags(tag=None, text="", ignore_case=True, get_only_content_inside=False):
    if tag is None:
        return

    flags = re.RegexFlag.DOTALL
    if ignore_case:
        flags = flags | re.RegexFlag.IGNORECASE

    reg_ex_start_tag = re.compile(r"<{0}[^<]*?>".format(tag), flags)
    reg_ex_end_tag = re.compile(r"</{0}[^<]*?>".format(tag), flags)

    tag_matrix = {}

    opened = re.finditer(reg_ex_start_tag, text)
    for o in opened:
        print("Opened start/end at {}: {}".format(o.span(), o.group()))
        tag_matrix[o.start()] = {'value': 1, 'start_at': o.start(), 'end_at': o.end()}
    print("")

    closed = re.finditer(reg_ex_end_tag, text)
    for c in closed:
        print("Closed start/end at {}: {}".format(c.span(), c.group()))
        tag_matrix[c.start()] = {'value': -1, 'start_at': c.start(), 'end_at': c.end()}
    print("")

    tag_matrix = sorted(tag_matrix.items())
    for tm in tag_matrix:
        print("tag_matrix: ", tm)
    print("")

    tags_found = []
    text_star_at = 0
    tags_opened = 0
    is_a_new_tag = True
    for _, tag in tag_matrix:
        if tags_opened == 0 and is_a_new_tag:
            text_star_at = tag.get('start_at')
            is_a_new_tag = False

        tags_opened += tag.get('value')
        if tags_opened == 0:
            tags_found.append(text[text_star_at: tag.get('end_at')])
            is_a_new_tag = True

    print("text:\n", text)
    for tf in tags_found:
        print("tags_found:")
        print("-----------------------")
        print(tf)
        print("-----------------------\n")
    print("\n")

    return tags_found
