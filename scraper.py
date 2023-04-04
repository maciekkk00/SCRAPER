import requests
from bs4 import BeautifulSoup
import pandas as pd
from os import listdir
import dao

def extractLinks(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content,"html.parser")
    names = []
    for a in soup.find_all('a', class_='description', href=True):
        names.append(a['href'])
        #print("-----------------------")
        #print(names)
    return names

def extractData(tableName):
    dao.truncateTable(tableName)
    pageNumber = 2
    lista = []
    componentsList = []
    listaSkladnikow = []
    for x in range(pageNumber):
        baseURL = f"https://kuchnialidla.pl/przepisy/dania-glowne/{x+1}#lista"
        lista.extend(extractLinks(baseURL))
        #print("-----------------")
        #print(lista)
    id = 0
    for x in lista:
        URL = f"https://kuchnialidla.pl{x}"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content,"lxml")
        title = soup.find('h1')
        components = soup.find('div', class_='skladniki')
        componentsList.append(components)
        description = soup.find(id="opis")
        id += 1
        image = 'lidl-logo.png'
        recipe = []
        recipe.append(id)
        recipe.append(title.text)
        recipe.append(description.text)
        recipe.append(image)
        print("--------------------------------")
        #print(recipe)
        dao.insertData(recipe, tableName)
    idd=0   
    for ul in componentsList:
        idd+=1
        listaSkladnikow.append(idd)
        for li in ul.findAll('li')[:10]:
            listaSkladnikow.append(li.text)
        for i in range(1,11):
            if len(listaSkladnikow)<11:
                listaSkladnikow.append(' ')
        print("--------------------------------")
        #print(listaSkladnikow)                       
        dao.insertData2(listaSkladnikow, tableName)
        listaSkladnikow = [] 

    print("Job is finished...")
    return componentsList

extractData('recipes')

