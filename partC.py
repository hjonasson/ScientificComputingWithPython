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