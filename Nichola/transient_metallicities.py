import numpy as np
import pandas as pd
from hoki import load
import matplotlib.pyplot as plt

# BINARY
path = 'Downloads//bpass_v2.2.1_imf135_300'
br_1 = load.model_output(path + '//supernova-bin-imf135_300.z001.dat.gz')[:-1]
br_2 = load.model_output(path + '//supernova-bin-imf135_300.z002.dat.gz')[:-1]
br_3 = load.model_output(path + '//supernova-bin-imf135_300.z003.dat.gz')[:-1]
br_4 = load.model_output(path + '//supernova-bin-imf135_300.z004.dat.gz')[:-1]
br_5 = load.model_output(path + '//supernova-bin-imf135_300.z006.dat.gz')[:-1]
br_6 = load.model_output(path + '//supernova-bin-imf135_300.z008.dat.gz')[:-1]
br_7 = load.model_output(path + '//supernova-bin-imf135_300.z010.dat.gz')[:-1]
br_8 = load.model_output(path + '//supernova-bin-imf135_300.z014.dat.gz')[:-1]
br_9 = load.model_output(path + '//supernova-bin-imf135_300.z020.dat.gz')[:-1]
br_10 = load.model_output(path + '//supernova-bin-imf135_300.z030.dat.gz')[:-1]
br_11 = load.model_output(path + '//supernova-bin-imf135_300.z040.dat.gz')[:-1]
br_12 = load.model_output(path + '//supernova-bin-imf135_300.zem4.dat.gz')[:-1]
br_13 = load.model_output(path + '//supernova-bin-imf135_300.zem5.dat.gz')[:-1]

file_list = [br_1, br_2, br_3, br_4, br_5, br_6, br_7, br_8, br_9, br_10, br_11,
              br_12, br_13]
metallicities = [0.00001, 0.0001, 0.001, 0.002, 0.003, 0.004, 0.006, 0.008, 
                 0.01, 0.014, 0.02, 0.03, 0.04]

age = [0]*13
bin_size = [0]*13
ccsne = [0]*13
ccsne_norm = [0]*13
typeIa_norm = [0]*13
lgrbs_norm = [0]*13
pisne_norm = [0]*13
for i, file in enumerate(file_list):
    age[i] = file.log_age.values
    bin_size[i] = file.age_yrs.values
    ccsne[i] = (file[['IIP', 'II', 'Ib', 'Ic']].sum(axis=1))
    ccsne_norm[i] = ccsne[i]/bin_size[i]/(10**6)
    typeIa_norm[i] = file.Ia.values/bin_size[i]/(10**6)
    lgrbs_norm[i] = file.LGRB.values/bin_size[i]/(10**6)
    pisne_norm[i] = file.PISNe.values/bin_size[i]/(10**6)


# plots all transient rates on the same graph (edit for other transient types)

plt.figure(figsize = (10,7))
for ag, norm, z in zip(age, pisne_norm, metallicities):
    plt.step(ag, norm, label="z = {}".format(z)) 
plt.yscale("log")
plt.xlim(6, 7)
plt.ylim(10**(-15), 10**(-9))
plt.ylabel(r"Event Rate (events/M$_{\odot}$/year)")
plt.xlabel("log(age/yrs)")
plt.legend(fontsize=16)
plt.title("Event Rates for Varying Metallicity PISNe Transients")
plt.show()


# plots all transient rates on different graphs (edit for other transient types)
'''
for ag, norm in zip(age, typeIa_norm):
    plt.figure(figsize = (10,7))
    plt.step(ag, norm, label='CCSNe')
    plt.yscale("log")
    plt.xlim(7.5, 11.5)
    plt.ylim(10**(-15), 10**(-9))
    plt.ylabel(r"Event Rate (events/M$_{\odot}$/year)")
    plt.xlabel("log(age/yrs)")
    plt.legend(fontsize=16)
    plt.show()
'''

