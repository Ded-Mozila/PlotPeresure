# from numpy import reshape
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
		mat[j] = i.split("    ")
		j = j + 1
	return mat	
def main():
	lat = openFile("/home/aleks/Aleksander/study/Credential/sasha_diplom_data/2013.12.11/lat.grd")
	lon = openFile("/home/aleks/Aleksander/study/Credential/sasha_diplom_data/2013.12.11/lon.grd")
	return 0
main()