import partC
import numpy as np

def matrixExp(file,newFile):

	A = partC.matrixRead(file)
	[l,v] = np.linalg.eig(A)
	l = np.diag(np.exp(l))
	expA = np.dot(np.dot(v,l),np.dot(v,np.eye(3,3)))
	partC.matrixWrite(expA,newfile)