# plots max transient rate as a function of metallicity
'''
max_time_typeIa = []
for i, file in enumerate(typeIa_norm):
    index, element = max(list(enumerate(typeIa_norm[i])), key=lambda x:x[1])
    max_time_typeIa.append(age[i][index])


max_time_ccsne = []
for i, file in enumerate(ccsne_norm):
    index, element = max(list(enumerate(ccsne_norm[i])), key=lambda x:x[1])
    max_time_ccsne.append(age[i][index])

max_time_lgrbs = []
for i, file in enumerate(lgrbs_norm):
    index, element = max(list(enumerate(lgrbs_norm[i])), key=lambda x:x[1])
    max_time_lgrbs.append(age[i][index])

max_time_pisne = []
for i, file in enumerate(pisne_norm):
    index, element = max(list(enumerate(pisne_norm[i])), key=lambda x:x[1])
    max_time_pisne.append(age[i][index])    

plt.figure(figsize = (10,7))
#plt.scatter(max_time_ccsne, metallicities, color='k', label='CCSNe')
plt.scatter(max_time_typeIa, metallicities, color='g', label='Type Ia')
#plt.scatter(max_time_lgrbs, metallicities, color='r', label='LGRBs')
#plt.scatter(max_time_pisne, metallicities, color='b', label='PISNe')
plt.show()
'''

# SINGULAR
# plots all transient rates on the same graph (edit for other transient types)

sbr_1 = load.model_output(path + '//supernova-sin-imf135_300.z001.dat.gz')[:-1]
sbr_2 = load.model_output(path + '//supernova-sin-imf135_300.z002.dat.gz')[:-1]
sbr_3 = load.model_output(path + '//supernova-sin-imf135_300.z003.dat.gz')[:-1]
sbr_4 = load.model_output(path + '//supernova-sin-imf135_300.z004.dat.gz')[:-1]
sbr_5 = load.model_output(path + '//supernova-sin-imf135_300.z006.dat.gz')[:-1]
sbr_6 = load.model_output(path + '//supernova-sin-imf135_300.z008.dat.gz')[:-1]
sbr_7 = load.model_output(path + '//supernova-sin-imf135_300.z010.dat.gz')[:-1]
sbr_8 = load.model_output(path + '//supernova-sin-imf135_300.z014.dat.gz')[:-1]
sbr_9 = load.model_output(path + '//supernova-sin-imf135_300.z020.dat.gz')[:-1]
sbr_10 = load.model_output(path + '//supernova-sin-imf135_300.z030.dat.gz')[:-1]
sbr_11 = load.model_output(path + '//supernova-sin-imf135_300.z040.dat.gz')[:-1]
sbr_12 = load.model_output(path + '//supernova-sin-imf135_300.zem4.dat.gz')[:-1]
sbr_13 = load.model_output(path + '//supernova-sin-imf135_300.zem5.dat.gz')[:-1]

sin_file_list = [sbr_1, sbr_2, sbr_3, sbr_4, sbr_5, sbr_6, sbr_7, sbr_8, sbr_9, 
                 sbr_10, sbr_11, sbr_12, sbr_13]

sin_age = [0]*13
sin_bin_size = [0]*13
sin_ccsne = [0]*13
sin_ccsne_norm = [0]*13
sin_pisne_norm = [0]*13
for i, file in enumerate(sin_file_list):
    sin_age[i] = file.log_age.values
    sin_bin_size[i] = file.age_yrs.values
    sin_ccsne[i] = (file[['IIP', 'II', 'Ib', 'Ic']].sum(axis=1))
    sin_ccsne_norm[i] = ccsne[i]/bin_size[i]/(10**6)
    sin_pisne_norm[i] = file.PISNe.values/bin_size[i]/(10**6)

plt.figure(figsize = (10,7))
for ag, norm, z in zip(sin_age, sin_pisne_norm, metallicities):
    plt.step(ag, norm, label="z = {}".format(z)) 
plt.yscale("log")
plt.xlim(6, 7)
plt.ylim(10**(-15), 10**(-9))
plt.ylabel(r"Event Rate (events/M$_{\odot}$/year)")
plt.xlabel("log(age/yrs)")
plt.legend(fontsize=16)
plt.title("Event Rates for Varying Metallicity PISNe Transients")
plt.show()
