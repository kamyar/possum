
from datetime import datetime

from possum_common import *



class PossumTime(dbus.service.Object):

        def __init__(self):
                bus_name = dbus.service.BusName('com.viero.possum', bus=dbus.SystemBus())
                dbus.service.Object.__init__(self, bus_name, '/time')

        @dbus.service.method('possum.time')
        def echo_test(self, echo_str):
                print "Got:", echo_str, "in PossumTime"
                return echo_str


        # @print_name_on_invoke
        @dbus.service.method('possum.time')
        def get_current_time(self):
                return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
