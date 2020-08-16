#This program does a simple MAST search given a star's coordinates. It finds the true contamination rate value of a star.

#import library
from astroquery.mast import Catalogs

#searches MAST for a star and gets its contamination rate value
ra1 = "200.908342878"
dec1 = " 30.4552802786" 
data1 = Catalogs.query_object(ra1+dec1, catalog = "CTL")
m = []
if(data1['dstArcSec'][0] < 3):
    m.append(data1['contratio'][0])

print(m)
#ra2 = "245.844749932"
#dec2 = "-52.2043315818" 
#data2 = Catalogs.query_object(ra2+dec2, catalog = "CTL")

#ra3 = "268.217882965"
#dec3 = "-30.4099326617" 
#data3 = Catalogs.query_object(ra3+dec3, catalog = "CTL")


