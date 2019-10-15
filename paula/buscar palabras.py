#el usuario dice una palabra y contamos cuantas veces aparece en el Quijote  
palabra=input("Diga qué palabra quiere buscar: ")  
f=open("file.txt")  
libro=f.read()  
n=libro.count(palabra)  
f.close()  
print("la ",palabra," aparece ",n," veces.")  
