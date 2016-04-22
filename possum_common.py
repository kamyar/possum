
from gi.repository import GLib
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
import json
import decorator



# DBus does not allow nested dict/lists, so json is your friend!
def dict2json(arg_dict):
    return json.dumps(arg_dict)


# TODO(MAYBE): Add option to print args?
@decorator.decorator
def log_dbus_invoke(f, *args, **kwargs):
    print "will call", f.__name__, "from", f.__module__
    # print "With args:"
    # print "\t", args
    # print "\t", kwargs
    res = f(*args, **kwargs)
    # print "Result:"
    # print "\t", res
    return res

