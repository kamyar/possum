#!/usr/bin/env python3

import dbus

bus = dbus.SystemBus()
timebus = bus.get_object("com.viero.possum", "/time")
systembus = bus.get_object("com.viero.possum", "/system")
networkbus = bus.get_object("com.viero.possum", "/network")


time_iface = dbus.Interface(timebus, "possum.time")
system_iface = dbus.Interface(systembus, "possum.system")
network_iface = dbus.Interface(networkbus, "possum.network")

# interface2 = dbus.Interface(system, "org.me.test2")

# Call the methods using the interface
# print interface1.session_bus_message1(raw_input())
# print time_iface.get_sw_time()
echo_test_dict = {}
echo_test_dict["this_is_foo"] = "with value bar"
echo_test_dict["Sometimes_i_baz"] = "I don not expect a quz"
print time_iface.echo_test(echo_test_dict)
# print system_iface.echo_test(raw_input())
# print system_iface.run_cmd(raw_input())
print network_iface.get_ifaces()
# print network_iface.echo_test(echo_test_dict)
# print(interface2.system_bus_message2())
# print(interface2.system_bus_strings("Hello", "world")
