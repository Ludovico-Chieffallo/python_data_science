#ricordiamoci il ciclo while e compariamolo con il ciclo For
counter=0
while counter<12:
    print(counter)
    counter=counter+1

#Per esprimere la stessa cosa del precedente ciclo while possiamo usare il ciclo for in questo modo:
for numero in range(11):     #for è il ciclo, "numero" è un nome assegnato in questo caso e arbitrario, in completa il ciclo, "range" è una funzione che vedremo subito sotto
  print(numero)
0
1
2
3
4
5
6
7
8
9
10 #questo è il risultato che avremo 

#ANALIZZIAMO MEGLIO FUNZIONE "RANGE"
#Perchè abbiamo scritto 11 per avere i valori fino a 10? perchè range inizia a contare da 0, quindi avremo 11 valori che arrivano a 10
#Con la funzione range possiamo gestire 3 parametri (start, stop, step) quindi il punto di inizio, il punto di fine e il passo 
#andiamo quindi a modificare il precedente codice per usare questi parametri.

for numero in range(0,11,2):
    print(numero)
0
2
4
6
8
10 #in questo modo avremo un punto di inizio a 0, fine a 11, con salti di 2 numeri

#Possiamo anche fare dei conteggi negativi
for numero in range(11,0,-1):
    print(numero)
11
10
9
8
7
6
5
4
3
2
1 #in questo modo avremo un conto alla rovescia

#POSSIAMO ANCHE STAMPARE QUALCOSA DI DIVERSO DA NUMERI
for numero in range(5):
    print("hello", numero) #Qui stiamo dicendo di stampare hello(questa volta con "") e poi di restituirci il valore di numero (ricordo che è possibile usare qualsiasi nome) e il valore sarà definito da range che sarà 5 infatti:
#hello 0
#hello 1
#hello 2
#hello 3
#hello 4 #questo è il risultato

#POSSIAMO ANCHE AGGIUNGERE ALTRE LINEE
for numero in range(5):
    print("hello", numero)
    print("-seconda linea")
    print("-terza linea")
#hello 0
#-seconda linea
#-terza linea
#hello 1
#-seconda linea
#-terza linea
#hello 2
#-seconda linea
#-terza linea
#hello 3
#-seconda linea
#-terza linea
#hello 4
#-seconda linea
#-terza linea #QUESTI SARANNO I NOSTRI RISULTATI
