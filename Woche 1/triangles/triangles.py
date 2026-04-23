#Anzahl Dreiecke
t = int(input())

#Wie oft soll es wiederholt werden
for i in range(t):

    #wie viele reihen hat das erste Dreieck
    n = int(input())

    #Neu anfang für jedes neue Dreieck
    summe = 0

    #Reihennummer von 1 - n (+1 da es ansonsten bei n stoppt ohne diese auszuführen)
    for j in range(1, n + 1):

    #z.b
    # j = 1  -> summe = 0  + 1  = 1
    # j = 2  -> summe = 1  + 2  = 3
        summe = summe + j

    print(summe)