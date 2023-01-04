# vanetsimulation_ns3
This project contains source code for vehicular network simulation in ns3.
This code was compiled with NS3 version 3.29.

The source code can be copied to the scratch folder of ns3 package and can be called with following command:
./waf --run "scratch/vanetroutingcompare --scenario=2"

Download the mobility file change he path to mobility file at line # 2400 of the source code.
After the simulation, an XML file would be generated, carrying the details of the network packet exchanges having "...flowmonitor" in the name. This file can be parsed with the custom python script which will give total Received and Transmitted Packets.
