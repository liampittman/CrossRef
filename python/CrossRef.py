
# =============================================================================
# File Name:        CrossRef.py
# Description:      Demonstrates usage of Cross Reference files
# Author:           William Pittman
# Created:          2025-10-17
# Last Modified:    2025-10-17
# Version:          1.0
# Python Version:   3.10
# Dependencies:     pandas
# =============================================================================

# =============================================================================
#                            Dependencies
# =============================================================================

import pandas as pd

# =============================================================================
#                            Import CSVs
# =============================================================================

se = pd.read_csv('../data/StormEvents.csv')                     # Storm Events
ms_pop = pd.read_csv('../data/2024_co-est-pop_28.csv')          # MS Co. Pop.
us = pd.read_csv('../resources/US_County_CrossReference.csv')   # US Co. X-Ref
ms = pd.read_csv('../resources/MS_County_CrossReference.csv')   # MS Co. X-Ref

# =============================================================================
#                            Formatting
# This section does a little minor housekeeping with cross reference and data 
# files
# =============================================================================

# Make FIPS conform to a five digit and/or string format
us['FIPS'] = us['FIPS'].astype(str).str.zfill(5)
ms['FIPS'] = ms['FIPS'].astype(str)

# Renames a column for later use
ms_pop.rename(columns={'District':'NAME'}, inplace=True)

# =============================================================================
#                            Flash Flood Count
# This section creates a dataframe that has a count of flash floods for all 
# FIPS where they have been reported.
# =============================================================================

# Creates a dataframe holding only rows where type is county
se_counties = se[se['CZ_TYPE'] == 'C'].reset_index(drop=True)

# Creates a 5-digit FIP code from State and County FIPS
se_counties['FIPS'] = (
    se_counties['STATE_FIPS'].astype(str).str.zfill(2) +
    se_counties['CZ_FIPS'].astype(str).str.zfill(3)
)

# Creates a dataframe that counts flash floods by FIPS code
ff_counts = (
    se_counties[se_counties['EVENT_TYPE'] == 'Flash Flood']
    .groupby('FIPS')
    .size()
    .reset_index(name='FlashFloodCount')
)


# =============================================================================
#                  Cross Reference FIPS with geoIDs for Mapping 
# This section attaches flash flood counts to the US County Cross Reference
# file and fills null values with 0              
# =============================================================================
ff_geoID = (
    us.merge(ff_counts, on='FIPS', how='left')
    .fillna({'FlashFloodCount': 0})
)

ff_geoID['FlashFloodCount'] = ff_geoID['FlashFloodCount'].astype(int)

# =============================================================================
#                            MS per Capita Flash Floods
# This section combines flash flood data and county population for Mississippi
# to calculate per Capita flash floods in Mississippi counties and merges this
# with geoIDs for mapping
# =============================================================================

# Adds population data to the ms CrossRef file
ms = ms.merge(ms_pop[['NAME', 'est_2024']], on='NAME', how='left')

# Creates a new dataframe that adds flash flood counts to the geoIDs and pop 
# data in the MS Cross Reference file
ff_MSgeoID = (
    ms.merge(ff_counts, on='FIPS', how='left').fillna({'FlashFloodCount':0})
)
ff_MSgeoID['FlashFloodCount'] = ff_MSgeoID['FlashFloodCount'].astype(int)

# Adds a column calculating Flash Floods per Capita
ff_MSgeoID['FFper100k'] = round(
    (ff_MSgeoID['FlashFloodCount'] / ff_MSgeoID['est_2024']) * 100000,
    2
)

# =============================================================================
#                            Export CSVs
# =============================================================================

# Creates a US csv
ff_geoID.to_csv('../output/us_flash-floods_count.csv', index=False)

# Creats a MS csv
ff_MSgeoID.to_csv('../output/ms_ff-cnt_pop.csv', index=False)