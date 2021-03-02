#!/usr/bin/env python
# coding: utf-8

# # Ejercio 1
# 
#    - Realiza una variable con tu matricula y realiza una secuencia de imprimir con tu nombre y tu matrícula concatenados.
# 

# In[2]:



n=str(input("Introduce tu nombre: "))
m=int(input("Introduce tu matricula: "))

print(n+" "+str(m))


# # Ejercicio 2
# 
#    - Pidiendo el input del usuario pide dos números y crea una pequeña calculadora con los operadores básicos de suma, resta, multiplicación, división, y exponente.

# In[4]:


print("\t\tCalculador de operaciones")
def menu():
    print("\n\nMenu de opciones\n 1)Suma\n 2)Resta\n 3)Multiplicacion\n 4)Division\n 5)Exponencial\n 0)Salir")

opc=0
while opc != 6 :
    menu()
    
    opc=int(input("Introduzca la opcion deseada: "))
    
    if opc == 0 :
        break
        
    if  opc>=6:
        
        print("Favor de introducir una opcion valida")
        menu()
        opc=int(input("Introduzca la opcion deseada: "))
        
    a1=float(input("Introduzca el primer valor deseado: "))
    a2=float(input("Indroduzca se segundo valor deseado: "))
    
    if opc==1:
        print("El resultado de",a1,"+",a2, "es=", a1+a2)
    elif opc==2:
        print("El resultado de ",a1, "-", a2, "es=", a1-a2)
    elif opc==3:
        print("El resultado de ", a1,"*",a2, "es=", a1*a2)
    elif opc==4:
        if a2==0:
             print("Valores no validos")
        else:
             print("El resultado ", a1, "/",a2,"es=", a1/a2)
    elif opc==5 :
        print("El resultado de ",a1, "elevado a la potencia de",a2, "es=", a1**a2)
        
    else:
        print("Favor de introducir una opcion valida")
    


# # Ejercicio 3
# 
#    - Con loop while o for, realiza una lista de 10 números múltiplos de 3, y después realiza una función de loop que sume todos los números dentro del arreglo.

# In[6]:


i=3
suma=0
acum=0
multiplos=[ ]

while acum < 10:
    if i%3==0:
        multiplos.append(i)
        suma=suma+i
        acum=acum+1
    i=i+1

print("\nPrimeros multiplos del 3: ", multiplos)
print("\nSumatoria de los multiplos obtenidos: ", suma)


# # Ejercico 4
#     
#    - Con una función de if else, revisar si un número es par o es impar. Con una función de if else, revisar si un número es primo o no.

# In[11]:



num=int(input("Introduzcca un numero: "))
if(num%2==0):
    print("\nSu numero es par")
     
else:
    print("\nSu numero es impar")
cont=0
for n in range (1, num+1):
    if num%n==0:
        cont=cont+1

if cont==2:
    print("\n", num, "es un número primo.")
else:
    print("\n", num, "no es un número primo.")


# # Ejercicio 5
# 
#    - Utilizando diferentes clases en python, crea una calculadora con los operadores básicos de suma, resta, multiplicación, división, y exponente.

# In[15]:


class calculadora:
    def sumar(self, x, y):
        print ('El resultado de la suma de  ' +str(x) + ' y '+str(y)+ ' es igual a: '+str((x+y)) )
    def restar(self, x, y):
        print ('El resultado de la resta de  '+str(x) + ' y '+str(y)+ ' es igual a: '+str((x-y)) )
    def multiplicar(self, x, y):
        print ('El resultado de la multiplicar de '+str(x) + ' y '+str(y)+ ' es igual a: '+str((x*y)) )
    def dividir(self, x, y):
        print ('El resultado de dividir  '+str(x) + ' y '+str(y)+ ' es igual a: '+str((x/y)) )
    def exponente(self, x, y):
        print ('El resultado de elevar a una potencia  '+str(x) + ' y ' +str(y)+ ' es igual a: '+str((x**y)) )

calc= calculadora()
def menu():
    print("""
    ¿Qué quieres hacer?
    1) Sumar los números
    2) Restar los números
    3) Multiplicar los números
    4) Dividir los números
    5) El exponente de los números 
    6) Salir
    """)
    return int(input('Introduce una opción: '))

while(True):
    opción= menu()
    if(opción==6):
        break
    else:
        num1= int(input('Ingresa el primer número: '))
        num2= int(input('Ingresa el segundo número: '))
        
        if(opción==1):
            calc.sumar(num1, num2)
        elif(opción==2):
            calc.restar(num1, num2)
        elif(opción==3):
            calc.multiplicar(num1, num2)
        elif(opción==4):
            calc.dividir(num1, num2)
        elif(opción==5):
            calc.exponente(num1, num2)
        else:
            print('Opción no valida')


# # Ejercicios con estructuras básicas de Phyton
# 
# ## Tuplas
#     Las tuplas son objetos iterativos, son inmutables y se identifican mediante parentesís
# - Crear una variable flotante, integer, boleana y compleja e imprimir el tipo de variable que es.

# In[17]:


x=86.79 
tipo1=type(x)
print ("La variable es",x, "y es de tipo",tipo1)

y=751 
tipo2=type(y)
print("La variable es",y, "y es de tipo", tipo2)

IscodingFun=True 
tipo3=type(IscodingFun)
print("La variable es",IscodingFun,"y es de tipo",tipo3)

Complex=657+4j 
tipo4=type(Complex)
print("La variable es", Complex, "y es de tipo", tipo4)


