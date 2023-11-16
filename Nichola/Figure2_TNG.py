import h5py
import numpy as np
import scipy.integrate
import illustris_python as il
import matplotlib.pyplot as plt

file = h5py.File(f"C:/Users/Nichola Charlton/Downloads/Documents/Y4 Project/star_formation_rates.hdf5", "r")
# keys in file include 'Snapshot_1' - 'Snapshot_99'
# keys in each snapshot - use print(file['Snapshot_n'].keys())
#   will use 'Snapshot_n/SFR_MsunPerYrs_in_r5pkpc_{x}Myrs
#   where {x} = 10, 50, 100, 200, 1000 Myr

snapshots = [2, 3, 4, 6, 8, 11, 13, 17, 21, 25, 33, 40, 50, 59, 67, 72, 78, 84, 
             91, 99]  # list of 'full' snapshots
redshifts = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1.5, 1, 0.7, 0.5, 0.4, 0.3, 
             0.2, 0.1, 0]


# CSFRD against redshift plot - including stars within a 3D aperture of 5 
#   physical kpc, averaged across the last 200 Myr

sfr = []
for snapshot in snapshots:
    shot = file['Snapshot_' + str(snapshot)]
    sfr.append(sum(shot['SFR_MsunPerYrs_in_r5pkpc_200Myrs'])/100**3)

empirical = []  # using Eqn 1. in Briel paper
for z in redshifts:
    numerator = 0.015*((1+z)**2.7)
    denominator = 1 + ((1+z)/2.9)**5.6
    y = (numerator/denominator)*0.66
    empirical.append(y)
'''
plt.plot(redshifts, sfr, label='TNG')
plt.plot(redshifts, empirical, label='Empirical')
plt.yscale('log')
plt.ylabel('CSFRD ($M_\odot$ yr$^{-1}$ Mpc$^{-3}$)')
plt.xlabel('Redshift')
plt.legend()
plt.show()


# CSFRD against redshift plot - for all time intervals {x} = 10, 50, 100, 200, 
#   1000 Myr

sfr_10 = []
for snapshot in snapshots:
    shot = file['Snapshot_' + str(snapshot)]
    sfr_10.append(sum(shot['SFR_MsunPerYrs_in_r5pkpc_10Myrs'])/100**3)
sfr_50 = []
for snapshot in snapshots:
    shot = file['Snapshot_' + str(snapshot)]
    sfr_50.append(sum(shot['SFR_MsunPerYrs_in_r5pkpc_50Myrs'])/100**3)
sfr_100 = []
for snapshot in snapshots:
    shot = file['Snapshot_' + str(snapshot)]
    sfr_100.append(sum(shot['SFR_MsunPerYrs_in_r5pkpc_100Myrs'])/100**3)
# sfr_200 is 'sfr' above
sfr_1000 = []
for snapshot in snapshots:
    shot = file['Snapshot_' + str(snapshot)]
    sfr_1000.append(sum(shot['SFR_MsunPerYrs_in_r5pkpc_1000Myrs'])/100**3)

plt.plot(redshifts, sfr_10, label='x = 10 Myr')
plt.plot(redshifts, sfr_50, label='x = 50 Myr')
plt.plot(redshifts, sfr_100, label='x = 100 Myr')
plt.plot(redshifts, sfr, label='x = 200 Myr')
plt.plot(redshifts, sfr_1000, label='x = 1000 Myr')
#plt.plot(redshifts, empirical, label='Empirical')
plt.yscale('log')
plt.ylabel('CSFRD ($M_\odot$ yr$^{-1}$ Mpc$^{-3}$)')
plt.xlabel('Redshift')
plt.legend()
plt.show()


# CSFRD against redshift plot - for all groups: SFR_MsunPerYrs_in_ [r5pkpc, 
#   InRad, r30pkpc, all] _200Myrs

# 5kpc is 'sfr' from above
sfr_inrad = []
for snapshot in snapshots:
    shot = file['Snapshot_' + str(snapshot)]
    sfr_inrad.append(sum(shot['SFR_MsunPerYrs_in_InRad_200Myrs'])/100**3)
sfr_30kpc = []
for snapshot in snapshots:
    shot = file['Snapshot_' + str(snapshot)]
    sfr_30kpc.append(sum(shot['SFR_MsunPerYrs_in_r30pkpc_200Myrs'])/100**3)
sfr_all = []
for snapshot in snapshots:
    shot = file['Snapshot_' + str(snapshot)]
    sfr_all.append(sum(shot['SFR_MsunPerYrs_in_all_200Myrs'])/100**3)

plt.plot(redshifts, sfr, label='5kpc aperture')
plt.plot(redshifts, sfr_inrad, label='2 x stellar half mass radius aperture')
plt.plot(redshifts, sfr_30kpc, label='30kpc aperture')
plt.plot(redshifts, sfr_all, label='all gravitationall bound stars')
#plt.plot(redshifts, empirical, label='Empirical')
plt.yscale('log')
plt.ylabel('CSFRD ($M_\odot$ yr$^{-1}$ Mpc$^{-3}$)')
plt.xlabel('Redshift')
plt.legend()
plt.show()

'''

# CSFRD against lookback time plot - for SFR_MsunPerYrs_in_r5pkpc_200Myrs data

def lookback(z, omega_M, omega_L, h):
    '''
    Calculates the lookback time according to a specific cosmology.

    Parameters:
    z : float
        The redshift at which the lookback time is to be calculated
    omega_M : float
        The matter density parameter (0.30897)
    omega_L : float
        The dark energy density parameter (0.6911)
    h : float
        The hubble parameter (0.6774)
    '''
    def f(x):
        a = np.sqrt(omega_M*(1+x)**3 + omega_L)
        return 1/((1+x)*a)
    t_hubble = (1/(100*h))*3.0856776*10**19
    return t_hubble*scipy.integrate.quad(f, 0, z)[0]/(60*60*24*365.2388526*1e9)

LB_time = []
for redshift in redshifts: 
    LB_time.append(lookback(redshift, 0.30897, 0.6911, 0.6774))

plt.plot(LB_time, sfr, label='TNG')
plt.plot(LB_time, empirical, label='Empirical')
plt.yscale('log')
plt.ylabel('CSFRD ($M_\odot$ yr$^{-1}$ Mpc$^{-3}$)')
plt.xlabel('Lookback Time (Gyr)')
plt.legend()
plt.show()
