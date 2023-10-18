import illustris_python as il
import matplotlib.pyplot as plt

basePath = './Illustris-3/output/'
fields = ['SubhaloMass','SubhaloSFRinRad']
subhalos = il.groupcat.loadSubhalos(basePath,135,fields=fields)


# star formation rate against total mass

mass_msun = subhalos['SubhaloMass'] * 1e10 / 0.704
#subhalos.keys()
#subhalos['SubhaloMass'].shape  # gives size of one of the arrays
plt.plot(mass_msun, subhalos['SubhaloSFRinRad'], '.', markersize = 2)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Total Mass [$M_\odot$]')
plt.ylabel('Star Formation Rate [$M_\odot / yr$]')
plt.show()

# gas fraction (gas mass over total baryonic mass) for five most massive 
#   central subhalos

#ptNumGas = il.snapshot.partTypeNum('gas') # 0
#ptNumStars = il.snapshot.partTypeNum('stars') # 4
#for i in range(5):
    #all_fields = il.groupcat.loadSingle(basePath,135,subhaloID=GroupFirstSub[i])
    #gas_mass   = all_fields['SubhaloMassInHalfRadType'][ptNumGas]
    #stars_mass = all_fields['SubhaloMassInHalfRadType'][ptNumStars]
    #frac = gas_mass / (gas_mass + stars_mass)
    #print GroupFirstSub[i], frac

'''
# merger tree - total subhalo mass against snapshot number

fields = ['SubhaloMass','SubfindID','SnapNum']
start = 100
for i in range(start, start+5):
    tree = il.sublink.loadTree(basePath, 135, GroupFirstSub[i], fields=fields, 
                               onlyMPB=True)
    plt.plot(tree['SnapNum'],tree['SubhaloMass'],'-')
plt.yscale('log')
plt.xlabel('Snapshot Number')
plt.ylabel('Total Subhalo Mass [code units]')
# dips in snapshots due to 'subhalo switching problem'
# downward then sudden increase in snapshot is a merger signature

# merger tree - find number of past mergers of a subhalo, above a mass ratio 
#   threshold (ratio of max past stellar mass of the two progenitors)

ratio = 1.0/5.0
fields = ['SubhaloID','NextProgenitorID','MainLeafProgenitorID','FirstProgenitorID','SubhaloMassType']
for i in range(start, start+5):
    tree = il.sublink.loadTree(basePath, 135, GroupFirstSub[i], fields=fields)
    numMergers = il.sublink.numMergers(tree, minMassRatio=ratio)
    print GroupFirstSub[i], numMergers


# snapshot data
'''