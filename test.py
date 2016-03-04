# from wiredScraper import cleanUp

import re

def cleanUp(par):
	# valids = ''.join([chr(x) for x in xrange(32,127)])
	# modpar = ''.join([x for x in par if x in valids])
	modpar = re.sub('<a href.+?>(.+?)</a>',r'\1',par)
	modpar = re.sub('<em.*?>(.+?)</em>',r'\1',modpar)
	modpar = re.sub('<strong.*?>(.+?)</strong>',r'\1',modpar)
	modpar = re.sub('<div.*?>(.+?)</div>',r'\1',modpar)
	modpar = re.sub('<iframe.+>.+?</iframe>','',modpar)
	modpar = re.sub('<img.+?>.+?</img>','',modpar)
	modpar = re.sub('&#8212;',' -- ',modpar) #Long dash
	modpar = re.sub('&#821[67];','\'',modpar) #Apostrophe
	modpar = re.sub('&#8220;','\"',modpar) #Open quote
	modpar = re.sub('&#8221;','\"',modpar) #Close quote
	return ' '.join(modpar.split())

# def clean(par):
# 	modpar = re.sub('.','1',par)

f = open('artTest.txt','r')
lines = f.readlines()
f.close()

for line in lines:
	print '%s\n'%line
	print '%s\n'%cleanUp(line)
	print '='*50

# print re.sub('.','1','foobar')
# print clean('foobar')