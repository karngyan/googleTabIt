#! python3 

#search.py - Open several webpages corresponding to a google search

import requests,sys,webbrowser,bs4

print("Googling  . . .")
res=requests.get('https://www.google.com/search?q='+' '.join(sys.argv[1:]))

res.raise_for_status()

#Retrieve Top Serach results
soup=bs4.BeautifulSoup(res.text)

#Open a browser tab for each search result
linkElems=soup.select('.r a')
numOpen=min(5,len(linkElems))

for i in range(numOpen):
	webbrowser.open('https://www.google.com'+linkElems[i].get('href'))
	