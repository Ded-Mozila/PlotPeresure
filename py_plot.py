#!/usr/bin/env python
#coding=utf-8
import matplotlib.image as mpimg
# import numpy as np
from pylab import *
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import os
levs = range(840, 1200, 5)


def openFile(str):
    fd = open(str, 'r')
    for i in range(5):
        s = fd.readline()
    mat = []
    for i in fd:
        mt = np.array([float(field) for field in i.strip().lstrip('[').rstrip(']').split()],dtype=float)
        mat.append(mt)
    fd.close()
    return mat


def dirList(str):
    lt = os.listdir(str)
    return lt


def absl(lon):
    mat = []
    for x in lon:
        mt = []
        for y in x:
            if y < 0:
                mt.append(y+360)
            else:
                mt.append(y)
        mat.append(mt)
    return mat


def printlon(ar):
    for x in ar:
        for y in x:
            if y < 0:
                print y
    return 0


def strInt(index):
    if index < 10:
        return "0" + str(index)
    return str(index)


def main():
    img = mpimg.imread('img_100.png')
    levs = range(840, 1200, 5)
    fs = open("settings.txt")
    str = fs.readline()
    fs.close()
    lt = dirList(str)
    lat = openFile("lat.grd")
    lon = absl(openFile("lon.grd"))
    # printlon(lon)
    for name in lt:
        os.makedirs(name+"/gif/", 0755)
        file_dir = dirList(str+'/'+name)
        for q in file_dir:
            f_dir = dirList(str+'/'+name+"/"+q)
            print str+'/'+name+"/"+q
            for x in f_dir:
                if x.find("presure") != -1:
                    print x
                    presure = openFile(str+'/'+name+"/"+q+"/"+x)
                    fig = plt.figure()
                    plt.clf()
                    plt.imshow(img, extent=[102, 173, 14, 68])
                    CS = plt.contour(lon, lat, presure, levs, extent=[102, 173, 14, 68], origin='lower', linewidths=1, antialiased=True, nchunk=0.5, colors='black')
                    plt.clabel(CS, inline=1, inline_spacing=0, fontsize=8, fmt='%2.0f', colors='black')
                    plt.title('Simplest default with ' + x)
                    plt.savefig(name + '/gif/' + x + '.png', pad_inches=0.05,  dpi=180, figsize=[800, 600])
                    plt.close(fig)
    return 0


def one_file(str):
    from mpl_toolkits.basemap import Basemap
    import numpy as np
    import matplotlib.pyplot as plt
    lat = openFile("lat.grd")
    lon = absl(openFile("lon.grd"))
    # llcrnrlat, llcrnrlon, urcrnrlat, urcrnrlon
    # are the lat/lon values of the lower left and upper right corners
    # of the map.
    # resolution = 'c' means use crude resolution coastlines.
    plt.figure()
    m = Basemap(projection='cyl', llcrnrlat=13.5, urcrnrlat=75.3, llcrnrlon=102, urcrnrlon=360-150.164, resolution='i')
    m.drawcoastlines()
    m.drawparallels(np.arange(-40,  61.,  2.))
    m.drawmeridians(np.arange(-20.,  21.,  2.))
    m.fillcontinents(color='coral',  lake_color='aqua')
    m.drawstates(linewidth=0.5,  linestyle='solid',  color='k',  antialiased=1,  ax=None,  zorder=None)
    # draw parallels and meridians.
    m.drawmapboundary(fill_color='aqua')
    # img=mpimg.imread('img_100.png')
    levs = range(840,  1200,  5)
    presure = openFile(str)
    # plt.imshow(img, extent=[0, 500, 0, 400])
    CS = m.contour(lon,  lat,  presure,  levs,  origin='lower',  linewidths=1,  antialiased=True,  nchunk=0.5,  colors='black')
    m.clabel(CS,  inline=1,  inline_spacing=0,  fontsize=8,  fmt='%2.0f',  colors='black')
    m.title('Simplest default with ')
    #plt.title('Simplest default with ' + x)
    #plt.savefig(name+'/gif/'+ x + '.png')
    plt.show()
    return 0


def one():
    from mpl_toolkits.basemap import Basemap
    import matplotlib.pyplot as plt
    m = Basemap(projection='cass',  resolution='i', llcrnrlon=102.25, llcrnrlat=13.5, urcrnrlon=-180.0, urcrnrlat=75.3, lon_0=140,  lat_0=50)
    m.drawcoastlines()
    m.fillcontinents(color='coral', lake_color='aqua')
    # draw parallels and meridians.
    # m.drawparallels(np.arange(-90., 91., 30.))
    # m.drawmeridians(np.arange(-180., 181., 60.))
    m.drawmapboundary(fill_color='aqua')
    plt.show()


