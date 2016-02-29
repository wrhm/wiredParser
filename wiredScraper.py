# -*- coding: utf-8 -*-

# from bs4 import BeautifulSoup
import urllib, re

url = 'http://www.wired.com/'

def getHomepageStoryLinks():
	print 'Loading homepage...'
	r = urllib.urlopen(url).read()
	print 'Homepage loaded.'
	html_lines = r.split('\n')
	homepageLinks = []
	for line in html_lines:
		if 'a href' in line and 'content' in line:
			hpl = line.split()[1][6:-1]
			homepageLinks.append(hpl)
	return homepageLinks

def cleanUp(par):
	modpar = re.sub('<a href.+>(.+)</a>',r'\1',par)
	modpar = re.sub('&#8212;',' -- ',modpar) #Long dash
	modpar = re.sub('&#8217;','\'',modpar) #Apostrophe
	modpar = re.sub('&#8220;','\"',modpar) #Open quote
	modpar = re.sub('&#8221;','\"',modpar) #Close quote
	return modpar

def getStoryInfo(storyurl):
	storyInfo = {	'storyURL':storyurl,
					'storyTitle':None,
					'authorName':None,
					'storyDate':None,
					'storyTime':None,
					'paragraphs':None }
	r = urllib.urlopen(storyurl).read()
	html_lines = r.split('\n')
	paragraphs = []
	inParagraph = False
	for line in html_lines:
		if 'post-title' in line and storyInfo['storyTitle'] == None:
			storyTitle = line.split('postTitle\">')[-1].split('</')[0]
			if '<h1' in storyTitle:
				storyTitle = '[Need to improve title parsing]'
			storyInfo['storyTitle'] = cleanUp(storyTitle)
		if 'rel=\"author\"' in line:
			authorName = line.split('\">')[1].split('<')[0]
			storyInfo['authorName'] = authorName
		if ' pubdate' in line:
			storyDate = line.split('\"')[-2]
			storyInfo['storyDate'] = storyDate
		if '<time' in line and 'm<' in line:
			storyTime = line.split(' >')[-1][:-7]
			storyInfo['storyTime'] = storyTime
		if '<p>' in line:
			inParagraph = True
		if inParagraph and 'span' not in line:
			pSplit = line.split('<p>')
			if len(pSplit[-1])>0:
				paragraph = pSplit[-1][:-4]
				paragraphs.append(cleanUp(paragraph))
		if '</p>' in line:
			inParagraph = False
	storyInfo['paragraphs'] = paragraphs
	return storyInfo

# storyurl = 'http://www.wired.com/2016/02/space-photos-week-milky-way-gets-close/'
# storyurl = 'http://www.wired.com/2016/02/forcing-apple-hack-iphone-sets-dangerous-precedent/'
# storyurl = 'http://www.wired.com/2016/02/know-spoons-splash-faucets-mit-made-art/'
# gsi = getStoryInfo(storyurl)
# # for e in gsi:
# # 	print '%s: %s'%(e,gsi[e])
# title = gsi['storyTitle']
# author = gsi['authorName']
# date = gsi['storyDate']
# time = gsi['storyTime']
# print '\"%s\" by %s on %s at %s:\n'%(title,author,date,time)
# for e in gsi['paragraphs']:
# 	print '%s\n'%e

''' GOAL: Print titles of all stories on the homepage '''
for story in getHomepageStoryLinks():
	# print getStoryInfo(story)['storyTitle']
	gsi = getStoryInfo(story)
	for e in gsi:
		# if gsi[e] != None:
		if e in ['storyURL','storyTitle']:
			print e, gsi[e]
	print ''
