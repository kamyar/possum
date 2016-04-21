
from gi.repository import GLib
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
import json

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


class PossumServiceBase(dbus.service.Object):
    def __init__(self):
        pass


