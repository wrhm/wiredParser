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

prevLen = 6 # length of prefix preview for displayed words
mcsi = 5 # most common start index
mcei = 10 # most common end index
print '  Author - words/unique(#articles)',
for folder in os.listdir('Corpora'):
	wcFolder = dict()
	nwFolder = 0
	nFiles = 0
	for filename in os.listdir('Corpora/%s'%folder):
		[nw,wc] = wordCounts(folder,filename)
		for w in wc:
			if w in wcFolder:
				wcFolder[w] += wc[w]
			else:
				wcFolder[w] = wc[w]
		nwFolder += nw
		commons = []
		for w in sorted(wc, key=wc.get, reverse=True):
		  	# commons.append('%s %d'%(w, wc[w]*10000/nw))
		  	commons.append(w)
		  	#This normalizes the count to that in a 10000-word piece
		# print '%s.%s - %4d/%d: %s'%(folder[:8],filename[:5],nw,len(commons),commons[:10])
		nFiles += 1
	fCommons = []
	for w in sorted(wcFolder, key=wcFolder.get, reverse=True):
	  	# commons.append('%s %d'%(w, wc[w]*10000/nw))
	  	fCommons.append([w,wcFolder[w]])
	# print '%s - %4d/%4d(%d): %s'%(folder[:8],nwFolder,len(fCommons),nFiles,fCommons[:10])
	print '\n%s - %5d/%5d(%d):'%(folder[:8],nwFolder,len(fCommons),nFiles),
	for [w,wc] in fCommons[mcsi:mcei]: # print the nmc most common words per author
		preview = w[:prevLen]
		if len(w)>prevLen:
			preview = preview[:prevLen-2]+'..'
		plenform = '%%%ds(%%3d)'%prevLen #may need to increase 3 as corpus grows
		print plenform%(preview,wc),
		# print '%8s'%preview,
