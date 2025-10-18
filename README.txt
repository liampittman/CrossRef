===============================================================================
               Creating and Using Cross Reference Files - README               
===============================================================================

AUTHOR INFORMATION:
- Author: William Pittman
- Contact: w651749@usm.edu
- Created: [2025-10-17]
- Last Modified: [2025-10-17]
- Version: 1.0
- License: MIT (code), CC BY 4.0 (original data)

===============================================================================
DESCRIPTION:
This project demonstrates the use of geographic and population cross-reference 
files via an analysis of flash flood events by county.

===============================================================================
PROJECT STRUCTURE:
- data/         : Raw input data files
- FlashFloods/  : ArcGIS Map Project using the processed output files
- output/       : Processed output files
- python/       : Python scripts and notebooks
  └── CrossRef.py     : Main data wrangling script
  └── CrossRef.ipynb  : Notebook version of the script
- resources/    : Geographic cross-reference files (geoIDs, FIPS, etc.)
- README.txt    : Documentation and usage instructions

===============================================================================
USAGE:
The output folder contains pre-generated files, but the process can be
replicated:

1. Navigate to the 'python/' directory.
2. Run the script:
   python CrossRef.py
3. Output files will be saved to 'output/', unless modified in the script.

===============================================================================
DEPENDENCIES:
- Python 3.x
- pandas
- numpy

===============================================================================
INPUT DATA (data/):
These files contain data that are merged and cross referenced with geoID files.

- Flash Floods:
  NOAA National Centers for Environmental Information. (2024).
  *StormEvents_details-ftp_v1.0_d2023_c20240201.csv* [Data set].
  NOAA. https://www.ncei.noaa.gov/stormevents/.

- Population Estimates:
  U.S. Census Bureau, Population Division. (2025). Annual Estimates of the 
  Resident Population for Counties: April 1, 2020 to July 1, 2024 (CO-EST2024-
  POP). Vintage 2024. Retrieved from https://www.census.gov/data/tables/time-
  series/demo/popest/2020s-counties-total.html.

- TIGER/Line Shapefiles:
  U.S. Census Bureau. (2023). 2023 TIGER/Line Shapefiles [Geospatial data 
  files]. U.S. Department of Commerce. Retrieved from https://www.census.gov/
  geographies/mapping-files/time-series/geo/tiger-line-file.2023.html#list-tab-
  790442341.

===============================================================================
FLASH FLOODS (FlashFloods/):
This folder contains a companion ArcGIS Pro map project that visualizes flash
flood data (by county for the country and by county per capita for the state of
Mississippi) using processed outputs and TIGER/Line shapefiles

Files used:
- output/us_flash-floods_count.csv  : U.S. county-level flash flood counts
- output/ms_ff-cnt_pop.csv:         : Mississippi flash floods per capita
- data/tl_2023_us_county:           : TIGER/Line shapefiles for U.S. counties

Symbology:
Choropleth maps using graduated color scales
- U.S.  : flash flood counts (absolute)
- Miss. : flash floods per capita (normalized)

Styling:
- Color ramps are designed to reflect statistical distribution

===============================================================================
OUTPUT DATA (output/):
- Format: CSV
- Files:
  - ms_ff-cnt_pop.csv         : Mississippi flash floods per capita by county
  - us_flash-floods_count.csv : U.S. flash flood counts by county

===============================================================================
CODE (python/):
Contains two versions of the code that generate the same outputs:
- CrossRef.py      : Python script
- CrossRef.ipynb   : Jupyter notebook

===============================================================================
RESOURCE FILES (resources/):
Contains geographic identifiers and district variations to facilitate data
merging and mapping.

All files in this folder were created by the author.

===============================================================================
LICENSE:
This project is licensed under the MIT License for all original code. See the
LICENSE file for full terms.

Original data files created by the author are licensed under the 
Creative Commons Attribution 4.0 International (CC BY 4.0). 
You may use, share, and adapt these files with appropriate credit.

Source data from the NOAA NCEI Storm Events Database, U.S. Census Bureau
Population Division, and TIGER/Line Shapefiles are public domain. 
Attribution is appreciated where feasible.

Please cite this project and its data sources appropriately in any derivative
work or publication.

Preferred citation format:
Pittman, W. (2025). Cross-Referenced Flash Flood and Population Data by County
[Data set and code]. Unpublished. Available from author upon request.

===============================================================================
NOTES:
- The file 'StormEvents_details-ftp_v1.0_d2023_c20240201.csv' has been renamed
  'StormEvents.csv'.

===============================================================================
