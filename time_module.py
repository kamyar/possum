
from datetime import datetime

from possum_common import *


class PossumTime(dbus.service.Object):
    def __init__(self, bus_name):
        dbus.service.Object.__init__(self, bus_name, '/time')

    @dbus.service.method('possum.time')
    @log_dbus_invoke
    def echo_test(self, echo_dict):
        for key in echo_dict:
            print "\t\t", key, echo_dict[key]
        return echo_dict

    @dbus.service.method('possum.time')
    @log_dbus_invoke
    def set_hw_time(self, timestamp):
        print(timestamp)
        return True

    @dbus.service.method('possum.time')
    @log_dbus_invoke
    def set_sw_time(self, timestamp):
        print(timestamp)
        return True

    @dbus.service.method('possum.time')
    @log_dbus_invoke
    def get_hw_time(self):
        # TODO: get hardware time
        return -1

    @dbus.service.method('possum.time')
    @log_dbus_invoke
    def get_sw_time(self):
        # TODO: get software time
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
