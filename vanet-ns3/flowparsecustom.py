from xml.etree import ElementTree as ET
import sys
import matplotlib.pyplot as pylab
et=ET.parse(sys.argv[1])
bitrates=[]
losses=[]
delays=[]
receivedpackets=[]
sentpackets=[]
for flow in et.findall("FlowStats/Flow"):
	receivedpackets.append(int(flow.get('rxPackets')))
	sentpackets.append(int(flow.get('txPackets')))
	

rxpackets = sum(receivedpackets)
txpackets = sum(sentpackets)
print("Received packet = {}".format(rxpackets))
print("Transmitted packets = {}".format(txpackets))
