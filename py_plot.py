import matplotlib.image as mpimg
from pylab import *
# import matplotlib.image as mpimg
import os
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
def dirList(str):
	lt =  os.listdir(str)
	return lt
# name
def absl(lon):
	mat =[]
	for x in lon:
		mt = []
		for y in x:
			if y < 0 :
				mt.append(y+360)
			else: mt.append(y)
		mat.append(mt)
	return mat
def printlon(ar):
	for x in ar:
		for y in x:
			if y < 0 :
				print y
	return 0 
def strInt(index):
	if index < 10:
		return "0" +str(index)
	return str(index) 
def main():
	img=mpimg.imread('img_100.png')
	levs = range(840,1200,5)
	fs = open("settings.txt")
	str = fs.readline()
	fs.close()
	lt = dirList(str)
	# lat = openFile("lat.grd")
	# lon = absl(openFile("lon.grd"))
	# printlon(lon)
	for name in lt:
			os.makedirs(name+"/gif/",0755 )
			file_dir = dirList(str+'/'+name)
			for q in file_dir:
				f_dir = dirList(str+'/'+name+"/"+q)
				for x in f_dir:
					if x.find("presure") != -1:
						print x
						presure = openFile(str+'/'+name+"/"+q+"/"+x)
						fig = plt.figure()
						plt.clf()
						# img = mpimg.imread('d01_khv75_blank.png')
						# plt.imshow(img)
						plt.imshow(img,extent=[0,500,0,400])
						# CS = plt.contour(lon,lat,presure,levs,
						CS = plt.contour(presure,levs,
		                 origin='lower',
		                 linewidths=1,
		                 antialiased=True,
		                 nchunk=0.5,
		                 colors='black')
						plt.clabel(CS,inline=1,
		                 inline_spacing=0,fontsize=8,fmt='%2.0f',colors='black')
						plt.title('Simplest default with ' + x)
						plt.savefig(name+'/gif/'+ x + '.png',pad_inches=0.05, dpi=100)
						plt.close(fig)
	return 0


def one_file(str):
	img=mpimg.imread('img_100.png')
	presure = openFile(str)
	plt.figure()
	plt.imshow(img,extent=[0,500,0,400])
	CS = plt.contour(presure)
	plt.clabel(CS, inline=1, fontsize=10)
	#plt.title('Simplest default with ' + x)
	#plt.savefig(name+'/gif/'+ x + '.png')
	plt.show()
	return 0
# one_file("/home/aleks/Aleksander/study/Credential/Project/ReceiveInformation_1/FILE10/2013.12.11/presure_00.txt")
main()
