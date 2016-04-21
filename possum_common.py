
from gi.repository import GLib
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
import json
import decorator


# currently not working as decorator changes the method name
#  it causes dbus to not recognize the method.
#  find a fix to print name of service method on invocation
def print_name_on_invoke(func):
    def wrapper(*args, **kwargs):
        print func.__name__
        return func(*args, **kwargs)
    return wrapper

# DBus does not allow nested dict/lists, so json is your friend!
def dict2json(arg_dict):
    return json.dumps(arg_dict)



@decorator.decorator
def log_dbus_invoke(f, *args, **kwargs):
    print "will call", f.__name__, "from", f.__module__
    print "With args:"
    print "\t", args
    print "\t", kwargs
    # print dir(f)
    # for attr in dir(f):
        # print attr,"--->", f.__getattribute__(attr)
    res = f(*args, **kwargs)
    print "Result:"
    print "\t", res
    return res

