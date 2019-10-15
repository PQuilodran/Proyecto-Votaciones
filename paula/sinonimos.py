import requests
from bs4 import BeautifulSoup
url='http://www.wordreference.com/sinonimos/'
#Busca los sinonimos en el wordreference
enlace=input("palabra a buscar: ")
buscar=url+enlace
#se le pone al url al final la palabra que se necesita buscar
resp=requests.get(buscar)
#manda la url y esta le reponde con los resultados 
bs=BeautifulSoup(resp.text,'lxml')
lista=bs.find_all(class_='trans clickable')
#Busca solamente las class llamadas trans clickable
for sin in lista:
    sino=sin.find_all('li')
    for fin in sino:
        print(fin.next_element)
