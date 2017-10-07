#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def get_properties():

    return r"(\S+)=[\"']?((?:.(?![\"']?\s+(?:\S+)=|[>\"']))+.)[\"']?"
