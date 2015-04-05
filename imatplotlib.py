import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pygrib

filename   = "file.grib2"
grbs       = pygrib.open('/data/' + filename)
grb        = grbs[2]
data       = grb.values
datac      = data*0.01
lats, lons = grb.latlons()

fig = plt.figure()
m = Basemap(projection='stere',lon_0=5,lat_0=90.0,\
            llcrnrlon=-25.0,urcrnrlon=60.0,llcrnrlat=30.0,urcrnrlat=60.0,resolution='l')

x, y = m(lons, lats)

levs = range(940,1065,5)
S1=plt.contour(x,y,datac,levs,linewidths=0.5,colors='b')
plt.clabel(S1,inline=1,inline_spacing=0,fontsize=8,fmt='%1.0f',colors='b')

m.drawmapboundary(fill_color='w')
m.drawcoastlines(linewidth=0.2)

plt.savefig('test.png', bbox_inches='tight',pad_inches=0.05, dpi=100)