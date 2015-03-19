# from numpy import reshape

from pylab import *
import numpy as np

# from pylab import *
def openFile(str):
	fd = open(str,'r')
	s = []
	for i in range(5):
		s += fd.readline()
	table_lines = fd.readlines()
	fd.close()
	mat = {}
	j = 0
	for i in table_lines:
		mat[j] = float(i.split("    "))
		j = j + 1
	return mat	
def main():
	lat = openFile("/home/aleks/Aleksander/study/Credential/sasha_diplom_data/2013.12.11/lat.grd")
	lon = openFile("/home/aleks/Aleksander/study/Credential/sasha_diplom_data/2013.12.11/lon.grd")
	presure = openFile("/home/aleks/Aleksander/study/Credential/Project/ReceiveInformation_1/FILE/presure_0.txt")
	plt.figure()
	# X , Y = np.meshgrid(lon, lat)
	CS = plt.contour(lat,lon,presure)
	plt.clabel(CS, inline=1, fontsize=10)
	plt.title('Simplest default with labels')
	# clabel(cset,fmt="%1.1f",fontsize=9)
	#savefig('pylab.eps')
	return 0
main()