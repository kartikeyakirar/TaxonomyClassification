import nltk
import re
from urlparse import urlparse
import pattern.en
import xml.etree.ElementTree as ET
import urllib
from xml.dom.minidom import parse, Node
text=raw_input()
parsedurl=urlparse(text)
tokenurl=re.split('-|/|_|~|(?=\\p{Upper}|[|]|{|}|^)',parsedurl.path)
tokenurl1=re.split('-|/|_|~|&|$|%|^|=|(?=\\p{Upper}|[|]|{|}|^)',parsedurl.query)

urlencd=urllib.quote_plus(text)
urlsock=urllib.urlopen('http://admin.m-bazaar.in/resources/campaign/loyalty/truec/parser.php?target_url=%s' % urlencd)
urlread=urlsock.read().split(",")


with open('temp3.txt','w') as f:
	for item in urlread:
		f.write("%s\n" % item)

f.close()


with open('temp3.txt','r') as q:
		lines = q.read().splitlines()
		filtered = filter(lambda x: not re.match(r'^\s*$', x), lines)


q.close()

with open('temp3.txt','w') as q:
	for item in filtered:
		q.write("%s\n" % item)	


q.close()

with open('temp1.txt','w') as f:
	for item in tokenurl:
		f.write("%s\n" % item)


f.close()
with open('temp1.txt','a') as q:
	for item in tokenurl1:
		q.write("%s\n" % item)

q.close()
with open('temp1.txt','r') as q:
		lines = q.read().splitlines()
		filtered = filter(lambda x: not re.match(r'^\s*$', x), lines)


q.close()

with open('temp1.txt','w') as q:
	for item in filtered:
		q.write("%s\n" % item)	


q.close()



with open('temp1.txt','r') as q:
		lines = q.read().splitlines()


q.close()

a=set(lines)
lines=list(a)

with open('temp1.txt','w') as q:
	for item in lines:
		q.write("%s\n" % item)	


q.close()

fin = open("temp1.txt")
fout = open("temp2.txt", "w+")
delete_list = ['search', 'pr', 'tracker','off','searches','prs','shows','show','otracker','pos','as','1s','1','2','3','4','start','otrackers'
,'searches','on','search','starts','changeBackToAll','urls','clickSrc','false','foundInAlls','santizedKeyword',
'changeBackToAlls','verticals','header','suggesteds','go','ltKeywords','categoryIds'
,'0s','categoryIdSearcheds','categoryIdSearched','catId','headers','noOfResults'
,'falses','santizedKeywords','dealDetails','catIds','categoryId','es','goes','vertical'
,'dealDetail','utmCtents','cityPageUrls','noOfResult','cityPageUrl','noOfResultss','odCatId'
,'suggested','cateryIds','cateryIdSearcheds','cateryIdSearched','id','6bo','ic','6bo','id','ic','Cidz','hom','Cidz','Crlj','Cord','Crlj','cateryId','noOfRult','clickSrcs','keyword','url','ltKeyword','foundInAll','utmCtent','keywords','odCatIds']
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)


fin.close()
fout.close()

with open('temp2.txt','r') as q:
		lines = q.read().splitlines()
		filtered = filter(lambda x: not re.match(r'^\s*$', x), lines)
		lined = [i for i in filtered if len(i) > 1]

q.close()

with open('temp2.txt','w') as q:
	for item in lined:
		q.write("%s\n" % item)	

q.close()


tr=[]
with open('temp2.txt','r') as q:
	lines=q.read().splitlines()
	for x in lines:
		urlsock=urllib.urlopen('http://lookup.dbpedia.org/api/search/KeywordSearch?QueryString=%s' % x)
		f=parse(urlsock)
		for node in f.getElementsByTagName('Result'):
			it=node.getElementsByTagName('Label')
			for g in it:
				tr.append(g.childNodes[0].nodeValue)


q.close()



tq=[]
with open('temp3.txt','r') as q:
	lines=q.read().splitlines()
	for x in lines:
		urlsock=urllib.urlopen('http://lookup.dbpedia.org/api/search/KeywordSearch?QueryString=%s' % x)
		f=parse(urlsock)
		for node in f.getElementsByTagName('Result'):
			it=node.getElementsByTagName('Label')
			for g in it:
				tq.append(g.childNodes[0].nodeValue)


q.close()


with open('pythondump.txt','w') as q:
	for item in tr:
		q.write("%s\n" % item.encode('utf-8'))	


q.close()


with open('phpdump.txt','w') as q:
	for item in tq:
		q.write("%s\n" % item.encode('utf-8'))	


q.close()
	

