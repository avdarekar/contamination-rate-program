#This program specifically looks at stars with a true contamination rate values of < 10. It calculates the contamination rate value for multiple apertures (40-200) and finds the best aperture (the aperture that gives a calculated contamination rate value that is closest to its true contamination rate value) for a star and writes it to an excel file.



#import libraries
import numpy as np
import openpyxl
from astropy.coordinates import SkyCoord as coord
import astropy.units as un
from astroquery.gaia import Gaia



aperture = []
all_mycontratio = []



for i in range(81):
    aperture.append(40+(2*i))

#calculates contamination rates for different apertures for a specific star
ra = "338.566883978"
dec = " -2.39110160542"
mast_contratio = "0.024454223"
        
for x in aperture:
       
    c = coord(ra, dec.strip(), unit = (un.deg, un.deg), frame='icrs')
    r = Gaia.query_object_async(c, radius = x*un.arcsecond)
        
    targetdist = min(r['dist']*3600)
        
    fluxsum = 0
        
    for flux in r['phot_g_mean_flux']:
            
        fluxsum+= flux
 
    targetindex = 0
        
    for distance in (r['dist']*3600):
            
        if (targetdist == distance):
                
            break
            
        else:
                
            targetindex += 1
            
    if (targetindex != 0):
        
        targetindex = targetindex - 1
            
    targetflux = r['phot_g_mean_flux'][targetindex]
        
    contaminateflux = fluxsum - targetflux
        
    contaminaterate = contaminateflux/targetflux
        
    all_mycontratio.append(contaminaterate)

#take difference of true contratio value and all values in the my contratio array
diff = []



for i in all_mycontratio:
    diff.append(abs(float(i) - float(mast_contratio)))
    


best_diff = min(diff)

print(best_diff)
#find the aperture value that matches the smallest difference
best_appindex = 0

for w in range(len(diff)):
    
    if (best_diff == diff[w]):
        
        best_appindex = w
        

print(best_appindex)

print(aperture[best_appindex])



#write best apperture to contratiolessthan10 file

location = '/Users/adarekar/Desktop/UNCResearch/TESS/contratiolessthan10.xlsx'
wb = openpyxl.load_workbook(location)
ws = wb['Sheet1']
ws['E140'] = aperture[best_appindex]

wb.save(location)
wb.close
    
   
