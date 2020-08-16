#This program creates a zip array with the ra, dec, true contamination rate, and calculated contamination rate. This program just organizes the data to make it easier to read.

#import libraries
from astroquery.mast import Catalogs
import numpy as np
from astropy.coordinates import SkyCoord as coord
import astropy.units as un
from astroquery.gaia import Gaia
import matplotlib.pyplot as plt
from xlrd import open_workbook

#open excel file with random star coordinates
 
bench = open_workbook('/Users/adbreeze13/Desktop/UNCResearch/TESS/random_ra_dec.xlsx')
sheet = bench.sheet_by_index(0)

#put the ra and dec columns in the excel file into 2 arrays 

ra_arr = []
dec_arr = []
for name in bench.sheet_names():
    sheetnew = bench.sheet_by_name(name)
    for row in range(1, sheet.nrows-1):
        ra_arr.append(sheetnew.cell_value(row, 0))
        dec_arr.append(sheetnew.cell_value(row,1))


mast_contratio = []
my_contratio = []
ra_asc = []
declination = []

#calculate contamination rates of stars and obtain the true contamination rate values for these stars

for x in range(len(ra_arr)):
    
    ra = str(ra_arr[x])
    
    dec = " " + str(dec_arr[x])
    
    data = Catalogs.query_object(ra+dec, catalog = "CTL")
    
    if (data['dstArcSec'][0] <= 3 and data['contratio'][0] < 10):
        ra_asc.append(ra)
        declination.append(dec)
        
        mast_contratio.append(data['contratio'][0])
        
        c = coord(ra, dec.strip(), unit = (un.deg, un.deg), frame = 'icrs')
        
        r = Gaia.query_object_async(c, radius = 40*un.arcsecond)
        
        targetdist = min(r['dist']*3600)
        
        fluxsum = 0
        
        for flux in r['phot_g_mean_flux']:
            
            fluxsum += flux
            
        targetindex = 0
        
        for distance in (r['dist']*3600):
            
            if (targetdist == distance):
                
                break
            
            else:
                
                targetindex +=1
                
        if (targetindex != 0):
            
            targetindex = targetindex -1
            
        targetflux = r['phot_g_mean_flux'][targetindex]
        
        contaminateflux = fluxsum - targetflux
        
        contaminaterate = contaminateflux/targetflux
        
        my_contratio.append(contaminaterate)
        
            
                   

#zip array
ra_dec_contratio = zip(ra_asc, declination, mast_contratio, my_contratio)





  

 
