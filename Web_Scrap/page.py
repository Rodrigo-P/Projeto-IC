import matplotlib.pyplot as plt
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re

#url="https://www.scopus.com/authid/detail.uri?origin=AuthorProfile&authorId=10140494200&zone="

url="https://censo2010.ibge.gov.br/sinopse/index.php?uf=35&dados=26#topo_piramide"

driver=webdriver.Firefox()

action=webdriver.ActionChains(driver)


try:
	driver.get(url)
except:
	pass

names=[]

soup=BeautifulSoup(driver.page_source,'lxml')

'''
badges=driver.find_element_by_css_selector("div[id='subjectAreaBadges']")

li=badges.find_elements_by_css_selector("span[class='badges']")

areas=""

for el in li:
	areas=areas+el.get_attribute('innerHTML')+'|'
	print el.get_attribute('innerHTML')
print areas
'''

time.sleep(2)


file=open("test.html","w")
file.write(str(soup))
file.close()

#driver.close()
driver.quit()