#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Print all the methods, and also the available methods in a specific object."""


def show_available(main_object=None, print_all=True, print_available=True):
    """Show available methods for an object which is debugging.

    This function NOT return any value but it print in the console the methods

    :param main_object: Object with is debugging
    :param print_all: Print all methods with dir(object)
    :param print_available: Try to execute all methods for object for example: object.reverse()
    :return: None
    """
    if main_object is None:
        return

    print("{}".format(main_object))

    if print_all:
        print("{}".format(dir(main_object)))

    if print_available:
        for m in dir(main_object):
            if m == "__dir__":
                continue

            try:
                print("object.{}(): {}".format(m, eval("main_object.{}()".format(m))))
            except AttributeError:
                pass
            except IndexError:
                pass
            except TypeError:
                pass
            except StopIteration:
                pass
