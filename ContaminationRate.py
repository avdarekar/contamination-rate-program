#This program attempts to calculate the contamination rate value of a star. 


#import libraries
import numpy as np
from astropy.coordinates import SkyCoord as coord
import astropy.units as un
from astroquery.gaia import Gaia

#query object based on ra and dec coordinates
ra = "344.106083696"
dec = " -47.797998307"
c = coord(ra, dec, unit = (un.deg, un.deg), frame='icrs')
r = Gaia.query_object_async(c, radius = 40*un.arcsecond)

print(r['phot_g_mean_flux'])
print(r['dist']*3600)

#get the target star's distance that is the closest to the ra and dec coordinates
targetdist = min(r['dist']*3600)
print(targetdist)

#add up all fluxes of the stars
fluxsum = 0; 
for flux in r['phot_g_mean_flux']:
    fluxsum+= flux

print(fluxsum)

#get the target star's index value 
targetindex = 0
for distance in (r['dist']*3600):
    print(distance)
    print(targetindex)
    if (targetdist == distance):
        break
    else:
        targetindex += 1
        

if (targetindex != 0):
    targetindex = targetindex - 1

print(targetindex)

#get the target star's flux value 
targetflux = r['phot_g_mean_flux'][targetindex]
print(targetflux)

#get the contamination flux value 
contaminateflux = fluxsum - targetflux
print(contaminateflux)

#calculate the contamination rate value
contaminaterate = contaminateflux/targetflux


print("ra: ")
print(ra)
print("dec: ")
print(dec)
print("contamination rate: ")
print(contaminaterate)




