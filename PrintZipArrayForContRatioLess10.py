#Very similar ot the PrintZipArray.py program except it writes every column to an excel file.
from astroquery.mast import Catalogs
import numpy as np
from astropy.coordinates import SkyCoord as coord
import astropy.units as un
from astroquery.gaia import Gaia
import matplotlib.pyplot as plt
from xlrd import open_workbook
import xlsxwriter
 
bench = open_workbook('/Users/adarekar/Desktop/UNCResearch/TESS/random_ra_dec.xlsx')
sheet = bench.sheet_by_index(0)

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
        
            
                   


ra_dec_contratio = zip(ra_asc, declination, mast_contratio, my_contratio)


#write all 4 columns from zip array to excel file 
workbook = xlsxwriter.Workbook('contratiolessthan10.xlsx') 
  

worksheet = workbook.add_worksheet() 
  

worksheet.write(0,0, 'ra') 
worksheet.write(0,1, 'dec') 
worksheet.write(0,2, 'mast contratio') 
worksheet.write(0,3, 'my contratio') 


row = 1

for ra1 in ra_asc:
    worksheet.write(row, 0, ra1)
    row +=1

row = 1
for dec1 in declination:
    worksheet.write(row, 1, dec1)
    row += 1

row = 1
for mastcontratio in mast_contratio:
    worksheet.write(row, 2, mastcontratio)
    row += 1

row = 1
for mycontratio in my_contratio:
    worksheet.write(row, 3, mycontratio)
    row += 1

#for ra,dec,mastcontratio,mycontratio in ra_dec_contratio:
    #worksheet.write(row, 0, ra)
    #worksheet.write(row, 1, dec)
    #worksheet.write(row, 2, mastcontratio)
    #worksheet.write(row, 3, mycontratio)
    #row += 1
        
workbook.close() 




  

 
