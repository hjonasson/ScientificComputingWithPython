#Part B, Strings, Lists, Tuples, Loops, Conditionals, File I/O

import numpy as np

#Count lines and words in the Gettysburg address
def getGA(file):
	
	file = open(file,'r')
	wordcount = 0
	for word in file.read().split():
		wordcount += 1

	for i,l in enumerate(file):
		pass

	print 'The number of words in the Gettysburg address is '+str(wordcount)+' and the number of lines is '+str(i+1)

#Count vowels in the Gettysburg address
def vowelCount(file):
	
	file = open(file)
	counts = {i:0 for i in 'aeiouAEIOU'}
	for i in file.read():
		if i in counts:
			counts[i] += 1
	
	print 'The vowel count in the Gettysburg address is:', counts

#Sort lines alphabetically, capital letters first? Why not.
def sortFile(file):
	
	file = open(file).readlines()
	file = sorted(file,key = lambda i: i.lower())
	newFile = open('ga_sortd.txt','w')
	for line in file:
		newFile.write(line)
	newFile.close


#1D map iteration
def oneDMapIteration(f,x0,filename):
	
	file = open(filename,'w')
	for i in range(100):
		x1 = f(x0)
		file.write(str(x0)+' '+str(x1)+'\n')
		x0 = x1
	file.close

#1D map analysis
def oneDMapAnalyse(file):

	file = open(file).readlines()
	iterates = [float(i.split()[1]) for i in file]
	mean = np.mean(iterates)
	higher = [i for i in iterates if i>.5]
	frac = float(len(higher))/len(iterates)
	print 'The mean of the iterates is '+str(mean)+' and the fraction of iterates higher than 0.5 is '+str(frac)
























