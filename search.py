# search.py
# Author: wrhm
# Date Created: 01 Mar 2016
#    Last Edit: 01 Mar 2016

import sys, os, string

if len(sys.argv) == 1:
	print 'Please specify search terms.'
	exit()

searchTerms = sys.argv[1:]
query = string.lower(' '.join(searchTerms))
maxNum = 25
numResults = 0
for folder in os.listdir('Corpora'):
	for filename in os.listdir('Corpora/%s'%folder):
		f = open('Corpora/%s/%s'%(folder,filename))
		lines = f.readlines()
		f.close()
		lineno = 1
		for line in lines:
			if query in string.lower(line):
				prevMin = max(0,line.find(query)-10)
				prevMax = min(line.find(query)+30,len(line)-1)
				preview = line[prevMin:prevMax]
				if prevMin > 0:
					preview = '...'+preview
				if prevMax < len(line)-1:
					preview = preview+'...'
				print '%s.../%s.../%2d: \"%s\"'%(folder[:8],filename[:5],lineno,preview)
				numResults += 1
				if numResults == maxNum:
					break
			lineno += 1
		if numResults == maxNum:
			break
	if numResults == maxNum:
		break