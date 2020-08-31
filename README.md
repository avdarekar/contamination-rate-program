# contamination-rate-program

## Description 
I attempted to create a program that calculates the contamination rates of stars using Gaia data.

## Table of Contents
- Progress
- File Descriptions
- Obtaining Data

## Progress
I have a program that calculates the contamination rate for a star (ContaminationRate.py). However, the numbers this program returns does not exactly match the true contamination rate value for a star. This could be an aperture issue. The FindBestAperture.py program finds the best aperture for each star in contratiolessthan10.xlsx and writes that best aperture value to the contratiolessthan10.xlsx file. This file might contain another aperture that might work better for these stars (the current aperture value that I've been using is 40 arc seconds). I believe that once the correct aperture is found, the numbers returned by my contamination rate program will match those in the MAST database. 

## File Descriptions
- ContaminationRate.py: This program attempts to calculate the contamination rate value of a star.
- ContaminationRateSampleOutput: This screenshot shows the output of the ContaminationRate.py program. 
- ContaminateRatePlotVer2.py: This program calculates the contamination rate values of random stars and obtains the true contamination rate values of these stars. It then plots these values with the x-axis being the calculated contamination rates and the y-axis being the true contamination rates.

- ContaminationRatePlot.py: This program creates a plot of calculated contamination rate values and true contamination rate values for stars.
- ContaminationRatePlot: This graph shows the contamination rate values that my program calculated and the true contamination rate values for each star.
- ContaminationRatePlot2: This graph is the same as the ContaminationRatePlot graph except zoomed in. 

- FractionalDeviationPlot.py: This program calculate the contamination rate values and obtains the true contamination rate values for random stars. It calculates the fractional deviation and plots this with the true contamination rate values.
- Fractional Deviation MAST Cont Ratio plot: This is the graph of the fractional deviations and the true contamination rate values. 

- FindBestAperture.py: This program specifically looks at stars with a true contamination rate values of < 10. It calculates the contamination rate value for multiple apertures (40-200) and finds the best aperture (the aperture that gives a calculated contamination rate value that is closest to its true contamination rate value) for a star and writes it to contratiolessthan10.xlsx.

- my_contratio vs mast_contratio 2: This graph has the calculated contamination rates on the x-axis and the true contamination rate values on the y-axis. It only shows stars with a true contamination rate value of less than 2.  
- my_contratio vs mast_contratio 10: This graph has the calculated contamination rates on the x-axis and the true contamination rate values on the y-axis. It only shows stars with a true contamination rate value of less than 10. 

- PrintZipArray.py: This program creates a zip array with the ra, dec, true contamination rate, and calculated contamination rate. This program just organizes the data to make it easier to read.
- PrintZipArrayForContRatioLess10.py: Very similar ot the PrintZipArray.py program except it writes every column to an excel file.

- MASTSearch.py: This program does a simple MAST search given a star's coordinates. It finds the true contamination rate value of a star.
- contamination_ratio_test: This file compares random stars' true contamination rate versus the contamination rate my program outputted.

- contratiolessthan10.xlsx: This file contains stars with true contamination rate values that are less than 10. It also contains a column for best aperture.
- random_ra_dec.xlsx: This file contains the coordinates of random stars. 

## Obtaining Data
The data was obtained from [MAST](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) and the [Gaia archive](https://gea.esac.esa.int/archive/).
