### Possum
===

#### Possum - Privileged Upstart Service for System manipulation

**Possum** - _[latin(/ˈpɒsəm/); Omnipotent, Potent, Capable]_

Possum runs as a service as superuser and exposes some privilaged operations over DBus. It is developped to expose only the minimum amount of privileged functionality in a secure way.


#### USAGE
1. install decorator
    - `pip install decorator` (to decorate dbus 'method' for logging purposes)
1. install debinterface
    - `git clone https://github.com/dggreenbaum/debinterface.git` (high-level access to /etc/network/interfaces)
3. move dbus config for possum from conf/com.viero.possum.conf to /etc/dbus-1/system.d/com.viero.possum.conf (change path inside accordingly, this is to run possum as a service)
4. reload dbus config
    - `sudo /etc/init.d/dbus restart`
5. move upstart config for possum from conf/possum.conf to /etc/init/possum.conf (change path inside accordingly, this is to run possum as a service)
6. reload upstart config
    - `sudo initctl load-configuration`   (else Upstart will not begin managing possum)
7. make sure possum is running
    - `sudo service possum start`



#### TODO
- Help Move debinterface to PyPI
- Move Possum to PyPI and/or make it installable from ubuntu apt
- Test

#### CONTRIBUTE
- Contributions and improvements are most welcome, just send the pull request and explain your changes briefly. :)
