APC
===

Set of scripts for monitoring and logging parameters of APC Schneider InRow and PDU parameters using SNMP protocol.

###### climate-logger.py
Script that logs custom parameters from the devices to a file via crontab.


###### climate-plot.py
Plot the data obtained with climate-logger.py.

###### status.py
Demo script, as used on a simple cluster, 2 InRow units, 3 Racks and 3 PDUs. 

###### Crontab

`*/10 * * * * climate-logger.py >> climate.log`


###### powernet410.mib
Translation file by APC Schneider, for easier snmp acces to parameter values.
