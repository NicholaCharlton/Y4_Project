# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:08:41 2023

@author: Nichola Charlton
"""

import pandas as pd
from hoki import load
import matplotlib.pyplot as plt

bin_rates = load.model_output(
    ('Downloads//bpass_v2.2.1_imf135_300//supernova-bin-imf135_300.z001.dat.gz')
    )
bin_rates = bin_rates[:-1]
age = bin_rates.log_age.values
bin_size = bin_rates.age_yrs.values

ccsne = (bin_rates[['IIP', 'II', 'Ib', 'Ic']].sum(axis=1))

ccsne_norm = ccsne/bin_size/(10**6)
typeIa_norm = bin_rates.Ia.values/bin_size/(10**6)
lgrbs_norm = bin_rates.LGRB.values/bin_size/(10**6)
pisne_norm = bin_rates.PISNe.values/bin_size/(10**6)

plt.figure(figsize = (10,7))
plt.step(age, typeIa_norm, label='SN Ia')
plt.step(age, ccsne_norm, label='CCSNe')
plt.step(age, lgrbs_norm, label='LGRB')
plt.step(age, pisne_norm, label='PISNe')
plt.yscale("log")
plt.text(9, 10**(-11), r"Z=0.05Z$_{\odot}$", fontsize=18)
plt.xlim(6, 11)
plt.ylim(10**(-15), 10**(-9))
plt.ylabel(r"Event Rate (events/M$_{\odot}$/year)")
plt.xlabel("log(age/yrs)")
plt.legend(fontsize=16)
plt.show()