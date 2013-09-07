# flickr downloader
# By Oros
# Licence Public Domaine
import urllib2, json, os, sys
for site in sys.argv[1:]:
	d="./"+(site.split("/")[-2] if site[-1:] == "/" else site.split("/")[-1])+"/"
	if not os.path.exists(d):
		os.makedirs(d)
	page=1
	while True:
		js = json.loads(urllib2.urlopen(site+"?data=1&page="+str(page)+"&append=1").read())
		if 'endpoint' in js:
			break
		for e in js:
			img = open(d+e['name']+"."+e['sizes']['o']['url'].split(".")[-1],'w')
			img.write(urllib2.urlopen(e['sizes']['o']['url']).read())
			img.close()
		page+=1
if not sys.argv[1:]:
	sys.exit("Need url in arguments ! Like :\npython "+sys.argv[0]+" https://secure.flickr.com/photos/XXXXXXXXXXXXX/")