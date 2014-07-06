import numpy as np
def iterateLogistic(x0,r,I):

	f = lambda x,y: y*x*(1-x)
	for i in range(I):
		x0 = f(x0,r)

	return x0

def logisticData(delta = .00005):
	for i in range(10):
		file = open('data'+str(i+1),'w')
		x0 = .3 + i * delta
		for j in range(1,51):
			file.write(str(j)+' '+str(x0)+'\n')
			x0 = iterateLogistic(x0,4.,j)
		file.close

def matrixRead(file):

	file = open(file).readlines()	
	return [[float(line.split()[i]) for i in range(len(line.split()))] for line in file]

def matrixWrite(mat,file):

	file = open(file,'w')
	for row in mat:
		for col in row:
			file.write(str(col)+' ')
		file.write('\n')
	file.close

def maxSeparation(file,min,max):

	#Make a list of all files that need to be read
	files = []
	for i in range(min,max+1):
		files.append(file+str(i))

	#Take all relevant data from each file
	datas = []
	for i in files:
		f = open(i).readlines()
		data = [float(line.split()[1]) for line in f]
		datas.append(data)

	#Find the d_max
	d_max = []#[max([datas[i][j]-datas[k][j] for k in range(i+1,len(datas)) for i in range(len(datas))]) for j in range(len(datas[0]))]
	for i in range(len(datas[0])):
		d = []
		for j in range(len(datas)):
			for k in range(j+1,len(datas)):
				d.append(abs(datas[j][i]-datas[j][k]))
		d_max.append(np.max(d)) 
	file = open('d_max','w')
	for i in d:
		file.write(str(i)+'\n')
	file.close





















