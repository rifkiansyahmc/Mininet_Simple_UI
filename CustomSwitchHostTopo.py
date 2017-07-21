from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel


class CustomSwitchHostTopo(Topo):
    "x switch connected to n hosts."
    def build(self, n=2):
        countSwitch = input('Enter number of switch: ')
        for i in range(countSwitch):
            switch = self.addSwitch('s%s' % (i+1)) #add switch #for the xth switch
            countHost = input('Enter number of host for switch %s: ' %(i+1))
            for h in range(countHost): #add as many hosts
                host = self.addHost('h%ss%s' % (h+1, i+1))
                self.addLink(host, switch)
        # Python's range(N) generates 0..N-1
        for j in range(countSwitch-1):
            self.addLink('s%s' %(j+1),'s%s' % (j+2))
