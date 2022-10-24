from unidecode import unidecode
import matplotlib.pyplot as plt
from selenium import webdriver
from bs4 import BeautifulSoup
import networkx as nx
import time
import re


def add_art(G,title,names,year,source,citations):
	for x in range(0,len(names)):
		for y in range(x+1,len(names)):
			G.add_edge(names[x],names[y],key=title,year=year,source=source,citations=citations)

G=nx.MultiGraph()

url="https://www.scopus.com/authid/detail.uri?origin=AuthorProfile&authorId=10140494200&zone="
options=webdriver.FirefoxOptions()
options.add_argument('-headless')

driver=webdriver.Firefox(firefox_options=options)

driver.implicitly_wait(10)
driver.get(url)

names=[]

soup=BeautifulSoup(driver.page_source,'lxml')
a=soup.find_all("a",{"class": "ddmDocTitle"})

if len(a)==0:
	tr=soup.find_all("tr",{"class": "searchArea"})
	for art in tr:
		span=art.find_all("span")
		td=art.find_all("td")

		title=unidecode(span[0].contents[0].lower())
		for i in range(1,len(span)):
			if ('.' in span[i].contents[0]) and not('...' in span[i].contents[0]):
				names.append(unidecode(span[i].contents[0].lower()))

		year=td[-3].contents[0]
		year=year.replace('\n','')

		source=td[-2].contents[0].lower()
		source=unidecode(source.replace('\n',''))

		citations=td[-1].contents[0]
		citations=citations.replace('\n','')
		
		add_art(G,title,names,year,source,citations)
		del names[:]
else:
	i=1
	nxt=driver.find_element_by_css_selector("a[data-value='"+str(i)+"']")

	while nxt!=None:
		nxt.click()
		time.sleep(2)
		soup=BeautifulSoup(driver.page_source,'lxml')

		tr=soup.find_all("tr",{"class": "searchArea"})
		for art in tr:
			a=art.find_all("a")
			
			title=a[0].contents[0].lower()
			for i in range(1,len(a)-1):
				if ('.' in a[i].contents[0]) and not('...' in a[i].contents[0]):
					names.append(a[i].contents[0].lower())
			
			if len(art.find_all("a",{"class": "ddmDocSource"}))>0:
				source=(art.find_all("a",{"class": "ddmDocSource"}))[0].contents[0].lower()
			else:
				source=(art.find_all("td",{"data-type": "source"}))[0].contents[0].lower()
			
			source=source.replace('\n','')

			year=(art.find_all("span",{"class": "ddmPubYr"}))[0].contents[0]
			year=year.replace('\n','')		

			cit=art.find_all("td",{"class": "textRight"})
			if len(art.find_all("a",{"title": "View the documents that references this one"}))>0:
				citations=(art.find_all("a",{"title": "View the documents that references this one"}))[0].contents[0]
			else:
				citations=cit[-1].contents[0]
			citations=citations.replace('\n','')

			add_art(G,title,names,year,source,citations)
			del names[:]

		try:
			nxt=driver.find_element_by_css_selector("a[data-value='"+str(i)+"']")
		except:
			nxt=None
pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=100)

nx.draw_networkx_edges(G, pos, width=1)

nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')


plt.axis('off')
plt.show()

nx.write_gml(G, 'network.gml')

file=open("Nx.txt","w")
file.write(str(G.nodes(data=True)).encode('utf-8'))
file.close()

'''
file=open("Edu_source.html","w")
file.write(str(soup))
file.close()
'''

driver.quit()