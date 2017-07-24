#!/usr/bin/env python

from Tkinter import *
from tkSimpleDialog import *
from tkMessageBox import *
import tkSimpleDialog
import tkMessageBox
from CustomSwitchHostTopo import CustomSwitchHostTopo
from RectangleTopo import RectangleTopo
from mininet.net import Mininet
from mininet.node import OVSController
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.topolib import TreeTopo
from mininet.topolib import TorusTopo
from mininet.topo import SingleSwitchReversedTopo
from mininet.topo import MinimalTopo
from mininet.util import dumpNodeConnections
from mininet.clean import Cleanup
from mininet.link import TCIntf
from mininet.link import Intf
from mininet.link import Link

sdk = tkSimpleDialog
msg = tkMessageBox

class App:


    def __init__(self, master):
        #main screen goes here
        w = Label(root, text="Choose from the available topology. Right click each for details")
        w.pack()
        frame = Frame(master)
        frame.pack()

        quitButton = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        quitButton.pack(side=LEFT)

        minimalButton = Button(frame, text="Minimal", command=self.minimal_topo)
        minimalButton.pack(side=LEFT)
        linearButton = Button(frame, text="Linear", command=self.linear_topo)
        linearButton.pack(side=LEFT)
        treeButton = Button(frame, text="Tree", command=self.tree_topo)
        treeButton.pack(side=LEFT)
        torusButton = Button(frame, text="Torus", command=self.torus_topo)
        torusButton.pack(side=LEFT)
        reversedButton = Button(frame, text="Reversed", command=self.reversed_switch)
        reversedButton.pack(side=LEFT)
        tutorialButton = Button(frame, text="Tutorials", command=self.tutorial)
        tutorialButton.pack(side=LEFT)

        def left_quit(event):
            frame.quit
        def right_quit(event):
            msg.showinfo("Help","Quit the program.")
        quitButton.bind('<Button-1>', left_quit)   
        quitButton.bind('<Button-3>', right_quit)  

        def left_minimal(event):
            self.minimal_topo
        def right_minimal(event):
            msg.showinfo("Help","Minimal topology is a topology with two host connected to one switch.")
        minimalButton.bind('<Button-1>', left_minimal)   
        minimalButton.bind('<Button-3>', right_minimal)  

        def left_tree(event):
            self.tree_topo
        def right_tree(event):
            msg.showinfo("Help","Tree topology is a topology where each level branches x number of node until y depth.")
        treeButton.bind('<Button-1>', left_tree)   
        treeButton.bind('<Button-3>', right_tree)  

        def left_linear(event):
            self.linear_topo
        def right_linear(event):
            msg.showinfo("Help","Linear topology is a topology with one host connected to each switch, which forms a line.")
        linearButton.bind('<Button-1>', left_linear)   
        linearButton.bind('<Button-3>', right_linear)  

        def left_torus(event):
            self.torus_topo
        def right_torus(event):
            msg.showinfo("Help","Torus topology is a topology where one host connected to three other hosts in a rectangle shape.")
        torusButton.bind('<Button-1>', left_torus)   
        torusButton.bind('<Button-3>', right_torus)  

        def left_reversed(event):
            self.reversed_switch
        def right_reversed(event):
            msg.showinfo("Help","Reversed topology is a topology where the lowest numbered host connects to the highest port.")
        reversedButton.bind('<Button-1>', left_reversed)   
        reversedButton.bind('<Button-3>', right_reversed)  
        
        def left_tutorial(event):
            self.tutorial
        def right_tutorial(event):
            msg.showinfo("Help","This button shows available tutorials or testing scenarios.")
        tutorialButton.bind('<Button-1>', left_tutorial)   
        tutorialButton.bind('<Button-3>', right_tutorial)  

        #topologies goes here

    def minimal_topo(self):
        setLogLevel('info')
        minimal = MinimalTopo()
        net = Mininet(topo=minimal)
        net.start()
        print "Dumping host connections"
        dumpNodeConnections(net.hosts)
        option = self.options(net)
        net.stop()

    def linear_topo(self):
        setLogLevel('info')
        topo = CustomSwitchHostTopo(n=4)
        net = Mininet(topo=topo, controller=OVSController)
        net.start()
        print "Dumping host connections"
        dumpNodeConnections(net.hosts)
        option = self.options(net)
        net.stop()

    def tree_topo(self):
        setLogLevel('info')
        cDepth = input('Enter number of depth: ')
        cFanout = input('Enter number of fanout: ')
        treecustom = TreeTopo(depth=cDepth,fanout=cFanout)
        net = Mininet(topo=treecustom)
        net.start()
        print "Dumping host connections"
        dumpNodeConnections(net.hosts)
        option = self.options(net)
        net.stop()

    def torus_topo(self):
        setLogLevel('info')
        xCount = input('Enter number of x-side nodes: ')
        yCount = input('Enter number of y-side nodes: ')
        toruscustom = TorusTopo(x = xCount, y = yCount)
        net = Mininet(topo=toruscustom, controller=OVSController)
        net.start()
        print "Dumping host connections"
        dumpNodeConnections(net.hosts)
        option = self.options(net)
        net.stop()

    def reversed_switch(self):
        setLogLevel('info')
        hCount = input('Enter number of hosts: ')
        ReverseSingle = SingleSwitchReversedTopo(k=hCount)
        net = Mininet(topo=ReverseSingle)
        net.start()
        print "Dumping host connections"
        dumpNodeConnections(net.hosts)
        option = self.options(net)
        net.stop()

    def rectangle_topo(self):
        setLogLevel('info')
        rect_topo = RectangleTopo()
        net = Mininet(topo=rect_topo, controller=OVSController)
        net.start()
        print "Dumping host connections"
        dumpNodeConnections(net.hosts)
        option = self.options()
        net.stop()

    def twinpair_topo(self):
        setLogLevel('info')
        pair_topo = PairTopo()
        net = Mininet(topo=rect_topo, controller=OVSController)
        net.start()
        print "Dumping host connections"
        dumpNodeConnections(net.hosts)
        option = self.options()
        net.stop()

        #tutorial menu goes here

    def tutorial(self):
        topt = Toplevel()
        topt.title("SDN Tutorial Menu")

        self.button = Button(
            topt, text="QUIT", fg="red", command=topt.quit
            )
        self.button.pack(side=LEFT)

        self.tutor0_Button = Button(topt, text="Tutorial 0", command=self.tutorial_0)
        self.tutor0_Button.pack(side=LEFT)
        self.tutor1_Button = Button(topt, text="Tutorial 1", command=self.tutorial_1)
        self.tutor1_Button.pack(side=LEFT)
        self.tutor2_Button = Button(topt, text="Tutorial 2", command=self.tutorial_2)
        self.tutor2_Button.pack(side=LEFT)
        self.tutor3_Button = Button(topt, text="Tutorial 3", command=self.tutorial_3)
        self.tutor3_Button.pack(side=LEFT)
        self.tutor4_Button = Button(topt, text="Tutorial 4", command=self.tutorial_4)
        self.tutor4_Button.pack(side=LEFT)

        #option menu goes here

    def options(self, net):
        topopt = Toplevel()
        topopt.title("Mininet Toolbox. Right click each button for info")

        quitButton = Button(
            topopt, text="QUIT", fg="red", command=topopt.quit)
        quitButton.grid(row=10, column=5)


        pingButton = Button(topopt, text="Ping", width=10)
        pingButton.grid(row=0)
        pingpairButton = Button(topopt, text="Ping Pair", width=10)
        pingpairButton.grid(row=0,column=1)
        pingpairfullButton = Button(topopt, text="Ping Pair Full", width=10)
        pingpairfullButton.grid(row=0, column=2)
        pingfullButton = Button(topopt, text="Ping Full", width=10)
        pingfullButton.grid(row=0,column=3)
        pingAllButton = Button(topopt, text="Ping All", width=10)
        pingAllButton.grid(row=0,column=4)
        pingAllfullButton = Button(topopt, text="Ping All Full", width=10)
        pingAllfullButton.grid(row=0,column=5)
        bwButton = Button(topopt, text="Bandwidth", width=10)
        bwButton.grid(row=1)
        delayButton = Button(topopt, text="Delay", width=10)
        delayButton.grid(row=2)
        jitterButton = Button(topopt, text="Jitter", width=10)
        jitterButton.grid(row=3)
        lossButton = Button(topopt, text="Loss",width=10)
        lossButton.grid(row=4)
        IPButton = Button(topopt, text="Set IP",width=10)
        IPButton.grid(row=1, column=1)
        MACButton = Button(topopt, text="Set MAC",width=10)
        MACButton.grid(row=2, column=1)
        linkButton = Button(topopt, text="Up/Down Link",width=10)
        linkButton.grid(row=3, column=1)
        hostButton = Button(topopt, text="Add Host",width=10)
        hostButton.grid(row=1, column=3)
        switchButton = Button(topopt, text="Add Switch",width=10)
        switchButton.grid(row=1, column=2)
        iperfButton = Button(topopt, text="Do iperf",width=10)
        iperfButton.grid(row=2, column=2)
        iperfudpButton = Button(topopt, text="Do iperfudp",width=10)
        iperfudpButton.grid(row=3, column=2)
        nodeButton = Button(topopt, text="Node List", width=10)
        nodeButton.grid(row=2, column=3)
        dumpButton = Button(topopt, text="Dump Nodes", width=10)
        dumpButton.grid(row=3, column=3)
        addnatButton = Button(topopt, text="Add NAT", width=10)
        addnatButton.grid(row=1, column=4)
        addctrlButton = Button(topopt, text="Add Controller")
        addctrlButton.grid(row=2, column=4)
        addlinkButton = Button(topopt, text="Add Link", width=10)
        addlinkButton.grid(row=3, column=4)
        dellinkButton = Button(topopt, text="Delete Link", width=10)
        dellinkButton.grid(row=4, column=4)
        stopswitchButton = Button(topopt, text="Stop Switch", width=10)
        stopswitchButton.grid(row=5, column=4)
        delnodeButton = Button(topopt, text="Delete Node", width=10)
        delnodeButton.grid(row=6, column=4)

        cliButton = Button(topopt, text="CLI", fg = "blue", width=5,command=lambda: CLI(net))
        cliButton.grid(row=10, column=0)

        #CLICK EVENTS GOES HERE.
        def left_ping(event):
            self.ping_node(net)
        def right_ping(event):
            msg.showinfo("Help","Ping button is used to test connection to another host.")
        pingButton.bind('<Button-1>', left_ping)   
        pingButton.bind('<Button-3>', right_ping)  

        def left_ping_pair(event):
            self.ping_pair(net)
        def right_ping_pair(event):
            msg.showinfo("Help","Ping pair button is used to test connection between the first two hosts.")
        pingpairButton.bind('<Button-1>', left_ping_pair)   
        pingpairButton.bind('<Button-3>', right_ping_pair)  
        
        def left_ping_pair_full(event):
            self.ping_pair_full(net)
        def right_ping_pair_full(event):
            msg.showinfo("Help","Ping pair full button is used to test connection between the first two hosts with details.")
        pingpairfullButton.bind('<Button-1>', left_ping_pair_full)   
        pingpairfullButton.bind('<Button-3>', right_ping_pair_full)  

        def left_ping_full(event):
            self.ping_full(net)
        def right_ping_full(event):
            msg.showinfo("Help","Ping pair full button is used to test connection between two hosts with details.")
        pingfullButton.bind('<Button-1>', left_ping_full)   
        pingfullButton.bind('<Button-3>', right_ping_full)  

        def left_ping_all(event):
            self.ping_all(net)
        def right_ping_all(event):
            msg.showinfo("Help","Ping all button is used to test connection between all connected hosts.")
        pingAllButton.bind('<Button-1>', left_ping_all)   
        pingAllButton.bind('<Button-3>', right_ping_all)  

        def left_ping_all_full(event):
            self.ping_all_full(net)
        def right_ping_all_full(event):
            msg.showinfo("Help","Ping all full button is used to test connection between all connected hosts with details.")
        pingAllfullButton.bind('<Button-1>', left_ping_all_full)   
        pingAllfullButton.bind('<Button-3>', right_ping_all_full)  

        def left_bw(event):
            self.set_bandwidth(net)
        def right_bw(event):
            msg.showinfo("Help","Bandwidth is used to change the bandwidth of a link.")
        bwButton.bind('<Button-1>', left_bw)   
        bwButton.bind('<Button-3>', right_bw)  

        def left_delay(event):
            self.set_delay(net)
        def right_delay(event):
            msg.showinfo("Help","Delay is used to change the delay of a link.")
        delayButton.bind('<Button-1>', left_delay)   
        delayButton.bind('<Button-3>', right_delay)  

        def left_jitter(event):
            self.set_jitter(net)
        def right_jitter(event):
            msg.showinfo("Help","Jitter is used to change the jitter of a link.")
        jitterButton.bind('<Button-1>', left_jitter)   
        jitterButton.bind('<Button-3>', right_jitter)  

        def left_loss(event):
            self.set_loss(net)
        def right_loss(event):
            msg.showinfo("Help","Loss is used to change the loss of a link.")
        lossButton.bind('<Button-1>', left_loss)   
        lossButton.bind('<Button-3>', right_loss)  

        def left_IP(event):
            self.set_IP(net)
        def right_IP(event):
            msg.showinfo("Help","Set IP is used to change the IP of a node.")
        IPButton.bind('<Button-1>', left_IP)   
        IPButton.bind('<Button-3>', right_IP)  

        def left_MAC(event):
            self.set_MAC(net)
        def right_MAC(event):
            msg.showinfo("Help","Set MAC is used to change the MAC of a node.")
        MACButton.bind('<Button-1>', left_MAC)   
        MACButton.bind('<Button-3>', right_MAC)  

        def left_link(event):
            self.set_link(net)
        def right_link(event):
            msg.showinfo("Help","Set Link is used to up/down a link.")
        linkButton.bind('<Button-1>', left_link)   
        linkButton.bind('<Button-3>', right_link)  

        def left_host(event):
            self.add_host(net)
        def right_host(event):
            msg.showinfo("Help","Add Host is used to add a host node.")
        hostButton.bind('<Button-1>', left_host)   
        hostButton.bind('<Button-3>', right_host)  

        def left_switch(event):
            self.add_switch(net)
        def right_switch(event):
            msg.showinfo("Help","Add Switch is used to add a switch node.")
        switchButton.bind('<Button-1>', left_switch)   
        switchButton.bind('<Button-3>', right_switch)  

        def left_iperf(event):
            self.start_iperf(net)
        def right_iperf(event):
            msg.showinfo("Help","Do iperf is used to perform TCP Bandwidth measurement between two hosts.")
        iperfButton.bind('<Button-1>', left_iperf)   
        iperfButton.bind('<Button-3>', right_iperf)  

        def left_iperfudp(event):
            self.start_iperfudp(net)
        def right_iperfudp(event):
            msg.showinfo("Help","Do iperfudp is used to perform UDP Bandwidth measurement between two hosts.")
        iperfudpButton.bind('<Button-1>', left_iperfudp)   
        iperfudpButton.bind('<Button-3>', right_iperfudp)  

        def left_node(event):
            self.show_nodes(net)
        def right_node(event):
            msg.showinfo("Help","Node List shows all nodes in the currently used topology.")
        nodeButton.bind('<Button-1>', left_node)   
        nodeButton.bind('<Button-3>', right_node)  

        def left_dump(event):
            self.dump_nodes(net)
        def right_dump(event):
            msg.showinfo("Help","Dump Node shows the details of all nodes in the currently used topology.")
        dumpButton.bind('<Button-1>', left_dump)   
        dumpButton.bind('<Button-3>', right_dump)  

        def left_nat(event):
            self.add_NAT(net)
        def right_nat(event):
            msg.showinfo("Help","Add NAT is used to add a Network Address Translation to a node.")
        addnatButton.bind('<Button-1>', left_nat)   
        addnatButton.bind('<Button-3>', right_nat)  

        def left_ctrl(event):
            self.add_Controller(net)
        def right_ctrl(event):
            msg.showinfo("Help","Add Controller is used to add an Open VSwitch Controller.")
        addctrlButton.bind('<Button-1>', left_ctrl)   
        addctrlButton.bind('<Button-3>', right_ctrl)  

        def left_add_link(event):
            self.add_link(net)
        def right_add_link(event):
            msg.showinfo("Help","Add Link is used to add a link: Connection between two nodes.")
        addlinkButton.bind('<Button-1>', left_add_link)   
        addlinkButton.bind('<Button-3>', right_add_link)  

        def left_del_link(event):
            self.delete_link(net)
        def right_del_link(event):
            msg.showinfo("Help","Delete Link is used to delete link between two nodes.")
        dellinkButton.bind('<Button-1>', left_del_link)   
        dellinkButton.bind('<Button-3>', right_del_link)  

        def left_stopswitch(event):
            self.stop_switch(net)
        def right_stopswitch(event):
            msg.showinfo("Help","Stop Switch is used to stop a working switch.")
        stopswitchButton.bind('<Button-1>', left_stopswitch)   
        stopswitchButton.bind('<Button-3>', right_stopswitch)  

        def left_delnode(event):
            self.del_node(net)
        def right_delnode(event):
            msg.showinfo("Help","Delete Node is used to remove node from the currently used topology.")
        delnodeButton.bind('<Button-1>', left_delnode)   
        delnodeButton.bind('<Button-3>', right_delnode)  

        def left_CLI(event):
            CLI(net)
        def right_CLI(event):
            msg.showinfo("Help","Command Line Interface to run Mininet and OpenFlow directly.")
        cliButton.bind('<Button-1>', left_CLI)   
        cliButton.bind('<Button-3>', right_CLI)  

        def left_quit(event):
            topopt.quit
        def right_quit(event):
            msg.showinfo("Help","Quit the program.")
        quitButton.bind('<Button-1>', left_quit)   
        quitButton.bind('<Button-3>', right_quit)  


        topopt.mainloop()

        #utilities goes here

    def ping_node(self,net):

        currenth1=sdk.askstring("Ping Node","Please enter node 1: ")
        if currenth1 not in net.keys():
            currenth1 = self.check_node(currenth1,net)
        currenth2=sdk.askstring("Ping Node","Please enter node 2: ")
        if currenth2 not in net.keys() or currenth2 == currenth1:
            currenth2 = self.check_node2(currenth2,net,currenth1)
        h = ['h1','h2']
        h[0] = net.get(currenth1)
        h[1] = net.get(currenth2)
        net.ping(h)

    def set_bandwidth(self, net):
        print "Set Bandwidth"
        currentn1=sdk.askstring("Set Bandwidth","Please enter node 1: ")
        if currentn1 not in net.keys():
            currentn1 = self.check_node(currentn1,net)
        currentn2=sdk.askstring("Set Bandwidth","Please enter node 2: ")
        if currentn2 not in net.keys() or currentn2 == currentn1:
            currentn2 = self.check_node2(currentn2,net,currentn1)
        b1 = net.get(currentn1)
        b2 = net.get(currentn2)
        newbw=sdk.askstring("New Bandwidth","Please enter the desired bandwidth(b/s): ")
        links = b1.connectionsTo(b2)
        srcLink = links[0][1]
        dstLink = links[0][1]
        srcLink.config(**{ 'bw' : newbw})
        dstLink.config(**{ 'bw' : newbw})
        print srcLink.config()
        print "The new bandwidth is ", srcLink.config('bw')

    def set_delay(self, net):
        print "Set delay"
        currentd1=sdk.askstring("Set Delay","Please enter node 1: ")
        if currentd1 not in net.keys():
            currentd1 = self.check_node(currentd1,net)
        currentd2=sdk.askstring("Set Delay","Please enter node 2: ")
        if currentd2 not in net.keys() or currentd2 == currentd1:
            currentd2 = self.check_node2(currentd2,net,currentd1)
        d1 = net.get(currentd1)
        d2 = net.get(currentd2)
        newdelay=sdk.askstring("New Delay","Please enter the desired delay: ")
        links = d1.connectionsTo(d2)
        srcLink = links[0][1]
        dstLink = links[0][1]
        srcLink.config(**{ 'delay' : newdelay})
        dstLink.config(**{ 'delay' : newdelay})

    def set_jitter(self, net):
        print "Set jitter"
        currentj1=sdk.askstring("Set Jitter","Please enter node 1: ")
        if currentj1 not in net.keys():
            currentj1 = self.check_node(currentj1,net)
        currentj2=sdk.askstring("Set Jitter","Please enter node 2: ")
        if currentj2 not in net.keys() or currentj2 == currentj1:
            currentj2 = self.check_node2(currentj2,net,currentj1)
        j1 = net.get(currentj1)
        j2 = net.get(currentj2)
        newjitter=sdk.askstring("New Jitter","Please enter the desired jitter: ")
        links = j1.connectionsTo(j2)
        srcLink = links[0][1]
        dstLink = links[0][1]
        srcLink.config(**{ 'jitter' : newjitter})
        dstLink.config(**{ 'jitter' : newjitter})

    def set_loss(self, net):
        print "Set loss"
        currentj1=sdk.askstring("Set Loss","Please enter node 1: ")
        if currentl1 not in net.keys():
            currentl1 = self.check_node(currentl1,net)
        currentl2=sdk.askstring("Set Loss","Please enter node 2: ")
        if currentl2 not in net.keys() or currentl2 == currentl1:
            currentl2 = self.check_node2(currentl2,net,currentl1)
        l1 = net.get(currentl1)
        l2 = net.get(currentl2)
        newloss=sdk.askstring("New Loss","Please enter the desired loss: ")
        links = l1.connectionsTo(l2)
        srcLink = links[0][1]
        dstLink = links[0][1]
        srcLink.config(**{ 'loss' : newloss})
        dstLink.config(**{ 'loss' : newloss})

    def set_IP(self, net):
        print "Set IP"
        currentIP=sdk.askstring("Set IP","Please enter node 1: ")
        if currentIP not in net.keys():
            currentIP = self.check_node(currentIP,net)
        i = net.get(currentIP)
        newi=sdk.askstring("New IP","Please enter the desired IP: ")
        i.setIP(ip=newi)
        print "The new IP is:", i.IP()
    def set_MAC(self, net):
        currentMAC=sdk.askstring("Set MAC","Please enter node 1: ")
        if currentMAC not in net.keys():
            currentMAC = self.check_node(currentMAC,net)
        m = net.get(currentMAC)
        newm=sdk.askstring("New MAC","Please enter the desired MAC: ")
        m.setMAC(newm)
        print "The new MAC is:", i.MAC()

    def set_link(self, net):   
        msg.showwarning("1. Up Link. 2. Down Link")
        link_opt = sdk.askinteger("Link Options","What do you want to do? ")
        if link_opt=="1":
            print ("Enter the nodes you want to link: ")
            link1=sdk.askstring("Up Link","Please enter node 1: ")
            if link1 not in net.keys():
                link1 = self.check_node(link1,net)
            link2=sdk.askstring("Up Link","Please enter node 2: ")
            if link2 not in net.keys() or link2 == link1:
                link2 = self.check_node2(link2,net,link1)
            node1 = net.get(link1)
            node2 = net.get(link2)
            Link1=net.configLinkStatus(node1,node2, 'up')
        if link_opt=="2":
            down1=sdk.askstring("Down Link","Please enter node 1: ")
            if down1 not in net.keys():
                down1 = self.check_node(down1,net)
            down2=sdk.askstring("Down Link","Please enter node 2: ")
            if down2 not in net.keys() or down2 == down1:
                down2 = self.check_node2(down2,net,down1)
                node1 = net.get(down1)
                node2 = net.get(down2)
                down_link=net.configLinkStatus(node1,node2, 'down')
        else: 
            msg.showwarning("Please choose one of the options: ")
            set_link(self,net)


    def add_link(self,net):
        print "Add link"
        bw = 10000
        delay = 10
        source=sdk.askstring("Source","Please enter source node: ")
        if source not in net.keys():
            source = self.check_node(source,net)
        dest=sdk.askstring("Destination","Please destination node: ")
        if dest not in net.keys() or dest == source:
            dest = self.check_node2(dest,net,source)
        bw_input = sdk.askstring("Bandwidth","Enter the desired bandwidth(default 10 GB): ")
        if (bw_input is not None):
            bw_input = bw
        else: bw = bw
        delay_input = sdk.askstring("Delay", "Enter the desired delay(default 10ms): ")
        if (delay_input is not None):
            delay_input = delay
        else: delay = delay
        node1 = net.get(source)
        node2 = net.get(dest)
        net.addLink(node1,node2,bw,delay)

    def add_host(self,net):
        print "Add host"
        hostname = sdk.askstring("Add Host","Enter name of host: ")
        net.addHost(name = hostname)

    def add_switch(self,net):
        print "Add switch"
        switchname = sdk.askstring("Add Switch","Enter name of switch: ")
        net.addSwitch(name = switchname)

    def add_NAT(self,net):
        print "Add NAT"
        natname = sdk.askstring("Add NAT","Enter NAT name: ")
        connectTo = sdk.askstring("Switch Connect", "Enter Switch to connect to: ")
        net.addNAT(name = natname,connect = connectTo)

    def add_Controller(self,net):
        print "Add Controller"
        ctrlName = sdk.askstring("Add Controller","Enter Controller name: ")
        net.addController(name=ctrlName,
                          controller=OVSController,
                          protocol=controllerProtocol,
                          port=controllerPort)

    def delete_link(self,net):
        print "Delete link"
        currentn1 = sdk.askstring("Delete Link","Enter node 1 to delete link: ")
        if currentn1 not in net.keys():
            currentn1 = self.check_node(currentn1,net)
        currentn2 = sdk.askstring("Delete Link","Enter node 2 to delete link: ")
        if currentn2 not in net.keys() or currentn2 == currentn1:
            currentn2 = self.check_node2(currentn2,net,currentn1)
        node1 = net.get(currentn1)
        node2 = net.get(currentn2)
        net.delLinkBetween(node1,node2)

    def stop_switch(self,net):
        print "Stop switch"
        currents = sdk.askstring("Stop Switch","Enter switch to stop: ")
        if currents not in net.keys():
            currents = self.check_node(currents,net)
        switch1 = net.get(currents)
        net.stop(switch1)

    def del_node(self,net):
        print "Delete node"
        currentn = sdk.askstring("Delete Node","Enter node to delete: ")
        if currentn not in net.keys():
            currentn = self.check_node(currentn,net)
        node1 = net.get(currentn)
        net.delNode(node1)

    def start_iperf(self,net):
        currenth1 = sdk.askstring("Iperf","Enter node 1 to iperf: ")
        if currenth1 not in net.keys():
            currenth1 = self.check_node(currents,net)
        currenth2 = sdk.askstring("Iperf","Enter node 2 to iperf: ")
        if currenth2 not in net.keys() or currenth2 == currenth1:
            currenth2 = self.check_node2(currenth2,net,currenth1)
        h = ['h1','h2']
        h[0] = net.get(currenth1)
        h[1] = net.get(currenth2)
        net.iperf(h)

    def start_iperfudp(self,net):
        currenth1 = sdk.askstring("IperfUDP","Enter node 1 to iperf: ")
        if currenth1 not in net.keys():
            currenth1 = self.check_node(currents,net)
        currenth2 = sdk.askstring("IperfUDP","Enter node 2 to iperf: ")
        if currenth2 not in net.keys() or currenth2 == currenth1:
            currenth2 = self.check_node2(currenth2,net,currenth1)
        bw=sdk.askstring("IperfUDP Bandwidth","Please enter UDP Bandwidth: ")
        h = ['h1','h2']
        h[0] = net.get(currenth1)
        h[1] = net.get(currenth2)
        net.iperf(h, l4Type='UDP',udpBw=bw)

    def ping_pair(self,net):
        net.pingPair()

    def ping_pair_full(self,net):
        net.pingPairFull()

    def ping_full(self,net):
        currenth1 = sdk.askstring("Ping Full","Enter node 1 to ping full: ")
        if currenth1 not in net.keys():
            currenth1 = self.check_node(currents,net)
        currenth2 = sdk.askstring("Ping Full","Enter node 2 to ping full: ")
        if currenth2 not in net.keys() or currenth2 == currenth1:
            currenth2 = self.check_node2(currenth2,net,currenth1)
        h = ['h1','h2']
        h[0] = net.get(currenth1)
        h[1] = net.get(currenth2)
        net.pingFull(h)

    def ping_all(self,net):
        net.pingAll()

    def ping_all_full(self,net):
        net.pingAllFull()

    def show_nodes(self,net): #show all nodes on net
        print "Available nodes:"
        print net.keys()

    def dump_nodes(self,net): #dump info of all nodes
        print "Dumping nodes:"
        print net.values()

    def dpctl_use(self,net):
        param = sdk.askstring("Enter the dpctl function you want to use: ")

    def xterm(self,net):
        node = sdk.askstring("Enter the node to open xterm: ")

    #def ofctl_cmd(self,net): #use dpctl commands

    #def turn_switch(self,net): #turn switch on or off

    #def show_ports(self,net): #mininet dump
    #self.intfList(net)?

    #def show_interface(self,net): #mininet intfs
    #intfNames(net)?

    #def show_net(self,net): #show connected intfs
    
    

        #tutorial instructions goes here

    def tutorial_0(self):
        setLogLevel('info')
        top0 = Toplevel()
        top0.title("Tutorial 0 Instructions")
        msg = Message(top0, textvariable=instr0)
        instr0.set("Please follow the instruction on the paper\n"
        "Initializing Twinpair Topology.")
        msg.pack()
        self.twinpair_topo()

        top0.mainloop()
        

    def tutorial_1(self):
        setLogLevel('info')
        # basic mininet tutorial.
        top1 = Toplevel()
        top1.title("Tutorial 1 Instructions")
        instr1 = StringVar()
        msg = Message(top1, textvariable=instr1)
        instr1.set("Log level is set to 'info'.\n"
        "Minimal topology used.\n"
        "The first tutorial is to familiarize Mininet commands\n"
        "Use mininet basic commands to see the created network\n"
        "1. Use 'h1 ping h2' and 'pingall'\n"
        "2. Use 'iperf h1 h2' to see the TCP Bandwidth between h1 and h2\n"
        "3. Use 'iperfudp 1M h1 h2' to see UDP Bandwidth between h1 and h2 at 1MB\n"
        "4. Use 'links' to see available links\n"
        "5. Use 'h2 ifconfig' to see properties of h2\n"
        "6. Use 'nodes' to see all available nodes.\n"
        "7. Use 'pingpairfull' to see the details of each ping pair.\n"
        "Please use CLI option to do the above actions.")
        msg.pack()
        self.minimal_topo()

        top1.mainloop()

    def tutorial_2(self):
        setLogLevel('info')
        top2 = Toplevel()
        top2.title("Tutorial 2 Instructions")
        instr2 = StringVar()
        msg = Message(top2, textvariable=instr2)
        instr2.set("Log level is set to 'info'.\n"
        "Tree topology used.\n"
        "This tutorial are regarding the Open vSwitch.\n"
        "Open vSwitch are a multilayer virtual switch\n"
        "It supports network protocols and work like physical switches.\n"
        "Any depth and fanout of the tree topology can be used\n"
        "Under 5 for each is recommended to ease testing.\n"
        "use 'sh' command before ovs-ofctl to use Open vSwitch inside of Mininet\n"
        "1. Use 'ovs-ofctl show s1' to find information on the switch\n"
        "2. Use 'ovs-ofctl dump-tables s1' and 'ovs-ofctl dump-flows s1'\n"
        "4. Try to ping from h1s1 to a host of another switch on Mininet CLI.\n"
        "5. Use 'ovs-ofctl del-flows s1'\n"
        "6. Try pinging again.\n"
        "7. Use 'ovs-ofctl add-flow s1 action=normal'\n"
        "8. Try pinging again.\n"
        "Please use CLI option to do the above actions.")
        msg.pack()
        self.tree_topo()

        top2.mainloop()

    def tutorial_3(self):
        setLogLevel('info')
        top3 = Toplevel()
        top3.title("Tutorial 3 Instructions")
        instr3 = StringVar()
        msg = Message(top3, textvariable=instr3)
        instr3.set("Log level is set to 'info'.\n"
        "Linear topology used.\n"
        "This tutorial are regarding traffic.\n"
        "Traffic can be monitored with several tools\n"
        "Among them Wireshark and xterm\n"
        "tcpdump can be used on xterm to see the moving packets\n"
        "use 'sh' before shell commands to use terminal inside of Mininet\n"
        "Prep: Enter amount of switch and host you want to have on each switch\n"
        "Less than 4 switches is recommended for ease of test.\n"
        "1. Run wireshark with 'sh wireshark &'\n"
        "2. Open xterm for two of the hosts with 'xterm <host> command' \n"
        "3. Start packet trace on xterm with 'tcpdump' command\n"
        "4. Ping the second host from the first host.\n"
        "5. Open xterm for two more pair of hosts.\n"
        "6. Start tcpdump on both and do pingall."
        "Please use CLI option to do the above actions.")
        msg.pack()
        self.linear_topo()

    def tutorial_4(self):
        setLogLevel('info')
        top4 = Toplevel()
        top4.title("Tutorial 4 Instructions")
        instr4 = StringVar()
        msg = Message(top4, textvariable=instr4)
        instr4.set("Log level is set to 'info'.\n"
        "Rectangle topology used.\n"
        "This tutorial are regarding routing.\n"
        "Routing in a network depends on the flow table\n"
        "However, there are times when a link went down\n"
        "Switch can be set to send packets from a different route\n"
        "Prep: Start xterm on s2 and s4 and use tcpdump\n"
        "1. Test connection between all hosts with 'pingall'. Observe xterm'\n"
        "2. Use 'link s1 s2 down' and 'link s3 s4 down'.\n"
        "3. Do another pingall. Observe xterm.\n"
        "4. Use 'link s1 s2 up'.\n"
        "5. Ping h1 to h6. Observe xterm\n"
        "Please use CLI option to do the above actions.")
        msg.pack()
        self.rectangle_topo()

        #Next Step: Make sure all the options above work

    #exceptions

    def check_node(self,cnode,net):
        while cnode not in net.keys():
            msg.showwarning("Node Not Found!","Choose one of :  %s" % net.keys())
            cnode=sdk.askstring("Node Entry", "Please reenter node: ")
            return cnode

    def check_node2(self,cnode,net,node1):
        while cnode not in net.keys() or cnode == node1:
            msg.showwarning("Node Error!","Choose one of :  %s" % net.keys())
            cnode=sdk.askstring("Node Entry", "Please reenter node: ")
            return cnode

    # def ifHost(self,cnode,net):

    # def ifSwitch(self,cnode,net):
    
        #Help messages goes here.

    

root = Tk()
root.title("Simple Mininet UI")

app = App(root)

root.mainloop()
root.destroy() # optional; see description below
