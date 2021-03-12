#diamo un valore ad "a" e "b"

a=10
b=5

#Aritmetica / qui inizieremo a fare qualche qualche operazione

c=a+b 
d=b/a

#Iniziamo a stampare i risultati e per stampare usiamo l'opzione #print

c         #scrivendo solo "c" possiamo vedere la variabile ma non è un modo corretto per stampare/ avremo come risultato 15 in questo caso
15
print(c)  #modo corretto per stampare 
15
print (d) # in questo caso facciamo una divisione
0.5

#perchè è meglio utilizzare "print()"? vediamo un esempio

c
d
0.5   #il risultato che avremo sarà solo uno, quindi solo una variabile

#mentre se usiamo print() avremo
print(c)
print(d)
15
0.5 #come vediamo avremo entrambi i valori

import math #in questo modo abbiamo importato il modulo matematico (math)
math.sqrt(a) @questa è la funzione per fare la radice quadrata (in questo caso di a)
3.1622776601683795
round(math.sqrt(a)) #usiamo per arrotondare il valore
3

#facciamo un esempio senza numeri, quindi con parole

greeting="hello"
name="marco" #in questo modo stiamo assegnando in modo facile e intuitivo dei valori verbali e non numerici
message= greeting+name @così possiamo definire che il messaggio deve contenere quei 2 valori, quindi "hello" e "marco"
print(message)
hellomarco #avrà stampato il valore ma purtroppo senza uno spazio quindi abbiamo bisogno di definirlo
message=greeting+" "+name #lo spazio si definisce con " " 
print(message)
hello marco #avremo il messaggio con lo spazio e quindi corretto
