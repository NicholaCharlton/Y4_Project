# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 13:10:58 2023

@author: Nichola Charlton
"""

import h5py
import numpy as np
from pylab import cm
import matplotlib as mpl
import matplotlib.pyplot as plt

# sets label fonts to default
mpl.rcParams.update(mpl.rcParamsDefault)

path = "Downloads/"
file = h5py.File(f"{path}/data.h5", "r")
DTD = file["DTD"]  # data types: DTD, SFH, raw_SFH, event_rates, observations
event_types = ["Ia", "IIP", "II", "Ib", "Ic", "LGRB", "PISNe", "BBH", "BHNS",
               "BNS"]

# metallicity datasets: ['zem5', 'zem4', 'z001', 'z002', 'z003', 'z004', 
#                        'z006', 'z008', 'z010', 'z014', 'z020', 'z030', 
#                        'z040']
Z1 = "z020"  # 0.020
Z2 = "z001"  # 0.001

# calculating total rates for each metallicity
# CCSN rate is a combination of: "IIP", "II", "Ib", "Ic"
event_total = {}  # contains rates of each event as a function of time
for i in (Z1, Z2):
    event_total[i] = {}
    for j in event_types:
        event_total[i][j] = DTD[j][i][:]
    event_total[i]["CCSN"] = (event_total[i]["II"] + event_total[i]["Ib"] + 
                              event_total[i]["Ic"] + event_total[i]["IIP"])

fig, ax =  plt.subplots(nrows=1, ncols=1, figsize=(14,8))
colors = cm.get_cmap('tab10', 10)

x1 = event_total[Z1]
x_axis = np.linspace(6.0, 11.0, 51)

# Set the minor and major ticks on both axes
ax.xaxis.set_tick_params(which='major', size=10, width=2, direction='in', 
                         top='on')
ax.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in', 
                         top='on')
ax.yaxis.set_tick_params(which='major', size=10, width=2, direction='in')
ax.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in')

# set the location of the ticks
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.2))

# axes labels, limits, and scales
fig.text(0.5,0.03,r"Delay Time [$\log_{10}$(yr)]", ha="center", va="bottom")
ax.set_ylabel(r"Event rate [yr$^{-1}$ M$_\odot^{-1}$]")
ax.set_yscale('log')
ax.set_xlim(6,11)
ax.set_ylim(1e-15,1e-9)

# plotting rates as step functions
ax.step(x_axis, x1["CCSN"], where="post", color=colors(0), lw=3, label="CCSN")
ax.step(x_axis, x1["Ia"], where="post", color=colors(1), lw=3, label="Type Ia")
ax.step(x_axis, x1["PISNe"], where="post", color=colors(3), lw=3)
ax.step(x_axis, x1["LGRB"], where="post", color=colors(4), lw=3)
#ax.step(x_axis, x1["Ib"], where="post", color=colors(5), lw=3)
#ax.step(x_axis, x1["Ic"], where="post", color=colors(6), lw=3)
ax.step(x_axis, x1["BBH"], where="post", color='black', lw=3, label="BBH")
ax.step(x_axis, x1["BHNS"], where="post", color="black", lw=2, ls="--", 
        label="BHNS")
ax.step(x_axis, x1["BNS"], where="post", color="black", lw=2, ls=":", 
        label="BNS")

# legend
ax.legend(bbox_to_anchor=(1, 0.89), loc="upper right", frameon=False, 
          fontsize=22, ncol=1)
ax.text(0.97, 0.9, r"Z=Z$_\odot$", horizontalalignment='right', 
        transform=ax.transAxes, fontsize=35)


# event rates for different metallicity - requires editing subplots above
'''
x2 = event_total[Z2]
ax2 = axes[1]

# Set the minor and major ticks on both axes
ax2.xaxis.set_tick_params(which='major', size=10, width=2, direction='in', 
                          top='on')
ax2.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in', 
                          top='on')
ax2.yaxis.set_tick_params(which='major', size=10, width=2, direction='in', 
                          right='on')
ax2.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in', 
                          right='on')

# set the location of the ticks
ax2.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1))
ax2.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.2))

# axes labels, limits, and scales
ax2.set_yscale('log')
ax2.set_xlim(6.00001,11)
ax2.set_ylim(1e-15,1e-9)
ax2.set_yticklabels([])

# plotting rates as step functions
ax2.step(x_axis, x2["CCSN"], where="post", color=colors(0), lw=3)
ax2.step(x_axis, x2["Ia"], where="post", color=colors(1), lw=3)
ax2.step(x_axis, x2["LGRB"], where="post", color=colors(4), lw=3, label="LGRB")
ax2.step(x_axis, x2["PISNe"], where="post", color=colors(3), lw=3, 
         label="PISN")
ax2.step(x_axis, x2["BBH"], where="post", color='black', lw=3)
ax2.step(x_axis, x2["BHNS"], where="post", color="black", lw=2, ls="--")
ax2.step(x_axis, x2["BNS"], where="post", color="black", lw=2, ls=":")

# legend
ax2.legend(bbox_to_anchor=(0.99, 0.90), loc="upper right", frameon=False, 
           fontsize=22, ncol=1)
ax2.text(0.96, 0.9, r"Z=0.05Z$_\odot$", horizontalalignment='right', 
         transform=ax2.transAxes, fontsize=35)
'''

plt.show()

file.close()