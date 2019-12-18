from pymongo import MongoClient 
from urllib.request import urlopen 
  
from urllib.error import HTTPError 
  
from urllib.error import URLError 
  
from bs4 import BeautifulSoup 
import requests 
 
 
 
sesiones=[] 
 
 

lista=[] 
url = 'http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID=3737'
try: 
      
    html = urlopen("http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID=3737") 
      
except HTTPError as e: 
      
    print(e) 
      
except URLError: 
      
    print("Server down or incorrect domain") 
else: 
    source = requests.get(url) 
    content = source.content 
    soup = BeautifulSoup(source.content, "html.parser") 
 
    for a in soup.findAll('proyecto_ley'): 
        me=a.get("boletin") 
        lista.append(me) 
            
    res = BeautifulSoup(html.read(),"html5lib") 

     
    for j in range(len(lista)): 
        re="" 
        texto=" " 
        
        aux=lista[j] 
        tags = res.find("proyecto_ley", {"boletin": aux}) 
        texto=tags.getText() 
 
        resul = res.findAll("intervencion_autoridad", {"descripcion": "Ministra de Transportes y Telecomunicaciones, señora Gloria Hutt"}) 
        for r in resul: 
            re=r.getText() #guarda texto en este caso intervecion ministra de trasportes
 
    ress=[]        
    #print (ress)
    sepa=re.split( )#separa las palabras del texto y las guarda como arreglo para poder recorrerla
    diccionario = {
    "proyecto":["proyecto","iniciativa","idea","plan","planificacion"]#diccionario de prueba
    }
   
    conta=0
    pos_inicial = -1
    lista_pos=[]
    psimi=[]
    for i in range(len(sepa)): #para cada palabra en el texto
        for p in diccionario["proyecto"]:#para cada palabra en el diccionario
                                           #(sinonimo de desarrollo)
            for w in p:                     #para r en esa palabra sinonimo de desarrolo
                                            #que ira cambiando con p
                ress.append(w)              #guardala ahora trozada en letras
            #print (ress)
            for z in range(len(ress)):  #para e en el rango del largo de la palabra trozada
                if ress[z] in sepa[i]:  # si esa letra esta esta en la palabra del texto 
                    conta+=1            #suma 1 
            if conta > len(sepa[i])-2:  # si las letras contadas en la palabra del texto es solo menor a 1 en la palabra del texto
                if len(sepa[i]) >= len(ress): # elimina del margen las palabras cortas
                    for h in diccionario["proyecto"]:
                        if sepa[i]== h:
                                    #psimi.append(sepa[i])
                                    print ("Palabras Similares: ", sepa[i]) #entonces la palabra del diccionario es similar a la analizada en el texto
                                    pos_inicial = re.index(sepa[i], pos_inicial+1) # toma la posicion de la palabra en el texto
                                    lista_pos.append(pos_inicial) # la guarga en un arreglo de posiciones

                                    print("En la posicion: ", lista_pos)# imprime las posciones
    
                        
            conta=0 # reinicia el contador
            
            ress=[] # reinicia el arreglo de letras del sinonimo de desarrollo tomada en este ciclo
    
            
        
    
        
