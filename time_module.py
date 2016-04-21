
from datetime import datetime

from possum_common import *


class PossumTime(dbus.service.Object):
    def __init__(self, bus_name):
        # bus_name = dbus.service.BusName('com.viero.possum', bus=dbus.SystemBus())
        dbus.service.Object.__init__(self, bus_name, '/time')

    @dbus.service.method('possum.time')
    @log_dbus_invoke
    def echo_test(self, echo_dict):
        print "PossumTime:"
        print "\tEcho Got:"
        # print echo_str
        for key in echo_dict:
            print "\t\t", key, echo_dict[key]
        return echo_dict

    # # @print_name_on_invoke
    # @dbus.service.method('possum.time')
    # def get_current_time(self):
    #     return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @dbus.service.method('possum.time')
    def set_hw_time(self, timestamp):
        print(timestamp)
        return True

    @dbus.service.method('possum.time')
    def set_sw_time(self, timestamp):
        print(timestamp)
        return True

    @dbus.service.method('possum.time')
    def get_hw_time(self):
        #get hardware time
        return -1

    @dbus.service.method('possum.time')
    def get_sw_time(self):
        # get software time
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
