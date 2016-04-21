import subprocess
from datetime import datetime

from possum_common import *


class PossumSystem(PossumServiceBase):
    def __init__(self, bus_name):
        # bus_name = dbus.service.BusName('com.viero.possum', bus=dbus.SystemBus())
        dbus.service.Object.__init__(self, bus_name, '/system')

    @dbus.service.method('possum.system')
    def echo_test(self, echo_str):
        print "Got:", echo_str, "in PossumSystem"
        return echo_str


    @dbus.service.method('possum.system')
    def reboot(self, delay):
        # TODO: reboot in 'delay' seconds
        print "Gonna reboot bitchez in", delay

    # DEBUG: For test purposes, remove on production
    @dbus.service.method('possum.system')
    def run_cmd(self, strcmd):
        print "lol1", strcmd
        print subprocess.check_output(strcmd.split())
        return "Server Bus 1"
