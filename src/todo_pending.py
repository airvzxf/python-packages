#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# TODO: Move this function to other package which show the object's methods
def __show_methods(main_object=None, execute=True):
    if main_object is None:
        return

    print("{}".format(main_object))
    print("{}".format(dir(main_object)))

    if execute:
        for m in dir(main_object):
            try:
                print("object.{}(): {}".format(m, eval("main_object.{}()".format(m))))
            except AttributeError:
                pass
            except TypeError:
                pass
            except StopIteration:
                pass