def two():
    from mpl_toolkits.basemap import Basemap
    import numpy as np
    import matplotlib.pyplot as plt
    # llcrnrlat, llcrnrlon, urcrnrlat, urcrnrlon
    # are the lat/lon values of the lower left and upper right corners
    # of the map.
    # resolution = 'c' means use crude resolution coastlines.
    m = Basemap(projection='cyl', llcrnrlat=13.5, urcrnrlat=75.3, llcrnrlon=102, urcrnrlon=360-150.164, resolution='i')
    m.drawcoastlines()
    m.drawcountries()
    m.fillcontinents(color='#e8eb8a', lake_color='aqua')
    m.drawstates(linewidth=0.5,  linestyle='solid',  color='k',  antialiased=1,  ax=None,  zorder=None)
    # draw parallels and meridians.
    m.drawmapboundary(fill_color='aqua')

    presure = openFile("/home/aleks/Aleksander/study/Credential/Project/ReceiveInformation_1/FILE_Test/2013.12.11/22/smth9/05/presure_00.txt")
    plt.figure()
    plt.clf()
    lat = openFile("lat.grd")
    lon = absl(openFile("lon.grd"))
    x = np.array(lat)
    y = np.array(lon)
    z = np.array(presure)
    lat_min = min(lat)
    lat_max = max(lat)
    lon_min = min(lon)
    lon_max = max(lon)
    xi = np.linspace(lat_min, lat_max, ngrid)
    yi = np.linspace(lon_min, lon_max, ngrid)
    zi = griddata(x, y, z, xi, yi)

    # lon,  lats = m.makegrid(lon,  lat)
    # x,  y = m(lon,  lat)

    CS = m.contour(xi, yi, zi, 20, linewidths=1)
        # levs, extent=[102, 173, 14, 68], zorder=4, alpha=0.6, cmap='RdPu', origin='lower', linewidths=1, antialiased=True, nchunk=0.5, colors='black')
                            # CS = plt.contour(presure, levs,
    m.colorbar(CS, location='bottom', pad="5%")
    plt.title("Equidistant Cylindrical Projection")
    plt.show()


def tree():
    from mpl_toolkits.basemap import Basemap
    lat = openFile("lat.grd")
    lon = absl(openFile("lon.grd"))
    # lon = openFile("lon.grd")
    data = openFile("/home/aleks/Aleksander/study/Credential/Project/ReceiveInformation_1/FILE_Test/2013.12.11/22/smth9/05/presure_00.txt")
    map = Basemap(projection='cyl', llcrnrlat=18, urcrnrlat=74, llcrnrlon=102, urcrnrlon=360-170, resolution='i')
    # Отрисовка городов
    # labels = ['Sitka', 'Baranof Warm Springs', 'Port Alexander']
    # for label, xpt, ypt in zip(labels, x, y):
    #     plt.text(xpt, ypt, label)
    map.drawcoastlines(linewidth=0.5, color='grey')
    map.drawcountries(linewidth=1, color='purple')
    map.fillcontinents(color='#FFFCC4', lake_color='aqua')
    map.drawstates(linewidth=0.5,  linestyle='solid',  color='grey',  antialiased=1,  ax=None,  zorder=None)
    # draw parallels and meridians.
    map.drawparallels(np.arange(-90., 120., 5.), labels=[1,0,0,0], color="grey", fontsize=6,labelstyle='g/t', linewidth=0.5, dashes=[0.2, 4]) # draw parallels
    map.drawmeridians(np.arange(0., 420., 5.), labels=[0,0,0,1], color="grey", fontsize=6, linewidth=0.5, dashes=[0.2, 4]) # draw meridians
    map.drawmapboundary(fill_color='aqua')
    x, y = map(lon, lat)
    lons = [135.08379, 126.65, 131.87353, 140.46778, 139.69171, 158.65076, 113.50087, 129.73306, 150.80347, 126.9784, 137.00995, 142.73603]
    lats = [48.48272, 45.75, 43.10562, 37.75, 35.6895, 53.04444, 52.03171, 62.03389, 59.5638, 37.566, 50.55034, 46.95407]
    xP, yP = map(lons, lats)
    map.plot(xP, yP, 'ro', markersize=2)
    point_lables = [u'Хабаровск', u'Харбин', u'Владивосток', u'Фукуcима', u'Токио', u'П-Камчатский', u'Чита', u'Якутск', u'Магадан', u'Сеул', u'К-на-Амере', u'Ю-Сахалинск']
    for label, xpt, ypt in zip(point_lables, xP, yP):
        plt.text(xpt+0.5, ypt+0.01, label,color='r', fontsize=5)
    CS = plt.contour(x, y, data, levs,  origin='lower',  linewidths=0.75,  antialiased=True,  nchunk=0.5,  colors='black')
    plt.clabel(CS, inline=1, inline_spacing=0.1, fontsize=7, fmt='%1.0f', colors='b')
    map.drawmapboundary(fill_color='w')
    map.drawcoastlines(linewidth=0.2)
    plt.title(u'ПРОГРНОЗ ПРИЗ. ДАВЛЕНИЯ')
    plt.savefig('example.png', pad_inches=0.05, dpi=400)
# one_file("/home/aleks/Aleksander/study/Credential/Project/ReceiveInformation_1/FILE10/2013.12.11/presure_00.txt")
# main()
# one()
# two()
tree()
