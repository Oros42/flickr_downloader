# -*- coding: utf-8 -*-
# flickr downloader
# By Oros
# Licence Public Domaine
import json, os, sys, itertools
try:
	import urllib.request as u
except ImportError:
	import urllib as u
for site in sys.argv[1:]:
	d="./{s}/".format(s=site.rstrip('/').split('/')[-1])
	if not os.path.exists(d):
		os.makedirs(d)
	for p in itertools.count(1):
		js = json.loads(u.urlopen("{site}?data=1&page={p}&append=1".format(site=site,p=p)).read(200000).decode('utf-8'))
		if 'endpoint' in js:
			break
		for e in js:
			img = open("{d}{name}.{ext}".format(d=d,name=e['name'],ext=e['sizes']['o']['url'].split(".")[-1]),'wb')
			img.write(u.urlopen(e['sizes']['o']['url']).read(20000000))
			img.close()
if not sys.argv[1:]:
	sys.exit("Need url in arguments ! Like :\npython {n} https://secure.flickr.com/photos/XXXXXXXXXXXXX/".format(n=sys.argv[0]))