import subprocess
from datetime import datetime

from possum_common import *


class PossumSystem(dbus.service.Object):
    def __init__(self, bus_name):
        dbus.service.Object.__init__(self, bus_name, '/system')

    @dbus.service.method('possum.system')
    @log_dbus_invoke
    def echo_test(self, echo_str):
        print echo_str
        return echo_str


    @dbus.service.method('possum.system')
    @log_dbus_invoke
    def reboot(self, delay):
        # TODO: reboot in 'delay' seconds
        print "Rebooting System in %s seconds"%(delay,)
        # TODO: fix delay thing, find a solution
        print subprocess.check_output(["shutdown", "-r", "now"])

    # DEBUG: For test purposes, remove on production, easy privilege escalation point
    @dbus.service.method('possum.system')
    @log_dbus_invoke
    def run_cmd(self, strcmd):
        print subprocess.check_output(strcmd.split())
        return "Server Bus 1"
