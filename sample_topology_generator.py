#!/usr/bin/python

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.topo import Topo
from mininet.util import dumpNodeConnections


def create_topology(switch, hosts):
    setLogLevel('info')
    topo = Topo()
    switch = topo.addSwitch(switch)

    for (hostname, opts) in hosts:
        host = topo.addHost(hostname, **opts)
        topo.addLink(host, switch)

    network = Mininet(topo, controller=None)
    network.start()
    print "*** Dumping host connections"
    dumpNodeConnections(network.hosts)
    CLI(network)
    network.stop()


create_topology(
    [
        'topic',
        [
            [
                'user1',
                {
                    'ip': '10.0.0.1/24',
                    'mac': '00:10:00:00:aa:01'
                }
            ],
            [
                'user2',
                {
                    'ip': '10.0.0.2/24',
                    'mac': '00:10:00:00:aa:02'
                }
            ]
        ],

    ]
)
