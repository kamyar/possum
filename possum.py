#!/usr/bin/env python


import subprocess

from possum_common import *



# import network_module
from time_module import PossumTime
from system_module import PossumSystem


class Possum_DBus(dbus.service.Object):

        def __init__(self):
                bus_name = dbus.service.BusName('com.viero.possum', bus=dbus.SystemBus())
                dbus.service.Object.__init__(self, bus_name, '/main')

        # Interface and Method
        @dbus.service.method('org.me.test1')
        def session_bus_message1(self, strcmd):
                print "lol1", strcmd
                print subprocess.check_output(strcmd.split())
                return "Server Bus 1"


        # Different Interface and different Method
        # The method must not have not the same name as the first
        @dbus.service.method('org.me.test2')
        def session_bus_message2(self):
                print "lol2"
                return "Server Bus 2"


        # Method with arguments
        @dbus.service.method('org.me.test2')
        def session_bus_strings(self, string1, string2):
                return string1 + " " + string2


# class Possum_DBus2(dbus.service.Object):

#         def __init__(self):
#                 bus_name = dbus.service.BusName('com.viero.possum', bus=dbus.SystemBus())
#                 dbus.service.Object.__init__(self, bus_name, '/two')
#         # Interface and Method
#         @dbus.service.method('org.me.test1')
#         def session_bus_message1(self, strcmd):
#                 print "dbus2", strcmd
#                 print subprocess.check_output(strcmd.split())
#                 return "Server Bus 1"


DBusGMainLoop(set_as_default=True)
# dbus_service = Possum_DBus()
# Possum_DBus2()

PossumTime()
PossumSystem()


try:
    GLib.MainLoop().run()
except KeyboardInterrupt:
    print("\nPossum will exit...")
    GLib.MainLoop().quit()