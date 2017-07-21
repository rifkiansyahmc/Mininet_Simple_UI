from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel


class PairTopo(Topo):
    "4 switches in the form of a rectangle"
    def build(self):
        cSwitch = 4
        for i in range(cSwitch):
            switch = self.addSwitch('s%s' % (i+1))
        self.addLink('s2','s3')
        self.addLink('s4','s1')

        cHost = 4
        for h in range(cHost): #add as many hosts
            host = self.addHost('h%s' % (h+1))

        self.addLink('h1','s1')
        self.addLink('h2','s2')
        self.addLink('h3','s3')
        self.addLink('h4','s4')
