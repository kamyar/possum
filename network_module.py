from debinterface import interfaces

from possum_common import *

interfaces = interfaces.Interfaces()


interfaces.removeAdapterByName("eth0")

opts = {}
opts["name"] = "eth0"
opts["allow-hotplug"] = True
opts["address"] = "192.168.0.110"
opts["netmask"] = "255.255.255.0"
opts["source"] = "static"
opts["addrFam"] = "inet"
opts["gateway"] = "192.168.0.1"
opts["dns-nameservers"] = "8.8.8.8"


interfaces.addAdapter(opts, 0)


adapters = interfaces.adapters
for adapter in adapters:
    item = adapter.export()
    print(item)
    # print(adapter.display())
    # print adapter._ifAttributes

interfaces.writeInterfaces()


# another possiuble candidate is
#   https://github.com/rlisagor/pynetlinux
