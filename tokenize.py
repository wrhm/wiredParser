import os, string

# regex = '[A-Za-z]+'
valids = string.ascii_lowercase+string.ascii_uppercase+' '

def wordCounts(folder,filename):
	wordCounts = dict()
	numWords = 0
	f = open('Corpora/%s/%s'%(folder,filename),'r')
	lines = f.readlines()
	f.close()
	for line in lines[5:]:
		cleanLine = string.lower(''.join([x for x in line if x in valids]))
		for word in cleanLine.split():
			if word in wordCounts:
				wordCounts[word] += 1
			else:
				wordCounts[word] = 1
			numWords += 1
	return [numWords,wordCounts]

# # Calculate the fraction of occurrence of each
# # unique word, and normalize out of 1000000
# wordProp = dict()
# for w in wordCounts:
# 	wordProp[w] = int(1000000*(1.*wordCounts[w]/numWords))

# for w in sorted(wordProp, key=wordProp.get, reverse=True):
#   print w, wordProp[w]

for folder in os.listdir('Corpora'):
	for filename in os.listdir('Corpora/%s'%folder):
		[nw,wc] = wordCounts(folder,filename)
		commons = []
		for w in sorted(wc, key=wc.get, reverse=True):
		  	commons.append('%s %d'%(w, wc[w]*10000/nw))
		  	#This normalizes the count to that in a 10000-word piece
		print '%d: %s'%(nw,commons[:10])