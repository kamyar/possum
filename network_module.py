from debinterface import interfaces

from possum_common import *




class PossumNetwork(dbus.service.Object):
    def __init__(self, bus_name):
        dbus.service.Object.__init__(self, bus_name, '/network')


    @dbus.service.method('possum.network')
    def echo_test(self, echo_dict):
        print "PossumTime:"
        print "\tEcho Got:"
        # print echo_str
        for key in echo_dict:
            print "\t\t", key, echo_dict[key]
        return echo_dict


    @dbus.service.method('possum.network')
    @log_dbus_invoke
    def get_ifaces(self):
        # TODO: Get list of ifaces
        print "Gonna return ifaces list"
        res = []

        # Export each interface adapter object to a dict
        for iface in interfaces.Interfaces().adapters:
            res.append(iface.export())

        return dict2json(res)


    @dbus.service.method('possum.network')
    def get_iface_info(self, iface_name):
        # TODO: Get iface info
        print "Gonna return iface info for", iface_name
        return "lol"

    # INFO: If there is a prob;em with sending python dictionaries,
    #       the iface info can be sent as json and deserialized to dict
    @dbus.service.method('possum.network')
    def set_iface_info(self, iface_info_dict):
        print subprocess.check_output(strcmd.split())
        return "Server Bus 1"


# interfaces = interfaces.Interfaces()
#
#
# interfaces.removeAdapterByName("eth0")
#
# opts = {}
# opts["name"] = "eth0"
# opts["allow-hotplug"] = True
# opts["address"] = "192.168.0.110"
# opts["netmask"] = "255.255.255.0"
# opts["source"] = "static"
# opts["addrFam"] = "inet"
# opts["gateway"] = "192.168.0.1"
# opts["dns-nameservers"] = "8.8.8.8"
#
#
# interfaces.addAdapter(opts, 0)
#
#
# adapters = interfaces.adapters
# for adapter in adapters:
#     item = adapter.export()
#     print(item)
#     # print(adapter.display())
#     # print adapter._ifAttributes
#
# interfaces.writeInterfaces()


# another possiuble candidate is
#   https://github.com/rlisagor/pynetlinux
