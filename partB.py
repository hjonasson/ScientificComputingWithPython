#Part B, Strings, Lists, Tuples, Loops, Conditionals, File I/O

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
	file = sorted(file)
	newFile = open('ga_sortd.txt','w')
	for line in file:
		newFile.write(line)
	newFile.close
	
