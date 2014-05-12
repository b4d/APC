#!/usr/bin/env python
# -*- coding: utf-8 -*-


import commands, string
from time import strftime

ipInRow1 = "192.168.65.249"
ipInRow2 = "192.168.65.250"
ipRackPDU1 = "192.168.65.246"
ipRackPDU2 = "192.168.65.247"
ipRackPDU3 = "192.168.65.248"


mibFile = "/homes/stuff/powernet410.mib"

coolPower = 30
coolPowerSingle = 15



groupCoolOutput =  float(commands.getoutput("snmpwalk -v1 -c public -m '"+mibFile+"' -Ovq "+ipInRow1+" PowerNet-MIB::airIRRCGroupStatusCoolOutput.0"))/10
maxRackInletTemp =  float(commands.getoutput("snmpwalk -v1 -c public -m '"+mibFile+"' -Ovq "+ipInRow2+" PowerNet-MIB::airIRRCGroupStatusMaxRackInletTempMetric.0"))/10
minRackInletTemp =  float(commands.getoutput("snmpwalk -v1 -c public -m '"+mibFile+"' -Ovq "+ipInRow2+" PowerNet-MIB::airIRRCGroupStatusMinRackInletTempMetric.0"))/10

hotAir2 =  float(commands.getoutput("snmpwalk -v1 -c public -m '"+mibFile+"' -Ovq "+ipInRow2+" PowerNet-MIB::airIRRCUnitStatusReturnAirTempMetric.0"))/10
hotAir1 =  float(commands.getoutput("snmpwalk -v1 -c public -m '"+mibFile+"' -Ovq "+ipInRow1+" PowerNet-MIB::airIRRCUnitStatusReturnAirTempMetric.0"))/10

tempRack1 =  float(commands.getoutput("snmpwalk -v1 -c public -m '"+mibFile+"' -Ovq "+ipRackPDU1+" PowerNet-MIB::rPDU2SensorTempHumidityStatusTempC.1"))/10
tempRack2 =  float(commands.getoutput("snmpwalk -v1 -c public -m '"+mibFile+"' -Ovq "+ipInRow1+" PowerNet-MIB::airIRRCUnitStatusSupplyAirTempMetric.0"))/10
tempRack3 =  float(commands.getoutput("snmpwalk -v1 -c public -m '"+mibFile+"' -Ovq "+ipInRow2+" PowerNet-MIB::airIRRCUnitStatusSupplyAirTempMetric.0"))/10

powerRack1 =  float(commands.getoutput("snmpwalk -v1 -c public -m '"+mibFile+"' -Ovq "+ipRackPDU1+" PowerNet-MIB::rPDU2DeviceStatusPower.1"))/100
powerRack2 =  float(commands.getoutput("snmpwalk -v1 -c public -m '"+mibFile+"' -Ovq "+ipRackPDU2+" PowerNet-MIB::rPDU2DeviceStatusPower.1"))/100
powerRack3 =  float(commands.getoutput("snmpwalk -v1 -c public -m '"+mibFile+"' -Ovq "+ipRackPDU3+" PowerNet-MIB::rPDU2DeviceStatusPower.1"))/100

humidityPDU1 =  float(commands.getoutput("snmpwalk -v1 -c public -m '"+mibFile+"' -Ovq "+ipRackPDU1+" PowerNet-MIB::rPDU2SensorTempHumidityStatusRelativeHumidity.1"))


timestamp = strftime("%Y-%m-%d %H:%M")

podatki = timestamp+"\t"+str(groupCoolOutput)+"\t"+str(max(hotAir1, hotAir2))+"\t"+str(max(tempRack1, tempRack2, tempRack3))+"\t"+str(humidityPDU1)+"\t"+str(powerRack1+powerRack2+powerRack3)

print podatki

