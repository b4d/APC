#!/usr/bin/env python
# -*- coding: utf-8 -*-


# For latest APC Schneider InRow ACRC301S you need MIB 4.1.7 in /usr/share/snmp/mibs/
# Get it here: ftp://ftp.apc.com/apc/public/software/pnetmib/mib/417/powernet417.mib

import commands, string, os
import time

ipInRow1 = "192.168.65.249"
ipInRow2 = "192.168.65.250"
ipInRow3 = "192.168.65.229"
ipRackPDU1 = "192.168.65.246"
ipRackPDU2 = "192.168.65.247"
ipRackPDU3 = "192.168.65.248"
ipRackPDU4 = "192.168.65.230"



coolPower = 30
coolPowerSingle = 15



inRow1CoolOutput =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow1+" PowerNet-MIB::airIRRCUnitStatusCoolOutput.0"))/10
#print progressBar((inRow1CoolOutput*100)/coolPowerSingle)

inRow2CoolOutput =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow2+" PowerNet-MIB::airIRRCUnitStatusCoolOutput.0"))/10
#print progressBar((inRow2CoolOutput*100)/coolPowerSingle)

#inRow3CoolOutput =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow3+" PowerNet-MIB::airIRRCUnitStatusCoolOutput.0"))/10
inRow3CoolOutput =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow3+" PowerNet-MIB::coolingUnitStatusAnalogValue.1.10"))/10

groupCoolOutput =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow1+" PowerNet-MIB::airIRRCGroupStatusCoolOutput.0"))/10
#print progressBar((groupCoolOutput*100)/coolPower)

groupCoolOutput = groupCoolOutput + inRow3CoolOutput



maxRackInletTemp =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow2+" PowerNet-MIB::airIRRCGroupStatusMaxRackInletTempMetric.0"))/10
# preveri se inrow3 ce je vecji

minRackInletTemp =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow2+" PowerNet-MIB::airIRRCGroupStatusMinRackInletTempMetric.0"))/10
# preveri se inrow3 ce je manjsi

hotAir1 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow1+" PowerNet-MIB::airIRRCUnitStatusReturnAirTempMetric.0"))/10
hotAir2 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow2+" PowerNet-MIB::airIRRCUnitStatusReturnAirTempMetric.0"))/10
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


#//
airFlow1 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow1+" PowerNet-MIB::airIRRCUnitStatusAirFlowMetric.0"))/10
airFlow2 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow2+" PowerNet-MIB::airIRRCUnitStatusAirFlowMetric.0"))/10
airFlow3 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow3+" PowerNet-MIB::coolingUnitStatusAnalogValue.1.11"))/10
#airFlow3

fanSpeed1 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow1+" PowerNet-MIB::airIRRCUnitStatusFanSpeed.0"))/10
fanSpeed2 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow2+" PowerNet-MIB::airIRRCUnitStatusFanSpeed.0"))/10
fanSpeed3 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow3+" PowerNet-MIB::coolingUnitStatusAnalogValue.1.12"))
# fanSpeed3

fluidFlow1 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow1+" PowerNet-MIB::airIRRCUnitStatusFluidFlowMetric.0"))/10
fluidFlow2 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow2+" PowerNet-MIB::airIRRCUnitStatusFluidFlowMetric.0"))/10
#fluidFlow3 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow3+" PowerNet-MIB::coolingUnitStatusAnalogValue.1.2"))/10
fluidFlow3 = 0
# fluidFlow3

fluidTempEnt1 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow1+" PowerNet-MIB::airIRRCUnitStatusEnteringFluidTemperatureMetric.0"))/10
fluidTempEnt2 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow2+" PowerNet-MIB::airIRRCUnitStatusEnteringFluidTemperatureMetric.0"))/10
#fluidTempEnt3 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow2+" PowerNet-MIB::airIRRCUnitStatusEnteringFluidTemperatureMetric.0"))/10
fluidTempEnt3 = 0
# fluidTempEnt3

fluidTempLea1 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow1+" PowerNet-MIB::airIRRCUnitStatusLeavingFluidTemperatureMetric.0"))/10
fluidTempLea2 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow2+" PowerNet-MIB::airIRRCUnitStatusLeavingFluidTemperatureMetric.0"))/10
#fluidTempLea3 =  float(commands.getoutput("snmpwalk -v1 -c public -Ovq "+ipInRow3+" PowerNet-MIB::airIRRCUnitStatusLeavingFluidTemperatureMetric.0"))/10
fluidTempLea3 = 0
# fluidTempLea3




#os.system('clear')

print
print "+---------------+---------------+---------------+---------------+---------------+---------------+---------------+"
print "| HPC KI @ "+time.strftime("%H:%M:%S %d/%m/%Y")+"                                                                                  |"
print "+---------------+---------------+---------------+---------------+---------------+---------------+---------------+"
print 
print "  ", groupCoolOutput, "kW \ttotal cool output"
print "  ", powerRack1+powerRack2+powerRack3+powerRack4, "kW \ttotal power consumption"
print
print "  ", maxRackInletTemp, "C \tmax rack inlet temperature"
print "  ", minRackInletTemp, "C \tmin rack inlet temperature"
print "  ", humidityPDU1, "% \trelative humidity"
print 
print "+---------------+---------------+---------------+---------------+---------------+---------------+---------------+"
print "| RACK 1 \t| INROW 1 \t| RACK 2 \t| INROW 2 \t| RACK 3 \t| INROW 3 \t| RACK 4 \t|"
print "+---------------+---------------+---------------+---------------+---------------+---------------+---------------+"
print "|\t\t|",inRow1CoolOutput,"kW\t|\t\t|",inRow2CoolOutput,"kW\t|\t\t|",inRow3CoolOutput,"kW\t|\t\t| cool output"
print "|               |               |               |               |               |               |               |"
print "|\t\t|",hotAir1,"C\t|\t\t|",hotAir2,"C\t|\t\t|",hotAir3,"C\t|\t\t| hot air temperature"
print "|\t\t|",fanSpeed1,"%\t|\t\t|",fanSpeed2,"%\t|\t\t|",fanSpeed3,"%\t|\t\t| fan speed"
print "|\t\t|",airFlow1,"L/s\t|\t\t|",airFlow2,"L/s\t|\t\t|",airFlow3,"L/s\t|\t\t| air flow"
print "|               |               |               |               |               |               |               |"
print "|\t",tempRack1,"C\t|\t\t|\t",tempRack2,"C\t|\t\t|\t",tempRack3,"C\t|\t\t|\t",tempRack4,"C\t| rack inlet temperature"
print "|               |               |               |               |               |               |               |"
print "|\t",powerRack1,"kW\t|\t\t|\t",powerRack2,"kW\t|\t\t|\t",powerRack3,"kW\t|\t\t|\t",powerRack4,"kW\t| power consumption"
print "+---------------+---------------+---------------+---------------+---------------+---------------+---------------+"
print "|\t\t|\t",fluidFlow1,"L/s\t|\t\t|\t",fluidFlow2,"L/s\t|\t\t|\t",fluidFlow3,"L/s\t|\t\t| fluid flow"
print "|\t\t|\t",fluidTempEnt1,"C\t|\t\t|\t",fluidTempEnt2,"C\t|\t\t|\t",fluidTempEnt3,"C\t|\t\t| fluid entering temperature"
print "|\t\t|\t",fluidTempLea1,"C\t|\t\t|\t",fluidTempLea2,"C\t|\t\t|\t",fluidTempLea3,"C\t|\t\t| fluid leaving temperature"
print "+---------------+---------------+---------------+---------------+---------------+---------------+---------------+"
print
