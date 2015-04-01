
from pylab import *
# import matplotlib.image as mpimg
import os
def openF
ile(str):
	fd = open(str,'r')
	for i in range(5):
		s = fd.readline()
	mat = []
	for i in fd:
		mt =[float(field) for field in i.strip().lstrip('[').rstrip(']').split()]
		mat.append(mt)
	fd.close()
	return mat
def dirList(str):
	lt =  os.listdir(str)
	return lt
# name
def main():
	fs = open("settings.txt")
	str = fs.readline()
	fs.close()
	lt = dirList(str)
	for name in lt:
		print name
		os.makedirs(name+"/gif/",0755 )
		# lat = openFile(str+name+"/lat.grd")
		# lon = openFile(str+name+"/lon.grd")
		file_dir = dirList(str+name)
		for x in file_dir:
			if x.find("presure") != -1:
				print x
				presure = openFile(str+name+"/"+x)
				plt.figure()
				# img = mpimg.imread('d01_khv75_blank.png')
				# plt.imshow(img)
				CS = plt.contour(presure)
				plt.clabel(CS, inline=1, fontsize=10)
				plt.title('Simplest default with ' + x)
				plt.savefig(name+'/gif/'+ x + '.png')
	return 0


def one_file(str):
	presure = openFile(str)
	plt.figure()
	CS = plt.contour(presure)
	plt.clabel(CS, inline=1, fontsize=10)
	#plt.title('Simplest default with ' + x)
	#plt.savefig(name+'/gif/'+ x + '.png')
	plt.show()
	return 0
one_file("/home/aleks/Aleksander/study/Credential/Project/ReceiveInformation_1/FILE/2013.12.11/test2.txt")
#main()