# - Crear una tupla con valores enteros imprimir el primer y último valor.

# In[18]:


listatupla = (1,2,3)
print("Primer valor de la tupla es igual a:",listatupla[0], "y el último es igual a:",listatupla[2],"\n")


# - Verificar si una variable existe dentro de la tupla.

# In[31]:


tup=('a','e','i','o','u')
a=str(input("Ingrese un dato a buscar:"))
if ((a in tup)==True):
    print("su dato fue encontrado en la tupla")
else:
    print("su dato no fue encontrado en la tupla")


# ## Listas
#    - Crear una lista con 40 elementos aleatorios enteros.

# In[32]:


import random
listAle=[random.randint(0,3928) for i in range(40)]
print("Los 40 elementos son:",listAle)


# - Con una funcion (def) crear dos listas nuevas a partir de la lista creada por numeros aleatorios, en la cual en una esten los elementos pares, y en la otra los elementos impares.

# In[33]:


listAle=[3674, 2788, 3059, 1958, 3324, 3772, 3029, 1708, 1972, 2005, 217, 2132, 2522, 1456, 546, 43, 401, 1666, 2404, 1928, 353, 324, 2753, 735, 2155, 263, 1569, 3066, 2993, 3344, 2925, 2217, 1474, 929, 3595, 2300, 370, 3762, 2279, 3576]
listpar=[]
listimp=[]
def listas():
    for i in range(40):
        h=listAle[i]%2
        if h==0:
            listpar.append(listAle[i])
        else:
            listimp.append(listAle[i])
    print("La lista de numeros pares aleatorios es:",listpar)
    print("La lista de numeros impares aleatorios es:",listimp)
listas()


# - Ordenar los elementos de la lista par de mayor a menor, y los de la lista impar de menor a mayor.

# In[38]:


istpar=[3674, 2788, 3059, 1958, 3324, 3772, 3029, 1708, 1972, 2005, 217, 2132, 2522, 1456, 546, 43, 401, 1666, 2404, 1928, 353, 324, 2753, 735, 2155, 263, 1569, 3066, 2993, 3344, 2925, 2217, 1474, 929, 3595, 2300, 370, 3762, 2279, 3576]
listimp=[917, 175, 85, 339, 397, 475, 1161, 891, 735, 1185, 213, 419, 363, 877, 335, 673, 745]
listpar.sort(reverse=True)
listimp.sort()
print("Lista par ascendente: ", listpar,"\nLista impar descendente: ",listimp)


# - Utilizar al menos cuatro de las funciones de listas en python en la lista original de 40 elementos.

# In[39]:


listAle=[3674, 2788, 3059, 1958, 3324, 3772, 3029, 1708, 1972, 2005, 217, 2132, 2522, 1456, 546, 43, 401, 1666, 2404, 1928, 353, 324, 2753, 735, 2155, 263, 1569, 3066, 2993, 3344, 2925, 2217, 1474, 929, 3595, 2300, 370, 3762, 2279, 3576]
listAle.insert(2,424)
b=listAle.count(424)
print("Cantidad de datos en lista :",len(listAle),"\nNumero mayor de los datos:",max(listAle),"\nNumero menor de los datos:",min(listAle), "\nSuma de los datos de la lista: ",sum(listAle))
print("Numero de veces que aparece el 424 en la lista: ",b)


# ## Diccionario
#   - Crear un diccionario de 6 personas que conozcas con su primer nombre y su edad.

# In[45]:


dic={'Aranza':'19','Azael':'21','Andres':'21','Jose':'22','Francisco':'21','Fabiola':'20'}


# - Crear una lista con los valores de la edad y reacomodar la lista de menor a mayor valor.

# In[48]:


dic={'Aranza':19,'Azael':21,'Andres':21,'Jose':22,'Francisco':21,'Fabiola':20}
edad=[]
for i in diccionario:
    if type(diccionario[i]) == type(98):
        edad.append(diccionario[i])
edad.sort()
print("Las edades son:",edad)


# - Usando el diccionario y un loop, imprimir solo los nombres

# In[50]:


diccionario={'Aranza':19,'Azael':21,'Andres':21,'Jose':22,'Francisco':21}
a=diccionario.keys()
print(a)


# - Añadir dos personas nuevas a tu diccionario, incluyendo edad

# In[51]:


diccionario={'Aranza':19,'Azael':21,'Andres':21,'Jose':22,'Francisco':21}
diccionario['Cesar']=21
diccionario['Karla']=25
print(diccionario)


# ## Sets
#    - Crea un set con 100 numeros aleatorios enteros del 1 al 25.

# In[54]:


import random
def listaSets(a):
    lista = [0]  * a
    for i in range(a):
          lista[i] = random.randint(1, 25) #Rango de numeros para crear la lista
    return lista

print("Ingrese cuantos numeros aleatorios desea obtener")
a=int(input())


secs=listaSets(a)
print(secs)

secs=set(secs)
print(secs)


# - Compruebe la longitud de tu set 

# In[55]:


import random as r
p=set()
for i in range(100):
    s=r.randint(1,25)
    p.add(s)
print("Los sets no tienen valores duplicados:",p)
print("Por eso su longitud es:",len(p))


# - Crea una lista de 5 numeros aleatorios del 1 al 10 y comprueba si cada valor aparece en el set inicial.

# In[56]:


lista = []

for i in range(5):
    lista.append(r.randint(1,10))
    if lista[i] in p:
        print("El numero", lista[i],"aparece en el set.")
    else:
        print("El numero", lista[i],"No aparece en el set.")


# In[ ]:




