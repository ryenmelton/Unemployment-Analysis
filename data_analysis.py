import numpy as np
import pandas as pd

# Function takes as input a file containing x years
# of national unemployment data and returns the average
def national_average(filename):
    df = pd.read_excel(filename[0])
    unempRates = df['Unemployment'].to_numpy()
    avg = np.mean(unempRates)
    return avg

# Function takes as an input the files containing state unemployment rates
# Outputs the average rate over the timespan, as well as returns only the
# states with unemployment higher than national average
def state_average(filenames, natAvg):
    rawRates = np.zeros((51,5))
    i = 0
    for file in filenames:
        df = pd.read_excel(file)
        rawRates[:,i] = df['Unemployment'].to_numpy()
        i += 1
    states = df['State'].to_numpy()
    stateAvg = np.mean(rawRates, axis=1)
    subsetInds = np.argwhere(stateAvg >= natAvg)
    subsetStates = states[subsetInds]
    subsetAvg = stateAvg[subsetInds]
    return subsetAvg, subsetStates

# Function takes as an input the files containing county level unemployment
# rates for all counties belonging in the target states found in the 
# state_average() call, then extracts the target counties by flagging
# all counties with unemployment levels higher than their state
def county_average(filenames, subsetAvg, subsetStates):
    temp =  pd.read_excel(filenames[0])
    counties = temp['County'].to_numpy()
    statesCounty = temp['State'].to_numpy()
    temp = None
    rawRates = np.zeros((len(counties), len(filenames)))
    i = 0
    for file in filenames:
        df = pd.read_excel(file)
        rawRates[:,i] = df['Unemployment'].to_numpy()
        i += 1
    countyAvg_raw = np.mean(rawRates, axis=1)

    targetCounties = []
    targetAvg = []
    i = 0
    for state in subsetStates:
        temp_inds = np.argwhere(statesCounty == state)
        for ind in temp_inds:
            if (countyAvg_raw[ind[0]] >= subsetAvg[i]):
                targetCounties.append(counties[ind[0]])
                targetAvg.append(countyAvg_raw[ind[0]])
        i += 1
    return targetAvg, targetCounties


national_file = ['Excel/national_records.xlsx']
state_files = ['Excel/states_2015.xlsx', 'Excel/states_2016.xlsx', 'Excel/states_2017.xlsx', 'Excel/states_2018.xlsx', 'Excel/states_2019.xlsx']
county_files = ['Excel/county_2015.xlsx', 'Excel/county_2016.xlsx', 'Excel/county_2017.xlsx', 'Excel/county_2018.xlsx', 'Excel/county_2019.xlsx']


nationalAverage = national_average(national_file)
stateAverages, stateList = state_average(state_files, nationalAverage)
countyAverages, countyList = county_average(county_files, stateAverages, stateList)