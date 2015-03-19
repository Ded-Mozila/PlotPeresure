
from pylab import *
import re
def openFile(str):
	fd = open(str,'r')
	for i in range(5):
		s = fd.readline()
	mat = []
	for i in fd:
		mt =[float(field) for field in i.strip().lstrip('[').rstrip(']').split()]
		mat.append(mt)
	fd.close()
	return mat	
def main():
	lat = openFile("/home/aleks/Aleksander/study/Credential/sasha_diplom_data/2013.12.11/lat.grd")
	lon = openFile("/home/aleks/Aleksander/study/Credential/sasha_diplom_data/2013.12.11/lon.grd")
	presure = openFile("/home/aleks/Aleksander/study/Credential/Project/ReceiveInformation_1/FILE/presure_0.txt")
	plt.figure()
	CS = plt.contour(presure,antialiased = True)
	plt.clabel(CS, inline=1, fontsize=10)
	plt.title('Simplest default with labels')

	plt.figure()
	CS = plt.contour(presure)
	plt.clabel(CS, inline=1, fontsize=10)
	plt.title('Simplest default with labels')
	plt.show()
	return 0
main()