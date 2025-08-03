
#character_name = "Raúl"
#character_age = 26.56
#is_male = True
#print("There once was a man named " + character_name + ", ")
#print("he was " + character_age + " years old. ")

#character_name = "Pepe"
#print("He really like the name " + character_name + ", ")
#print("but didn't like being " + character_age + ".")

#TRABAJANDO CON CADENAS

#print("Giraffe\"Academy")
#Usamos la \ para imprimir comillas sin cerrar la string

#phrase = "Giraffe Academy"
#print(phrase + " is cool")
#Creamos una string combinando una variable y una string

#phrase = "Giraffe Academy"
#print (phrase.upper().isupper())
#Pedimos que ponga en mayúsculas todo y después que confirme

#phrase = "Giraffe Academy"
#print(len(phrase))
#Contamos la longitud de nuestra variable

#phrase = "Giraffe Academy"
#print(phrase[0])
#Buscamos la posición concreta de un carácter en la frase.
#Comenzamos los índices con 0.

#phrase = "Giraffe Academy"
#print(phrase.index("Gir"))
#Aquí hacemos la inversa, pedimos el índice del carácter donde empieza la cadena.

#phrase = "Giraffe Academy"
#print (phrase.replace("Giraffe", "Elephant"))
#Típica función de reemplazar, se usa phrase.replace

#TRABAJANDO CON NÚMEROS

#print(-2.0987 - 4)
#print (3/(2-4))
#print (10 % 3) Nos da el resto

#my_num = 5
#print(my_num)
#Podemos trabajar con variables de números

#my_num = 5
#print (str(my_num) + " mi número favorito")
#Imprimir números en cadenas

#my_num = -5
#print(abs(my_num))
#Función que da el absoluto

#my_num = -5
#print(pow(my_num, 2))
#Para obtener la potencia

#print(max(4, 6))
#Min y max nos dan el número más peq. o más grande

#print(round(3.7))
#Redondea el número

#from math import *
#print (floor(3.7))
#print (ceil(3.2))
#print (sqrt(36))
#Importamos un módulo externo para hacer funciones matemáticas

#CONSEGUIR INPUTS DE USUARIOS

#name = input("Enter your name: ")
#age = input("Enter your age: ")
#print ("Hello" + name + "! You are" + age)

#CREAR UNA CALCULADORA BÁSICA

#num1 = input("Enter a number: ")
#num2 = input("Enter a number: ")
#result = float(num1) + float(num2)
#print(result)
#Ponemos float en lugar de int para aceptar decimales

#JUEGO MAD LIBS

#color = input ("Enter a color: ")
#plural_noun = input ("Enter a plural noun: ")
#celebrity = input ("Enter a celebrity: ")

#print ("Roses are " + color)
#print (plural_noun + " are blue")
#print ("I love " + celebrity)

#LISTAS

#friends = ["Kevin", "Karen", "Jim", "Oscar"]
#              0        1       2       3
#print (friends)
#Imprime todos los amigos

#print (friends[2])
#Imprime solo un elemento de la lista (si empezamos a contar por la derecha, el primero es -1)

#print (friends[1:3])
#Coge un rango, el 1 y el 2.

#friends[1] = ("Mike")
#print (friends[1])
#Con esta modificación, ya no nos da a Karen, nos da a Mike. Podemos hacer cambios posteriores en las listas

#FUNCIONES DE LISTAS

#lucky_numbers = [4, 8, 15, 16, 23, 42]
#friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#friends.extend (lucky_numbers)
#print(friends)
#Esto permite sumar dos listas conjuntamente

#friends.append("Creed")
#print (friends)
#Agregamos otro elemento a una lista

#friends.insert(1, "Kelly") #Añade un elemento
#friends.remove ("Jim") #Elimina un elemento
#friends.clear() #Limpia la lista
#friends.pop() #Elimina el último elemento
#print(friends.index("Toby")) #Encuentra el elemento en la lista
#print (friends.count("Toby")) #Cuenta cuantas veces está un elemento en la lista
#friends.sort() #Lo pone en orden alfabético (también con números en ascendente)
#lucky_numbers.reverse #Invierte el orden de la lista
#friends2 = friends.copy() #Copia una lista
#print(friends2)

#TUPLAS

#Es un tipo de datos, un contenedor donde almacenar diferentes valores (similar a la lista)
#coordinates = (4, 5) #Esto es la tupla. Una tupla es INMUTABLE, no se puede cambiar
#print(coordinates[0]) #Imprimimos el índice 0, o sea 4
#Diferencia entre tuplas y listas: Primeros usan paréntesis, en vez de corchetes. Los primeros no se pueden modificar.
#coordinates = [(4, 5), (6, 7), (80, 34)] #Podemos hacer una lista de tuplas

#FUNCIONES

#Colección de código que realiza una tarea específica. Utilizamos "def"
#Automáticamete se usa una sangría para que se incluya dentro de la función
#def say_hi(name, age):
#    print("Hello " + name + ", you are " + str(age))
#El código de una función no se ejecuta de forma predeterminada. Así que hay que llamarla
#print ("Top") #Esto es una impresión
#say_hi() #Esta es la función
#print ("Bottom") #Esto es una impresión
#Un parámetro es una pieza de información que le damos a la función
#say_hi("Mike", 35)
#say_hi("Steve", 70)

#DECLARACIÓN RETURN

#def cube(num):
#    return num*num*num

#result = cube(4)
#print(result)
#Usamos return para que devuelva el parámetro que pedimos.

#DECLARACIÓN IF
#PODEMOS AYUDAR A NUESTROS PROGRAMAS A TOMAR DECISIONES

#EXPLICACIÓN
#I wake up
#If I'm hungry
#   I eat breakfast

#I leave my house
#if it's cloudy
    #I bring an umbrella
#otherwise
    # I bring sunglasses

#Im at a restaurant
#if I want meat
    #I order a steak
#otherwise if I want pasta
    #I order spaghetti & meatballs
#otherwise
    # I order a salad

#EJEMPLO
#is_male = False
#is_tall = True

#if is_male or is_tall:
#    print("You are a male or tall or both")
#else:
#    print("You are neither male or tall")

#if is_male and is_tall:
#    print("You are a tall male")
#elif is_male and not(is_tall)
#    print("You are a short male")
#elif not(is_male) and is_tall
#    print("You are not a male but tall")
#else:
#    print("You are either not male or not tall or both")

#DECLARACIÓN IF Y COMPARACIONES

#def max_num(num1, num2, num3):
#    if num1 >= num2 and num1 >= num3:
#        return num1
#    elif num2 >= num1 and num2 >= num3:
#        return num2
#    else:
#        return num3
#print (max_num(300,6,5))

#CREAR UNA CALCULADORA MEJOR