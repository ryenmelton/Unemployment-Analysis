import numpy as np

# counties = list of all counties
# statesCounty = list of all states corresponding to the counties
counties = np.array(['1','2','3','4','5','6','7','8'])
statesCounty = np.array(['A','A','A','B','C','D','E','F'])
subsetStates = np.array(['B','D','A'])

subCounties = []
for i in range(len(subsetStates)):
    temp_inds = np.argwhere(statesCounty == subsetStates[i])
    for ind in temp_inds:
        print(ind)
        subCounties.append(counties[ind[0]])

print(subCounties)

#print(inds)
#print(indices)
#print(x[indices])


# 1,3,0,6,7
