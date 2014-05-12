#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import *
from pylab import *
import matplotlib.dates as md


# VARIABLES
lineWidth = 3
colorAxesTicks = '#dddddd'
data = csv2rec('climate.log', delimiter='\t')


# END OF VARIABLES

fig = figure(num=None, figsize=(17, 11), dpi=80, facecolor='w', edgecolor='k')
ax1 = fig.add_subplot(311)


# timestamp spremeni v date string tak lep
# zarotiraj oznake na y osi


#ax1.plot(data['timestamp'][1::5], data['htemp'][1::5], label='Hot air', color="red", linewidth=lineWidth)
#ax1.plot(data['timestamp'][1::5], data['ctemp'][1::5], label='Cold air', color="blue", linewidth=lineWidth)
ax1.plot(data['timestamp'], data['htemp'], label='Hot air', color="red", linewidth=lineWidth)
ax1.plot(data['timestamp'], data['ctemp'], label='Cold air', color="blue", linewidth=lineWidth)

ax1.spines['bottom'].set_color(colorAxesTicks)
ax1.spines['top'].set_color(colorAxesTicks) 
ax1.spines['right'].set_color(colorAxesTicks)
ax1.spines['left'].set_color(colorAxesTicks)

ax1.tick_params(axis='x', colors=colorAxesTicks)
ax1.tick_params(axis='y', colors=colorAxesTicks)

title('Temperature', fontweight='bold')
#xlabel('Time')
ylabel('Temperature (C)', color=colorAxesTicks)
legend(loc='upper left',prop={'size':7})
xticks(rotation=45)

ax=gca()
xfmt = md.DateFormatter('%d.%m. %H:%M')
ax.xaxis.set_major_formatter(xfmt)

#tight_layout()


ax2 = fig.add_subplot(312)

#ax2.plot(data['timestamp'][0::20], data['cooling'][0::20], label='Cooling power', color="blue", linewidth=lineWidth, markevery=20)
#ax2.plot(data['timestamp'][1::5], data['power'][1::5], label='Server power consumption', color="purple", linewidth=lineWidth)
ax2.plot(data['timestamp'], data['cooling'], label='Cooling power', color="blue", linewidth=lineWidth, markevery=20)
ax2.plot(data['timestamp'], data['power'], label='Server power consumption', color="purple", linewidth=lineWidth)

ax2.spines['bottom'].set_color(colorAxesTicks)
ax2.spines['top'].set_color(colorAxesTicks) 
ax2.spines['right'].set_color(colorAxesTicks)
ax2.spines['left'].set_color(colorAxesTicks)

ax2.tick_params(axis='x', colors=colorAxesTicks)
ax2.tick_params(axis='y', colors=colorAxesTicks)



title('Power', fontweight='bold')
#xlabel('Time')
ylabel('Power (kW)', color=colorAxesTicks)
legend(loc='upper left', prop={'size':7})
xticks(rotation=45)

ax=gca()
xfmt = md.DateFormatter('%d.%m. %H:%M')
ax.xaxis.set_major_formatter(xfmt)



ax3 = fig.add_subplot(313)

ax3.plot(data['timestamp'], data['humidity'], label='%RH', color="blue", linewidth=lineWidth)
#ax3.plot(data['timestamp'][1::5], data['humidity'][1::5], label='%RH', color="blue", linewidth=lineWidth)
ax3.spines['bottom'].set_color(colorAxesTicks)
ax3.spines['top'].set_color(colorAxesTicks) 
ax3.spines['right'].set_color(colorAxesTicks)
ax3.spines['left'].set_color(colorAxesTicks)

ax3.tick_params(axis='x', colors=colorAxesTicks)
ax3.tick_params(axis='y', colors=colorAxesTicks)



title('Humidity', fontweight='bold')
#xlabel('Time')
ylabel('RH (%)', color=colorAxesTicks)
xticks(rotation=45)

ax=gca()
xfmt = md.DateFormatter('%d.%m. %H:%M')
ax.xaxis.set_major_formatter(xfmt)

#legend(loc='upper left')

subplots_adjust(hspace=1)


savefig('podatki.png')

show()
