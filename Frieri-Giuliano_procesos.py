import random, time

#En el caso de estar en desorden se puede usar pat = sorted(pat.items(), key=operator.itemgetter(1))
# o key=lambda item: item[1]

#------- Funciones -------#
def fcfs():
    wt = dict()
    tat = dict()
    gc = 0
    c = 0
    pfcfs = sorted(patbt.items())
    for at, bt in pfcfs:
        if c == 0:
            gc += bt
            wt[c] = 0
            tat[c] = bt
            #print(c)
        else:
            gc += bt
            wt[c] = gc - at
            tat[c] = bt + wt[c]
            #print(c)
        c+=1        

    promwt = sum(wt.values())/len(wt)
    promtat = sum(tat.values())/len(tat)

    return promwt, promtat

def sjf():
    wt = dict()
    tat = dict()
    gc = 0
    c = 0
    psjf = sorted(patbt.items(), key=lambda item:item[1])
    for at, bt in psjf:
        wt[c] = gc - at
        gc += bt
        tat[c] = gc - wt[c]
        #print(c)
        c+=1

    promwt = sum(wt.values())/len(wt)
    promtat = sum(tat.values())/len(tat)
    
    return promwt, promtat

def srtf():
    wt = dict()
    tat = dict()
    gc = 0
    c = 0

    psrtf = sorted(patbt.items())
    if c == 0:
        at, bt = psrtf[0]
        gc += bt
        wt[c] = 0
        tat[c] = bt
        c+=1
    psrtf.pop(0)

    psrtf.sort(key=lambda items: items[1])
    for at, bt in psrtf:
        wt[c] = gc - at
        gc += bt
        tat[c] = gc - at
        #print(c)
        c+=1 

    promwt = sum(wt.values())/len(wt)
    promtat = sum(tat.values())/len(tat)

    return promwt, promtat

def inicioFCFS():
    wtprom = 0
    tatprom = 0

    inicio = time.time()

    for i in range(10000):
        wtprom, tatprom = fcfs()

    duracion = time.time() - inicio
    print('Duración del FCFS:', duracion)
    print('Waiting Time promedio FCFS:', wtprom)
    print('Turn Around Time promedio FCFS:', tatprom)
    return

def inicioSJF():
    wtprom = 0
    tatprom = 0

    inicio = time.time()

    for i in range(10000):
        wtprom, tatprom = sjf()

    duracion = time.time() - inicio
    print('Duración del SJF:', duracion)
    print('Waiting Time promedio SJF:', wtprom)
    print('Turn Around Time promedio SJF:', tatprom)
    return

def inicioSRTF():
    wtprom = 0
    tatprom = 0

    #print(psrtf) 

    inicio = time.time()

    for i in range(10000):
        wtprom, tatprom = srtf()

    duracion = time.time() - inicio
    print('Duración del SRTF:', duracion)
    print('Waiting Time promedio SRTF:', wtprom)
    print('Turn Around Time promedio SRTF:', tatprom)
    return

#Inicio declarar procesos
patbt = dict()
for i in range(20):
    tiempo = random.randrange(0,100,1)
    patbt[tiempo] = random.randrange(1000,2000,1)
#Fin declarar procesor

#----First Come First Served-----#
inicioFCFS()
print('----------')
#------- Shortest Job First -------#
inicioSJF()
print('----------')
#------- Shortest Remaining Time First -------#
inicioSRTF()