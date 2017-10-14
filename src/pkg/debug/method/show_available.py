#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Print all the methods, and also the available methods in a specific object."""


# TODO: Create Unit Test and DocStrings.
def show_available(main_object=None, show_all=True, show_available=True):
    if main_object is None:
        return

    print("{}".format(main_object))

    if show_all:
        print("{}".format(dir(main_object)))

    if show_available:
        for m in dir(main_object):
            try:
                print("object.{}(): {}".format(m, eval("main_object.{}()".format(m))))
            except AttributeError:
                pass
            except TypeError:
                pass
            except StopIteration:
                pass
