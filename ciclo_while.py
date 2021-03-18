#Vediamo come funzionano i cicli while su altri linguaggi di programmazione
while(condition) {    #per prima cosa si deve capire se la condizione risulta vera, se è vera allora il ciclo continuerà ciclicamente (loop), finchè non sarà falsa la condition
  executable code1
  executable code2
  executable code3
}
#vediamo come viene strutturato in python, risulta essere molto più facile
while condition:   
  executable code1 #python sa cosa fa parte del ciclo o meno grazie all'indentazione (spazio vuoto)
  executable code2
  executable code3
executable code4

#vediamo un esempio pratico
while False:
  print("hello") #non stamperà nulla poichè la condiizone è falsa
  
while true:
  print("hello") #stamperà ciclicamente hello
                 #ATTENZIONE, NON INVIARE QUESTO CODICE, ALTRIEMENTI ANDRA' IN TILT IL BROWSER POICHE' STAMPERA' "HELLO" ALL'INFINITO
                 #SE AVETE FATTO PARTIRE IL CODICE USARE CTRL+C

  #Vediamo un esempio pratico
  counter=0             #questo è un indicatore che possiamo chiamare come vogliamo anche "pippo=1, pippo=2, vercingetorige=30"
  while counter<12:     #stiamo comunicando che se il valore che abbiamo assegnato è minore di 12 il codice può continuare, in questo caso può continuare
    print(counter)
    counter=counter+1   #se il ciclo sarà vero aggiunierà sempre a counter (o nome assegnato) +1 fino alla condizione assegnata (cioè <12)
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
10
11   #avremo questo risultato come ci aspettavamo





  
