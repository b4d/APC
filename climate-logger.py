#!/usr/bin/env python
# -*- coding: utf-8 -*-


import commands, string
from time import strftime

ipInRow1 = "192.168.65.249"
ipInRow2 = "192.168.65.250"
ipInRow3 = "192.168.65.229"
ipRackPDU1 = "192.168.65.246"
ipRackPDU2 = "192.168.65.247"
ipRackPDU3 = "192.168.65.248"
ipRackPDU4 = "192.168.65.230"


# Deprecated, copy this file to /usr/share/snmp/mibs/
#mibFile = "/homes/stuff/powernet410.mib"



inRow3CoolOutput =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow3+" PowerNet-MIB::coolingUnitStatusAnalogValue.1.10"))/10
groupCoolOutput =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow1+" PowerNet-MIB::airIRRCGroupStatusCoolOutput.0"))/10

groupCoolOutput = groupCoolOutput + inRow3CoolOutput

maxRackInletTemp =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow2+" PowerNet-MIB::airIRRCGroupStatusMaxRackInletTempMetric.0"))/10
minRackInletTemp =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow2+" PowerNet-MIB::airIRRCGroupStatusMinRackInletTempMetric.0"))/10

hotAir2 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow2+" PowerNet-MIB::airIRRCUnitStatusReturnAirTempMetric.0"))/10
hotAir1 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow1+" PowerNet-MIB::airIRRCUnitStatusReturnAirTempMetric.0"))/10
hotAir3 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow3+" PowerNet-MIB::coolingUnitStatusAnalogValue.1.4"))/10

tempRack1 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipRackPDU1+" PowerNet-MIB::rPDU2SensorTempHumidityStatusTempC.1"))/10
tempRack2 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow1+" PowerNet-MIB::airIRRCUnitStatusSupplyAirTempMetric.0"))/10
tempRack3 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow2+" PowerNet-MIB::airIRRCUnitStatusSupplyAirTempMetric.0"))/10
tempRack4 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow3+" PowerNet-MIB::coolingUnitStatusAnalogValue.1.2"))/10

powerRack1 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipRackPDU1+" PowerNet-MIB::rPDU2DeviceStatusPower.1"))/100
powerRack2 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipRackPDU2+" PowerNet-MIB::rPDU2DeviceStatusPower.1"))/100
powerRack3 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipRackPDU3+" PowerNet-MIB::rPDU2DeviceStatusPower.1"))/100
powerRack4 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipRackPDU4+" PowerNet-MIB::rPDU2DeviceStatusPower.1"))/100

humidityPDU1 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipRackPDU1+" PowerNet-MIB::rPDU2SensorTempHumidityStatusRelativeHumidity.1"))


timestamp = strftime("%Y-%m-%d %H:%M")

podatki = timestamp+"\t"+str(groupCoolOutput)+"\t"+str(max(hotAir1, hotAir2, hotAir3))+"\t"+str(max(tempRack1, tempRack2, tempRack3, tempRack4))+"\t"+str(humidityPDU1)+"\t"+str(powerRack1+powerRack2+powerRack3+powerRack4)

print podatki

