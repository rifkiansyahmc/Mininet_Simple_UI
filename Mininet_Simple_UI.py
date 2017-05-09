#!/usr/bin/env python

from Tkinter import *
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


class App:

    def __init__(self, master):

        w = Label(root, text="Choose from the available topology")
        w.pack()
        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.minimal_Button = Button(frame, text="Minimal", command=self.minimal_topo)
        self.minimal_Button.pack(side=LEFT)
        self.linear_Button = Button(frame, text="Linear", command=self.linear_topo)
        self.linear_Button.pack(side=LEFT)
        self.tree_Button = Button(frame, text="Tree", command=self.tree_topo)
        self.tree_Button.pack(side=LEFT)
        self.torus_Button = Button(frame, text="Torus", command=self.torus_topo)
        self.torus_Button.pack(side=LEFT)
        self.reversed_Button = Button(frame, text="Reversed", command=self.reversed_switch)
        self.reversed_Button.pack(side=LEFT)
        self.tutorial_Button = Button(frame, text="Tutorials", command=self.tutorial)
        self.tutorial_Button.pack(side=LEFT)

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
        ReverseSingle = SingleSwitchReversedTopo(k = hCount)
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
        CLI(net)
        net.stop()

    def tutorial(self):
        topt = Toplevel()
        topt.title("SDN Tutorial Menu")

        self.button = Button(
            topt, text="QUIT", fg="red", command=topt.quit
            )
        self.button.pack(side=LEFT)

        self.tutor1_Button = Button(topt, text="Tutorial 1", command=self.tutorial_1)
        self.tutor1_Button.pack(side=LEFT)
        self.tutor2_Button = Button(topt, text="Tutorial 2", command=self.tutorial_2)
        self.tutor2_Button.pack(side=LEFT)
        self.tutor3_Button = Button(topt, text="Tutorial 3", command=self.tutorial_3)
        self.tutor3_Button.pack(side=LEFT)
        self.tutor4_Button = Button(topt, text="Tutorial 4", command=self.tutorial_4)
        self.tutor4_Button.pack(side=LEFT)
        #print "Several tutorials are available: "
        #print "1. Basic mininet commands." #ping, iperf, IP change, etc. Use minimal topo.
        #print "2. View Open vSwitch configurations." #use ovs-ofctl
        #print "3. Generate and monitor traffic." #tcpdump, wireshark,
        #print "4. Configure routing on network." #link up or down. make several switch route for this
        #choice = raw_input()
        #if choice == "1":
        #    self.tutorial_1()
        #elif choice == "2":
        #    self.tutorial_2()
        #elif choice == "3":
        #    self.tutorial_3()
        #elif choice == "4":
        #    self.tutorial_4()
        #elif choice == "5":
        #    self.tutorial_5()

    def options(self, net):
        while True:
            print "What would you like to do?"
            print "1. Set Bandwidth"
            print "2. Set Delay"
            print "3. Set Jitter"
            print "4. Set Loss"
            print "5. Set IP"
            print "6. Set MAC"
            print "7. Up/Down Link"
            print "0. Open CLI" #Due to new path, use it extensively.
            print "Type 'exit' to exit program."

            choice = raw_input()
            if choice == "1":
                self.set_bandwidth(net)
            elif choice == "2":
                self.set_delay(net)
            elif choice == "3":
                self.set_jitter(net)
            elif choice == "4":
                self.set_loss(net)
            elif choice == "5":
                self.set_IP(net)
            elif choice == "6":
                self.set_MAC(net)
            elif choice == "7":
                self.set_link(net)
            elif choice == "0":
                CLI(net)
            elif choice == "exit":
                break

    def set_bandwidth(self, net):
        currentn1=raw_input("Please enter node 1 of the link: ")
        currentn2=raw_input("Please enter node 2 of the link: ")
        b1 = net.getNodeByName(currentn1)
        b2 = net.getNodeByName(currentn2)
        newbw=raw_input("Please enter the desired bandwidth(b/s): ")
        links = b1.connectionsTo(b2)
        srcLink = links[0][1]
        dstLink = links[0][1]
        srcLink.config(**{ 'bw' : newbw})
        dstLink.config(**{ 'bw' : newbw})
        #print "The new bandwidth is ", srcLink.bw
    def set_delay(self, net):
        currentd1=raw_input("Please enter node 1 you want to change: ")
        currentd1=raw_input("Please enter node 2 you want to change: ")
        d1 = net.getNodeByName(currentd1)
        d2 = net.getNodeByName(currentd2)
        newdelay=raw_input("Please enter the desired delay: ")
        srcLink = links[0][1]
        dstLink = links[0][1]
        srcLink.config(**{ 'delay' : newdelay})
        dstLink.config(**{ 'delay' : newdelay})
    def set_jitter(self, net):
        currentj1=raw_input("Please enter node 1 you want to change: ")
        currentj2=raw_input("Please enter node 2 you want to change: ")
        j1 = net.getNodeByName(currentj1)
        j2 = net.getNodeByName(currentj2)
        newjitter=raw_input("Please enter the desired jitter: ")
        srcLink = links[0][1]
        dstLink = links[0][1]
        srcLink.config(**{ 'jitter' : newjitter})
        dstLink.config(**{ 'jitter' : newjitter})
    def set_loss(self, net):
        currentl1=raw_input("Please enter node 1 you want to change: ")
        currentl2=raw_input("Please enter node 2 you want to change: ")
        l1 = net.getNodeByName(currentl1)
        l2 = net.getNodeByName(currentl2)
        newloss=raw_input("Please enter the desired loss: ")
        srcLink = links[0][1]
        dstLink = links[0][1]
        srcLink.config(**{ 'loss' : newloss})
        dstLink.config(**{ 'loss' : newloss})

    def set_IP(self, net):
        currentIP=raw_input("Please enter the node you want to change: ")
        i = net.get(currentIP)
        newi=raw_input("Please enter the desired IP: ")
        i.setIP(ip=newi)
        print "The new IP is:", i.IP()
    def set_MAC(self, net):
        currentMAC=raw_input("Please enter the node you want to change: ")
        m = net.get(currentMAC)
        newm=raw_input("Please enter the desired MAC: ")
        m.setMAC(newm)
        print "The new MAC is:", i.MAC()

    def set_link(self, net):
        print "1. Up Link"
        print "2. Down Link"
        link_opt = raw_input("Which option do you want to do?")
        if link_opt=="1":
            print ("Enter the nodes you want to link: ")
            link_1 = raw_input()
            host1 = net.get(link_1)
            link_2 = raw_input()
            host2 = net.get(link_2)
            Link1=self.Link(host1,host2)
        if link_opt=="2":
            deleted = raw_input("Enter the node with link you want to delete: ")
            currenthost = net.get(deleted)
            Link1=self.link(currenthost)
            Link1.delete()

    def tutorial_1(self):
        setLogLevel('info')
        # create root window contents...
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

        top.mainloop()

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

root = Tk()
root.title("Simple Mininet UI")

app = App(root)

root.mainloop()
root.destroy() # optional; see description below
